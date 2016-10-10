#coding:utf-8
#!/usr/bin/env python
__author__ = 'dick'

import requests

post_data = {'first':'true','kd':'Android','pn':'1'}


# return_data=requests.post("http://www.lagou.com/jobs/position",data=post_data)
# return_data=requests.post("https://mm.taobao.com/json/request_top_list.htm?page=1",data=post_data)
return_data=requests.post("https://mm.taobao.com/self/model_album.htm?user_id=687471686",data=post_data)
return_data=requests.post("https://mm.taobao.com/self/album_photo.htm?user_id=405095521&album_id=10000557042&album_flag=0tm?user_id=405095521&album_id=10000557042&album_flag=0",data=post_data)
print return_data.text
