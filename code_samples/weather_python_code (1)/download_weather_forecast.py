#!/usr/bin/env python3

"""
download_weather_forecast.py

$ chmod 766 download_weather_forecast.py
$ ./download_weather_forecast.py 108
"""

import sys

def get_weather_info( area_code, file_name='weather.html', save=True ):
    import urllib.request
    import urllib.parse

    area_code_dict = { "전국": 108,
                       "서울": 109,
                       "경기도": 109,
                       "강원도": 105,
                       "충청북도": 131,
                       "충청남도": 133,
                       "전라북도": 146,
                       "전라남도": 156,
                       "경상북도": 143,
                       "경상남도": 159,
                       "제주도": 184
                     }
    
    url2api = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
    #values = { 'stnId': area_code_dict["서울"] }
    values = { 'stnId': area_code }
    params = urllib.parse.urlencode( values )
    url = url2api + "?" + params
    
    # Download
    response = urllib.request.urlopen( url ).read()
    xml = response.decode('utf-8')
    
    if save:
        with open( file_name, mode="w" ) as f:
            f.write( xml )
            print(f'{file_name} is saved.' )
    
    return xml

if __name__ =="__main__":
    if len( sys.argv) <= 1:
        print( "Usage: ./download_weather_forecast.py <area_code> " )
        sys.exit()
    area_code = sys.argv[1]
    
    weather_info = get_weather_info( area_code )
    print( weather_info )