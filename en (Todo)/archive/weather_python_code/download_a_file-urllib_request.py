# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:09:05 2020

@author: aimldl
"""

import urllib.request

'''
Caution: Use a link obtained by "right-click > Copy Image Location".
The same image file at https://github.com/aimldl/book/blob/master/images/image.png
is downloaded, but it doesn't display with an image viewer program.
'''

url = "https://raw.githubusercontent.com/aimldl/book/master/images/image.png"

# 1. urlretreive함수로 직접 파일을 다운로드 가능
file_name = "image.png"
urllib.request.urlretrieve( url, file_name )
print(f'{file_name} is saved.' )

# 2. urlopen로는 데이터가 메모리에 올라가므로, 별도로 파일에 저장해야 함.
file_name = "image2.png"
memory = urllib.request.urlopen( url ).read()

with open( file_name, mode="wb" ) as f:
    f.write( memory )
    print(f'{file_name} is saved.' )
    
# 3. API에서 text 다운로드 받기 
# XML/HTML등 텍스트 기반 데이터를 다운로드하는 예

url = "http://api.aoikujira.com/ip/ini"  # http or ftp
response = urllib.request.urlopen( url )
data = response.read()

text = data.decode( "utf-8" )
print( text )
'''
[ip]
API_URI=http://api.aoikujira.com/ip/get.php
REMOTE_ADDR=112.169.219.12
REMOTE_HOST=112.169.219.12
REMOTE_PORT=34438
HTTP_HOST=api.aoikujira.com
HTTP_USER_AGENT=Python-urllib/3.7
HTTP_ACCEPT_LANGUAGE=
HTTP_ACCEPT_CHARSET=
SERVER_PORT=80
FORMAT=ini
'''
