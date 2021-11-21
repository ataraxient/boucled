import timeloop
import time
import random
from datetime import timedelta

from jvc import JVC

class BotJVC():
    def __init__(self, topic_generator, tickrate=10):
        '''
        Class which defines a jvc bot

        Parameters
        ----------
        cookie : string
            coniunctio cookie associated to a connection

        topic_generator : TopicGenerator object
            TopicGenerator object which generate topics, see generators.py

        tickrate : int
            number of minutes between each topics
        '''
        self.generator = topic_generator
        self.tickrate = tickrate

        self.topic_count = 0
        self.tl = timeloop.Timeloop()
        self.client = JVC(self.getCookie()[1])

    def getCookie(self):        
        '''
        Takes a cookie from the cookies.txt file, and returns a pair (account,cookie)
        '''
        with open('cookies.txt','r') as f:
            data = f.read()
            cookie = random.choice(data.split('\n')).split(' ')
        return cookie

    def log(self):
        print('Date : {}, topics posted : {}'.format(time.ctime(),self.topic_count))

    def run(self):
        @self.tl.job(interval=timedelta(minutes=self.tickrate))
        def post_topic():
            topic = self.generator.generate()
            author, cookie = self.getCookie()
            self.client.updateCookies(cookie)
            if self.client.createTopic("http://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm", 
                                       topic['title'],
                                       topic['message']):
                print(f'Posted topic at {time.ctime()} as {author}')
                self.topic_count += 1
            else:
                print(f'Failed to post topic as {author}')
        self.tl.job(interval=timedelta(hours=1))(self.log)
        self.tl.start()
        post_topic()
        while True:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                self.tl.stop()
                break