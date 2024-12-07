# -*- coding: utf-8 -*-
"""
example-login2url.py

"""

import requests
from bs4 import BeautifulSoup

# 
url2login = "https://www.hanbit.co.kr/member/login.html"
user_id = "mrtonnet"
user_password = "Sk_xogud22"
login_info = { "m_id": user_id, "m_password": user_password }

# Log into the URL. If the log-in attempt fails, raise an exception
session = requests.session()
response = session.post( url2login, data=login_info )
response.raise_for_status()

print( "Log-in successful" )

# Access the mypage (마이한빛)
url2my_page = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
response = session.get( url2my_page )
response.raise_for_status()
html = response.text

# Fetch the values of mileage and ecoin
soup = BeautifulSoup( html, "html.parser" )

'''
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()

causes an error

    mileage = soup.select_one(".mileage_section1 span").get_text()
AttributeError: 'NoneType' object has no attribute 'get_text'

because soup.select_one(".mileage_section1 span") returns nothing or None!
'''
# Copy > Copy selector
mileage = soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section1 > dd > span")
#ecoin = soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section2 > dd > span").get_text()
print( "마일리지:"+mileage )
#print( "한빛이코인:"+mileage )