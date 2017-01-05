#-*- coding: utf-8 -*-
# 对抗12306多次查询后,会出现服务器繁忙问题

from auto_book import login_proc,search_proc,book_proc
import configparser

config=configparser.ConfigParser()
config.read('user.cfg')

result = 'gogogo'
username=config.get('user','username')
password=config.get('user','password')
begin_time = '15:35:00'
refresh_interval = 0.1
timer=False
type='G'

for i in range(1,5):
    if result == 'gogogo':
        try:
            sel = login_proc(username,password)
            search_proc(sel,type,timer)
            book_proc(sel,refresh_interval)
        except:
            continue
    else:
        print result
        break
