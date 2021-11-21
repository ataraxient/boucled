import sys
import argparse

import bot
import generators as gen

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    path_parser = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument("delay", help="Délai entre les topics postés")

    path_parser.add_argument("--csv", help="Chemin vers un fichier .csv")
    path_parser.add_argument("--txt", help="Chemin vers un dossier contenant des .txt")

    args = parser.parse_args()
    
    if args.csv:
        b = bot.BotJVC(gen.FromCSV(args.csv), tickrate=int(args.delay))
        b.run()
    elif args.txt:
        b = bot.BotJVC(gen.FromTXT(args.txt), tickrate=int(args.delay))
        b.run()
