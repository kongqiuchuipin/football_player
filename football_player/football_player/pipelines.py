# -*- coding: utf-8 -*-
import pymysql
from football_players.items import PlayersItem
from football_players.to_db import db_mysql, my_parse


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FootballPlayersPipeline(object):
    def process_item(self, item, spider):
        player = my_parse.my_parse(item['players'])
        db_mysql.player_to_db(player)
