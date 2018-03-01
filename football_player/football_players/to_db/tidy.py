# _*_ coding:utf-8 _*_
import pymysql


def tidy_db():
    # 整理数据库--------------------------------------------------------------------------------------------
    to_db = pymysql.connect(host='localhost', user='root', password='2000', db='football_players', port=3306,
                            charset='utf8')
    cur = to_db.cursor()

    # 更改'"", "-"' 为 null
    columns = ('名称', '号码', '位置', '进球', '助攻', '进点球', '进球间隔时间', '总丢球数', '未丢球场次', '乌龙球',
               '出场次数', '场均积分', '替补下场', '替补上场', '黄牌', '红牌', '黄变红', '出场总时间', '赛季',
               '身高', '体重', '年龄', '英文名', '惯用脚', '球队', '联赛', '国家队', '国籍',
               )
    for column in columns:
        s1 = 'update player set {}=null where {} in ("","-")'.format(column, column)
        cur.execute(s1)
        to_db.commit()

    #  有些队员的数据国家队的名字是其它俱乐部的名字, 在这里更改为null
    s2 = 'select 球队 from player'
    cur.execute(s2)
    res1 = cur.fetchall()
    club = tuple([i[0] for i in res1])
    to_db.commit()
    s3 = 'update player set 国家队=null where 国家队 in {}'.format(str(club))
    cur.execute(s3)
    to_db.commit()

    # 年龄和号码是0的改为null
    for c in ['年龄', '号码']:
        s4 = 'update player set {}=null where {}=0'.format(c, c)
        cur.execute(s4)
        to_db.commit()

    # 更改数据类型
    numchar = ['号码', '进球', '助攻', '进点球', '进球间隔时间', '总丢球数', '未丢球场次', '乌龙球', '出场次数',
               '替补下场', '替补上场', '黄牌', '红牌', '黄变红', '出场总时间', '身高', '体重', '年龄']
    for char in numchar:
        s5 = 'alter table player change {} {} smallint'.format(char, char)
        cur.execute(s5)
        to_db.commit()
    s6 = 'alter table player change 场均积分 场均积分 decimal(5,2)'
    cur.execute(s6)
    to_db.commit()

    cur.close()
    to_db.close()


if __name__ == '__main__':
    tidy_db()
