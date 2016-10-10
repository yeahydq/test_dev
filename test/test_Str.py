#coding:utf-8
#!/usr/bin/env python
__author__ = 'dick'
import random

print 'name:%s; sex:%s' % ('tom', 'male')


'''
ip，端口，类型(0高匿名，1透明)，protocol(0 http,1 https),country(国家),area(省市),updatetime(更新时间)
 speed(连接速度)
'''
parserList = [
        {
            'urls': ['http://www.66ip.cn/%s.html'% n for n in ['index']+range(2,12)],
            'type':'xpath',
            'pattern': ".//*[@id='main']/div/div[1]/table/tr[position()>1]",'http:%s' %
            'postion':{'ip':'./td[1]','port':'./td[2]','type':'./td[4]','protocol':''}
        }]
print parserList


url=u'//mm.taobao.com/45834230.htm'
url="u'//mm.taobao.com/45834230.htm'"
fullUrl='http:%s' % url.replace("u'",'').replace("'",'')
print fullUrl
