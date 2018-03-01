# _*_ coding:utf-8 _*_
import json
import re
import scrapy
from scrapy.http import Request
from football_players.items import PlayersItem


class PremierLeague(scrapy.Spider):
    name = 'football_players'
    league_url = 'https://dc.qiumibao.com/shuju/public/index.php?_url=/data/index&league={}&tab=积分榜&year=[year]'
    team_url = 'https://db.qiumibao.com/f/index/team?name={}'
    player_url = 'https://db.qiumibao.com/f/index/player?pid={}'

    def start_requests(self):
        for league_name in ['西甲', '意甲', '法甲', '德甲', '英超']:
            url = PremierLeague.league_url.format(league_name)  # 联赛
            yield Request(url, callback=self.parse, meta={'league': league_name})

    def parse(self, response):
        text = response.text
        j_l = json.loads(text)
        teams = [t['球队'] for t in j_l['data']]
        for team_name in teams:
            url = PremierLeague.team_url.format(team_name)  # 球队
            yield Request(url, callback=self.team,
                          meta={'league': response.meta['league']}
                          )

    def team(self, response):
        text = response.text
        j_l = json.loads(text)
        _ids = [i['id'] for i in j_l['players'] if i['name']]
        for _id in _ids:
            url = PremierLeague.player_url.format(_id)  # 球员
            yield Request(url, callback=self.player,
                          meta={'league': response.meta['league']}
                          )

    def player(self, response):
        text = response.text
        league = response.meta['league']
        j_t = re.search('{"id.+}', text, re.S).group()
        j_l = json.loads(j_t)
        item = PlayersItem()
        item['players'] = (league, j_l)
        return item
