# _*_ coding:utf-8 _*_
"""
第一步get 旋风解析
第二步get aip.177537，获得post参数
第三步 post参数，获得包含视频地址的网址
第四步 get网址，得到视频链接
"""
import requests
import json
import re
import time
import sys
from urllib import request


def get_video_url(video_origin_url):
    xuanfeng_url = 'http://api.xfsub.com/index.php?url={}'.format(video_origin_url)
    api_url = 'https://api.177537.com'  # /?url=
    enterport_url = api_url + '/?url=' + video_origin_url
    post_url = 'https://api.177537.com/url.php'
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 ' \
            'Safari/537.36 '
    headers = {
        'User-Agent': agent,
        # 'Host': 'api.xfsub.com'
    }
    with requests.session() as session:
        session.headers.update(headers)
        session.get(xuanfeng_url, headers=headers, timeout=6)  # ----------------1
        time.sleep(0.15)
        session.headers['Host'] = 'api.177537.com'
        session.headers['Referer'] = 'http://api.xfsub.com/index.php?url={}'.format(video_origin_url)
        session.verify = False
        enterport_req = session.get(enterport_url)  # --------------2
        # print(enterport_req.text)/
        posts_text = re.search('"url\.php",(.+\"iqiyi\"),', enterport_req.text).group(1) + '}'
        # time.sleep(0.1)
        data = json.loads(posts_text)
        print(data)
        session.headers['Referer'] = 'https://api.177537.com/?url={}'.format(video_origin_url)

        post_req = session.post(url=post_url, data=data)  # -----------------3
        time.sleep(0.1)
        print(post_req.text)

        video_url = api_url + json.loads(post_req.text)['url']  # ---------------------4
        session.headers['X-Requested-With'] = 'ShockwaveFlash/28.0.0.137'
        # print(video_url)
        fourth_req = session.get(url=video_url, headers=headers)
        # print(session.headers)
        video_link = re.findall(r'\[CDATA\[(.+?)\]', fourth_req.text, re.S)
        # v  = session.get(url, verify=False)
        # print('aha',v.text)
        print(video_link)
        return video_link


def schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 1
    sys.stdout.write("  " + "%.2f%% 已经下载的大小:%ld 文件大小:%ld" % (per, a * b, c) + '\r')
    sys.stdout.flush()


def video_download(url1, filename):
    request.urlretrieve(url=url1, filename=filename, reporthook=schedule)


if __name__ == '__main__':
    # url= 'http://101.247.66.116/mp4files/7001000001290288/61.179.109.162/w/6d36d74366a94a0e5a1d3a560a532655.mp4'
    # url = 'http://221.194.64.110/0/a53eaf2ab79152420f2bbe78d42c5218.mp4?type=ppbox.launcher&key=' \
    # '24cb47f67a25c829770f837fa9177673'
    urls = get_video_url('http://www.iqiyi.com/v_19rrk3u9wg.html')
    for i, url in enumerate(urls):
        video_download(url, 'The Truman Show/{}.rmvb'.format(i))
