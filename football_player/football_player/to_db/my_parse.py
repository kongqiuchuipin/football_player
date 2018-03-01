# _*_ coding:utf-8 _*_


def my_parse(item_play):
    league = item_play[0]
    j_l = item_play[1]
    player = {
        '名称': j_l['name'], '身高': j_l['height'], '体重': j_l['weight'], '年龄': j_l['age'],
        '英文名': j_l['name_en'], '球队': j_l['team_name'], '号码': j_l['number'], '位置': j_l['position'],
        '国籍': j_l['nationality'], '国家队': j_l['national_team'], '惯用脚': j_l['habit_foot'],
        '进球': 0, '助攻': 0, '红牌': 0,
        '出场次数': 0, '黄牌': 0, '联赛': league,
        '场均积分': 0.0, '替补下场': 0, '替补上场': 0,
        '黄变红': 0, '进球间隔时间': 0.0, '赛季': '',
        '出场总时间': '-', '进点球': '-', '乌龙球': 0,
        '总丢球数': '-', '未丢球场次': '-'
    }
    if j_l['season_performace']:
        lists = j_l['season_performace']['league_list']
        for i in lists:
            if i['赛事'] == league and i['赛季'] == '17/18':
                league_list = i
                if j_l['position'] == '守门员':
                    league_list['进点球'] = '-'
                    league_list['进球间隔时间'] = '-'
                else:
                    league_list['总丢球数'] = '-'
                    league_list['未丢球场次'] = '-'
                player = {
                    '名称': j_l['name'], '身高': j_l['height'], '体重': j_l['weight'], '年龄': j_l['age'],
                    '英文名': j_l['name_en'], '球队': j_l['team_name'], '号码': j_l['number'], '位置': j_l['position'],
                    '国籍': j_l['nationality'], '国家队': j_l['national_team'], '惯用脚': j_l['habit_foot'],
                    '进球': league_list['进球'], '助攻': league_list['助攻'], '红牌': league_list['红牌'],
                    '出场次数': league_list['出场次数'], '黄牌': league_list['黄牌'], '联赛': league_list['赛事'],
                    '场均积分': league_list['场均积分'], '替补下场': league_list['替补下场'], '替补上场': league_list['替补上场'],
                    '黄变红': league_list['黄变红'], '进球间隔时间': league_list['进球间隔时间'], '赛季': league_list['赛季'],
                    '出场总时间': league_list['出场总时间'], '进点球': league_list['进点球'], '乌龙球': league_list['乌龙球'],
                    '总丢球数': league_list['总丢球数'], '未丢球场次': league_list['未丢球场次']
                }
    return player
