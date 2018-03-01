# _*_ coding:utf-8 _*_

import pymysql
import time

columns = ('名称', '号码', '位置', '进球', '助攻', '进点球', '进球间隔时间', '总丢球数', '未丢球场次', '乌龙球',
           '出场次数', '场均积分', '替补下场', '替补上场', '黄牌', '红牌', '黄变红', '出场总时间', '赛季',
           '身高', '体重', '年龄', '英文名', '惯用脚', '球队', '联赛', '国家队', '国籍', '创建时间'
           )


def player_to_db(players):
    create_time = time.strftime('%Y-%m-%d %X')
    mydb = pymysql.connect(host='localhost', user='root', password='2000',
                         db='football_players', port=3306, charset='utf8'
                         )
    cursor = mydb.cursor()
    char = '{} char(50),' * len(columns[:-1])
    table_create = ('create table if not exists player (' + char + '{} datetime)').format(*columns)
    cursor.execute(table_create)
    mydb.commit()
    val = tuple(players[c] for c in columns[:-1]) + (create_time,)
    # print(val)
    formats = '"{}",' * len(val)
    values = formats[:-1].format(*val)
    sql_insert = 'insert into player values ({})'.format(values)
    # print(sql)
    cursor.execute(sql_insert)
    mydb.commit()
    cursor.close()
    mydb.close()
