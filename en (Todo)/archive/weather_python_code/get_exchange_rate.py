##!/bin/python
"""
fetch_exchange_rate.py
  crawls exchange rates from Naver Finance at "http://finance.naver.com/marketindex/".
  
* Rev.1: 2020-03-01 (Sun)
* Draft: 2020-02-28 (Fri)
"""

def get_url_from_command_line_arguments():
    # Use the default URL or get an URL from command line argument
    import sys

    argc = len( sys.argv )
    argv = sys.argv
    if argc <= 1:
        url = "http://finance.naver.com/marketindex/"
    else:
        url = argv[1]
    return url

def download_response_from( url ):
    import urllib.request as request
    from bs4 import BeautifulSoup
    
    print(f'Downloading the response from {url} ...' )
    response = request.urlopen( url )
    html = BeautifulSoup( response, "html.parser" )
    
    return html

def fetch_exchange_rates_from( url, debug=False ):
    
    html = download_response_from( url )
    
    price = html.select_one( "div.head_info > span.value" ).string
    if debug:
        print(f"USD/KRW={price}" )
    
    return price

def get_today( debug=False ):
    '''
    returns a string like 2020-03-01-sun
    
    date.weekday()¶
      Return the day of the week as an integer, where Monday is 0 and Sunday is 6. For example, date(2002, 12, 4).weekday() == 2, a Wednesday. See also isoweekday().
    Refer to "datetime — Basic date and time types" at https://docs.python.org/3/library/datetime.html
    '''
    from datetime import date
    
    day = ['mon','tue','wed','thu','fri','sat','sun']  # the day of the week
    today = date.today().strftime('%Y-%m-%d') + '-' + day[ date.today().weekday() ]
    
    if debug:
        print( day[ date.today().weekday() ]  )  # date.today().weekday() = 6, day[6] = sun
        print( today )
    
    return today

#def add_today_as_suffix( file_name ):
def save( price ):
    
    file_name = 'dcs-exchange_rates-crawling_naver-' + get_today() + '.txt'
    
    print(f'Saving to {file_name} ...' )
    with open( file_name, 'w', encoding='utf-8') as file:
        file.write( price )

if __name__ == "__main__":
     
    url = get_url_from_command_line_arguments()
    #price = fetch_exchange_rates_from( url, debug=True )
    price = fetch_exchange_rates_from( url )
    save( price )