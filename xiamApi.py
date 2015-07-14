#!usr/evn/python
# -*- coding:utf-8 -*-
import re,urllib,urllib2,json,cookielib
from bs4 import BeautifulSoup

def xiamiLogin(usermail = "",password = ""):
    usermail,password = "harry159821@126.com","*GPH211314"
    # usermail,password = "984405219@qq.com","*GPH211314"
    cookiejar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    opener.addheaders = [
            ('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'),
            ("Referer","http://www.xiami.com/"),
            ]
    urllib2.install_opener(opener)

    Login_data = {
        "email":usermail,
        "password":password,
        "remember":"1",
        "LoginButton":"登录",
    }
    Login_url = 'https://login.xiami.com/web/login'
    Login_request = urllib2.Request(Login_url,data=urllib.urlencode(Login_data))
    Login_response = urllib2.urlopen(Login_request).read()
    # print Login_response

    if 'id="validate"' in Login_response:
        print u"需要输入验证码"
        bs = BeautifulSoup(Login_response)
        Captcha_url = bs.select("form p img")[0]['src']
        Captcha_request = urllib2.Request(Captcha_url)
        Captcha_response = urllib2.urlopen(Captcha_request).read()
        with open('Captcha.png', 'wb') as f:
            f.write(Captcha_response)
        validate = raw_input('captcha > ')
        Login_data = {
            "email":usermail,
            "password":password,
            "remember":"1",
            "LoginButton":"登录",
            "validate":validate,
        }
        Login_url = 'https://login.xiami.com/web/login'
        Login_request = urllib2.Request(Login_url,data=urllib.urlencode(Login_data))
        Login_response = urllib2.urlopen(Login_request).read()

    indexResponse = urllib2.urlopen(urllib2.Request('http://www.xiami.com/')).read()

    # http://www.xiami.com/index/home　用户信息
    userInfoRes = urllib2.urlopen(urllib2.Request('http://www.xiami.com/index/home')).read()
    userInfoJson = json.loads(userInfoRes)
    if userInfoJson["data"]['userInfo']:
        print userInfoJson["data"]['userInfo']['user_id']
        print userInfoJson["data"]['userInfo']['nick_name']
        print userInfoJson["data"]['userInfo']['avatar']
        print userInfoJson["data"]['userInfo']['level']
        print userInfoJson["data"]['userInfo']['credits']
        print userInfoJson["data"]['userInfo']['numlevel']
        print userInfoJson["data"]['userInfo']['sign']['persist_num']
    else:
        print u'未登录'

    # www.xiami.com/index/recommend 今日推荐歌单
    # http://www.xiami.com/song/playlist/id/1/type/9/cat/json?_ksTS=1436773987047_429
    recommendRes = urllib2.urlopen(urllib2.Request('http://www.xiami.com/song/playlist/id/1/type/9/cat/json')).read()
    recommendJson = json.loads(recommendRes)
    print recommendJson['data']['trackList'][0]['title']
    # print recommendJson['data']['trackList'][0]['song_id']
    # print recommendJson['data']['trackList'][0]['album_id']
    print recommendJson['data']['trackList'][0]['album_name']
    # print recommendJson['data']['trackList'][0]['object_id']
    # print recommendJson['data']['trackList'][0]['object_name']
    # print recommendJson['data']['trackList'][0]['insert_type']
    print recommendJson['data']['trackList'][0]['background']
    # print recommendJson['data']['trackList'][0]['grade']
    print recommendJson['data']['trackList'][0]['artist']
    # print recommendJson['data']['trackList'][0]['aritst_type']
    print recommendJson['data']['trackList'][0]['artist_url']
    # print recommendJson['data']['trackList'][0]['location']
    # print recommendJson['data']['trackList'][0]['ms']
    # print recommendJson['data']['trackList'][0]['lyric']
    print recommendJson['data']['trackList'][0]['lyric_url']
    print recommendJson['data']['trackList'][0]['pic']
    print recommendJson['data']['trackList'][0]['album_pic']
    print recommendJson['data']['trackList'][0]['length']       # 歌曲长度 秒
    # print recommendJson['data']['trackList'][0]['tryhq']
    # print recommendJson['data']['trackList'][0]['artist_id']

    print location_dec(recommendJson['data']['trackList'][0]['location'])

    # http://www.xiami.com/index/feed
    # http://www.xiami.com/index/collect 精选集推荐
    # http://www.xiami.com/index/indexright
    # http://www.xiami.com/index/subscribe 订阅

    # 签到
    checkin_url = 'http://www.xiami.com/task/signin'
    checkin_headers = {
        'Accept':'*/*',
        'Accept-Language':'zh-CN,zh;q=0.8,ja;q=0.6,en-US;q=0.4,en;q=0.2',
        'DNT':'1',
        'Host':'www.xiami.com',
        'Origin':'http://www.xiami.com',
        'Referer':'http://www.xiami.com/',
        'User-Agent':'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        }
    checkin_request = urllib2.Request(checkin_url,headers=checkin_headers)
    checkin_response = urllib2.urlopen(checkin_request)
    checkin_response = checkin_response.read()
    print checkin_response

def requests(url,timeouts=5):
    header = {
            'Referer': 'http://www.xiami.com/',
            'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
            }   
    request = urllib2.Request(url,headers=header)
    response = urllib2.urlopen(request,timeout=timeouts)
    html = response.read()
    if html:    
        return html
    return False

def location_dec(str):
    head = int(str[0])
    str = str[1:]
    rows = head
    cols = int(len(str)/rows) + 1

    out = ""
    full_row = len(str) % head
    for c in range(cols):
        for r in range(rows):
            if c == (cols - 1) and r >= full_row:
                continue
            if r < full_row:
                char = str[r*cols+c]
            else:
                char = str[cols*full_row+(r-full_row)*(cols-1)+c]
            out += char
    return urllib.unquote(out).replace("^", "0")

def getDetail(id):
    url = 'http://songs.sinaapp.com/apiv3.php?type=1&id='+id
    html = requests(url)
    html = html.replace('\/','/')
    html = json.loads(html)
    #print html['location']
    #print html['pic']
    #print html['lyric']
    return html

def getUrl(id):
    url = 'http://www.xiami.com/song/playlist/id/'+id+'/object_name/default/object_id/0'
    html = requests(url)
    url = ''
    try:
        bs = BeautifulSoup(html)
        bs = BeautifulSoup(str(bs))
        url = location_dec(bs.select('location')[0].text)
    except Exception, e:
        print e
    return url

def getRealUrl(songID):
    detail = getDetail(songID)
    if detail:
        songUrl = detail['location']
    else:
        songUrl = getUrl(songID)
    return songUrl

if __name__ == '__main__':
    xiamiLogin()

'''
# ---------------------------------------------
def printCookie():
    cookie=''
    cookieDict = {}
    for c in cookiejar:
        cookie += c.name + '=' + c.value + ';'
        cookieDict[c.name] = c.value
# ---------------------------------------------
'''
