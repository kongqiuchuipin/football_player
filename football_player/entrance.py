# _*_ coding:utf-8 _*_
import os
from football_players.to_db import tidy
if __name__ == '__main__':
    os.system('scrapy crawl football_players')
    tidy.tidy_db()