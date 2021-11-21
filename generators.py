import pandas as pd
import random
import glob
from abc import ABCMeta, abstractmethod
from numpy.random import permutation

class TopicGenerator(metaclass=ABCMeta):
    '''
    Trait for what a Topic Generator should be. We only requires a function which returns a topic
    which should be a dict with a title and the message {'title': ,'message':}
    '''
    @abstractmethod
    def generate(self):
        pass

class LoopChooser():
    '''
    Loop through every single topic before starting again
    '''
    def __init__(self,n):
        self.n = n
        self.__newGenerator__()
    
    def __newGenerator__(self):
        newPerm = permutation(self.n)
        self.gen = (k for k in newPerm)
    
    def next(self):
        try:
            return next(self.gen)
        except StopIteration:
            self.__newGenerator__()
            return next(self.gen)

class FromCSV(TopicGenerator):
    '''
    Generate topic by picking a random topic from a .csv file
    The .csv file should have to columns : title and content
    '''
    def __init__(self, topic_db_path):
        self.df = pd.read_csv(topic_db_path)
        self.n = self.df.shape[0]
        self.chooser = LoopChooser(self.n)

    def generate(self):
        k = self.chooser.next()
        return {'title': self.df['title'][k], 'message': self.df['content'][k]}
        
class FromTXT(TopicGenerator):
    '''
    Generate topic by picking a random topic from a folder containing
    .txt files, .txt files must have the same format : the title on the
    first line, the content of the topic after
    '''
    def __init__(self, topic_folder_path):
        self.path = topic_folder_path
        self.topics = glob.glob("./" + topic_folder_path + "*.txt")
        self.chooser = LoopChooser(len(self.topics))

    def generate(self):
        topic = self.topics[self.chooser.next()]
        with open(topic,'r') as f:
            data = f.read()
            title = data.split('\n', 1)[0]
            message = data.split('\n', 1)[1]
        return {'title':title,'message':message}