# _*_ coding:utf-8 _*_
import pymysql
import requests
import json
import time
import re
from football_players.to_db.db_mysql import player_to_db
from football_players.to_db.my_parse import my_parse

dt = time.strftime('%Y-%m-%d %X')
to_db = pymysql.connect(host='localhost', user='root', password='2000', db='football_players', port=3306,
                        charset='utf8')
cur = to_db.cursor()
# s = 'create table if not exists time({} char(100), {} datetime)'.format('数据', '时间')
# cur.execute(s)
# to_db.commit()
# print(dt)
# sql = 'insert into time values ("a","{}")'.format(dt)
# s1 = 'select 球队 from player'
# cur.execute(s1)
# res1 = cur.fetchall()
# print(len(res1))
# club = tuple([i[0] for i in res1])
# print(club)
# to_db.commit()
# s2 = 'update player set 国家队="" where 国家队 in {}'.format(str(club))
# cur.execute(s2)
# res2 = cur.fetchall()
# print(res2)
# s3 = 'alter table player change 场均积分 场均积分 decimal(5,2)'
# res = cur.execute(s3)
# s4 = 'update player set 位置=null where 位置=""'
# res = cur.execute(s4)
# columns = ('名称', '号码', '位置', '进球', '助攻', '进点球', '进球间隔时间', '总丢球数', '未丢球场次', '乌龙球',
#            '出场次数', '场均积分', '替补下场', '替补上场', '黄牌', '红牌', '黄变红', '出场总时间', '赛季',
#            '身高', '体重', '年龄', '英文名', '惯用脚', '球队', '联赛', '国家队', '国籍', '创建时间'
#            )
# for column in columns:
#     # s5 = 'alter table player change {} {} char(50)'.format(column, column)
#     s5 = 'update player set {}=null where {} in ("","-")'.format(column, column)
#     res = cur.execute(s5)
#     to_db.commit()
#     print(res)
s6 = 'update player set 号码=null where 号码=0'
res = cur.execute(s6)
# numchar = ['号码', '进球', '助攻', '进点球', '进球间隔时间', '总丢球数', '未丢球场次', '乌龙球', '出场次数',
#            '替补下场', '替补上场', '黄牌', '红牌', '黄变红', '出场总时间', '身高', '体重', '年龄']
# for char in numchar:
#     s5 = 'alter table player change {} {} smallint'.format(char, char)
#     res = cur.execute(s5)
#     print(res)
#     to_db.commit()
to_db.commit()
# print(res)
cur.close()
to_db.close()

# text = requests.get('https://db.qiumibao.com/f/index/player?pid=42925').text
# j_t = re.search('{"id.+}', text, re.S).group()
# j_l = json.loads(j_t)
# league = '德甲'
# item = (league, j_l)
# print(item)
# if __name__ == '__main__':
#     player = my_parse(item)
#     print(player)
#     player_to_db(player)
