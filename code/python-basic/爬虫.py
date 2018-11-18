import numpy as np
import pandas as pd
import urllib
from urllib import request, parse
from datetime import date, timedelta, datetime
import re
import json
import time
from datayes.advisor.main.index_return import get_weekend, get_weekday

################ urllib ################
## request : 发送一个get请求到指定的页面，然后返回http的响应

# urlopen
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

print('Data:', data.decode('utf-8'))

# 通过往Request对象添加HTTP头，把请求伪装成浏览器，可以模拟浏览器发送GET请求

req = request.Request('http://www.douban.com/')  # 参数 data：可以传入用户名/密码
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 \
               (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

#  动态网页，以post发送请求，参数data以bytes形式传入

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer',
               'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass


def get_content(url):
    '''
    模仿浏览器，提交请求，获取http响应
    '''
    opener = request.build_opener()
    # 标识浏览器
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36')]
    # cookie
    opener.addheaders.append(('Cookie',
                              'cookie_locale=zh; UM_distinctid=15ba3242e791001-0ea5b4e3364b28-4e47052e-232800-15ba3242e7aaff; WtbB_2132_saltkey=INutSKKa; WtbB_2132_lastvisit=1494571257; WtbB_2132_ulastactivity=4216TyHziXRs0dIjw08lGH6z2H40m%2FqPGkdmdAvNJLtmZXQxb74V; WtbB_2132_nofavfid=1; __utma=75570051.169882094.1491626208.1494574858.1494574858.1; __utmz=75570051.1494574858.1.1.utmcsr=apidoc.datayes.com|utmccn=(referral)|utmcmd=referral|utmcct=/app/overview; cloud-sso-token=5A63AFA2791C25117EEDC8D804E9E49C; CNZZDATA1000377076=757399342-1495001413-https%253A%252F%252Fapp.wmcloud.com%252F%7C1495761965; _gat=1; _ga=GA1.2.169882094.1491626208; _gid=GA1.2.437948554.1495787959'))
    f = opener.open(url)
    content = f.read()
    return content.decode('utf-8')


url = ''
content = get_content(url)

################ urllib2 ################


################ scrapy ################


################ beautiful soup ################
