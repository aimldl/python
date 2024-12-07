# -*- coding: utf-8 -*-
"""
j2p-05_6-import_modules.py
p.251, 05-6. 외장 함수

The Python Standard Library¶
  https://docs.python.org/3/library/index.html

Copy & Paste the commands in this script.
이 스크립트의 명령어는 복사해서 Python prompt >>> 에 붙이기로 실행.
  
"""

#%% sys
#  sys 모듈로 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있다.

# sys.argv 명령 행에서 인수 전달하기
# argv_test.py
import sys
print( sys.argv )

# 윈도우즈
#   > python test.py abc pey guido
# 리눅스
#   $ python test.py abc pey guido
#
# 파이썬 명령어를 위와 같이 실행하면 
#   입력인수 (test.py abc pey guido)가 sys.argv라는 리스트에 저장된다.
#   ['test.py', 'abc', 'pey', 'guido']

# sys.exit 강제로 스크립트 종료하기
# >>> sys.exit()
# 를 실행하면 Ctrl + Z, Ctrl+D를 눌러서 대화형 이넡프리터를 종료하는 것과 같다.

# sys.path 자신이 만든 모듈 불러와 사용하기
# sys.path는 파이썬 모듈이 저장된 위치를 나타낸다.
# 이 경로에 있는 파이썬 모듈들은 어디에서나 불러올 수 있다.

# Windows 10의 Ubuntu Linux
#   aimldl@DESKTOP-HPVQJ6N:/mnt/c/Users/aimldl/Desktop$ python3
#   Python 3.6.7 (default, Oct 22 2018, 11:32:17)
#   [GCC 8.2.0] on linux
#   Type "help", "copyright", "credits" or "license" for more information.
#   >>> import sys
#   >>> sys.path
#   ['', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']
#   >>>

# '' = 현재 디렉터리

# Windows 10의 Anaconda Prompt
#   (base) C:\Users\aimldl>python
#   Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
#   Type "help", "copyright", "credits" or "license" for more information.
#   >>> import sys
#   >>> sys.path
#   ['', 'C:\\Users\\aimldl\\Anaconda3\\python37.zip', 'C:\\Users\\aimldl\\Anaconda3\\DLLs', 'C:\\Users\\aimldl\\Anaconda3\\lib', 'C:\\Users\\aimldl\\Anaconda3', 'C:\\Users\\aimldl\\Anaconda3\\lib\\site-packages', 'C:\\Users\\aimldl\\Anaconda3\\lib\\site-packages\\win32', 'C:\\Users\\aimldl\\Anaconda3\\lib\\site-packages\\win32\\lib', 'C:\\Users\\aimldl\\Anaconda3\\lib\\site-packages\\Pythonwin']
#   >>>

# path_append.py
import sys
sys.path.append('C:\\Python\\Mymodules')

#%% pickle
#  pickle모듈로 객체의 형태를 그대로 유지하면서, 파일에 저장하고 불러올 수 있다.

# write2pickle.py
import pickle
f = open('test.txt','wb')
data = {1:'python', 2:'you need'}
pickle.dump( data,f )
f.close()

# read_thru_pickle.py
import pickle

f = open('test.txt','rb')
data = pickle.load( f )
print( data )
# {2:'you need', 1:'python'}

#%% OS
#   OS모듈로 환경변수, 디렉토리, 파일 등 OS자원을 제어할 수 있다.

####################################################
# os.environ 내 시스템의 환경 변수 값을 알고 싶을 때 #
####################################################
#   시스템은 제각기 다른 환경변수 값을 가지고 있다. 그 값을 확인할 수 있다.
import os
os.environ

# Windows 10의 Anaconda Prompt
#environ({'ALLUSERSPROFILE': 'C:\\ProgramData',
#         'APPDATA': 'C:\\Users\\aimldl\\AppData\\Roaming',
#         'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files',
#         'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
#         'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files',
#         'COMPUTERNAME': 'DESKTOP-HPVQJ6N',
#         'COMSPEC': 'C:\\Windows\\system32\\cmd.exe',
#         'CONDA_DEFAULT_ENV': 'base',
#         'CONDA_EXE': 'C:\\Users\\aimldl\\Anaconda3\\Scripts\\conda.exe',
#         'CONDA_PREFIX': 'C:\\Users\\aimldl\\Anaconda3',
#         'CONDA_PROMPT_MODIFIER': '(base) ',
#         'CONDA_PYTHON_EXE': 'C:\\Users\\aimldl\\Anaconda3\\python.exe',
#         'CONDA_SHLVL': '1',
#         'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData',
#         'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 
#         'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 
#         'HOMEDRIVE': 'C:', 
#         'HOMEPATH': '\\Users\\aimldl', 
#         'LOCALAPPDATA': 'C:\\Users\\aimldl\\AppData\\Local', 
#         'LOGONSERVER': '\\\\DESKTOP-HPVQJ6N', 
#         'NUMBER_OF_PROCESSORS': '8', 
#         'ONEDRIVE': 'C:\\Users\\aimldl\\OneDrive', 
#         'ONEDRIVECONSUMER': 'C:\\Users\\aimldl\\OneDrive', 
#         'OS': 'Windows_NT', 
#         'PATH': 'C:\\Users\\aimldl\\Anaconda3;
#                  C:\\Users\\aimldl\\Anaconda3\\Library\\mingw-w64\\bin;
#                  C:\\Users\\aimldl\\Anaconda3\\Library\\usr\\bin;
#                  C:\\Users\\aimldl\\Anaconda3\\Library\\bin;
#                  C:\\Users\\aimldl\\Anaconda3\\Scripts;
#                  C:\\Users\\aimldl\\Anaconda3\\bin;
#                  C:\\Users\\aimldl\\Anaconda3\\condabin;
#                  C:\\Windows\\system32;
#                  C:\\Windows;
#                  C:\\Windows\\System32\\Wbem;
#                  C:\\Windows\\System32\\WindowsPowerShell\\v1.0;
#                  C:\\Windows\\System32\\OpenSSH;
#                  C:\\Program Files\\dotnet;
#                  C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn;
#                  C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn;
#                  C:\\Users\\aimldl\\AppData\\Local\\Microsoft\\WindowsApps;.', 
#         'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 
#         'PROCESSOR_ARCHITECTURE': 'AMD64', 
#         'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 9, GenuineIntel', 
#         'PROCESSOR_LEVEL': '6', 
#         'PROCESSOR_REVISION': '9e09', 
#         'PROGRAMDATA': 'C:\\ProgramData', 
#         'PROGRAMFILES': 'C:\\Program Files', 
#         'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 
#         'PROGRAMW6432': 'C:\\Program Files', 
#         'PROMPT': '(base) $P$G', 
#         'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;
#                          C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules',
#         'PUBLIC': 'C:\\Users\\Public', 
#         'SESSIONNAME': 'Console', 
#         'SYSTEMDRIVE': 'C:', 
#         'SYSTEMROOT': 'C:\\Windows', 
#         'TEMP': 'C:\\Users\\aimldl\\AppData\\Local\\Temp', 
#         'TMP': 'C:\\Users\\aimldl\\AppData\\Local\\Temp', 
#         'USERDOMAIN': 'DESKTOP-HPVQJ6N', 
#         'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-HPVQJ6N', 
#         'USERNAME': 'aimldl', 
#         'USERPROFILE': 'C:\\Users\\aimldl', 
#         'WINDIR': 'C:\\Windows'})
#>>>

##################################
# os.chdir 디렉터리 위치 변경하기 #
##################################
os.chdir('C:\WINDOWS')

########################################
# os.getcwd 현재 디렉토리 위치 리턴 받기 #
########################################
os.getcwd()
# 'C:\\Users\\aimldl'

###################################
# os.system 시스템 명령어 호출하기 #
###################################
# 시스템 자체의 프로그램, 기타 명령어들을 파이썬에서 호출.

os.system('dir')
# C 드라이브의 볼륨에는 이름이 없습니다.
# 볼륨 일련 번호: E0EE-4D5E
#
# C:\Users\aimldl 디렉터리
#
#2019-07-13 토  오후 03:11    <DIR>          .
#2019-07-13 토  오후 03:11    <DIR>          ..
#2019-06-25 화  오후 10:09    <DIR>          .anaconda
#2019-07-12 금  오후 01:30    <DIR>          .android
#2019-07-12 금  오후 01:29    <DIR>          .AndroidStudio3.4
#2019-06-26 수  오전 12:08    <DIR>          .conda
#2019-06-25 화  오후 10:39                43 .condarc
#2019-06-25 화  오후 10:13    <DIR>          .continuum
#2019-07-12 금  오후 12:41    <DIR>          .dotnet
#2019-06-25 화  오후 10:11    <DIR>          .ipython
#2019-06-26 수  오전 12:49    <DIR>          .jupyter
#2019-06-25 화  오후 11:24    <DIR>          .keras
#2019-06-25 화  오후 10:11    <DIR>          .matplotlib
#2019-07-13 토  오후 04:37               380 .python_history
#2019-07-13 토  오전 12:21    <DIR>          .spyder-py3
#2019-07-12 금  오전 08:45    <DIR>          3D Objects
#2019-07-07 일  오후 11:50    <DIR>          Anaconda3
#2019-07-12 금  오전 08:45    <DIR>          Contacts
#2019-07-13 토  오후 02:38    <DIR>          Desktop
#2019-07-12 금  오후 01:05    <DIR>          Documents
#2019-07-12 금  오후 05:02    <DIR>          Downloads
#2019-07-07 일  오후 11:46    <DIR>          Dropbox
#2019-06-25 화  오전 01:20    <DIR>          Evernote
#2019-07-12 금  오전 08:45    <DIR>          Favorites
#2019-07-12 금  오후 02:38    <DIR>          iCloudDrive
#2019-07-12 금  오전 08:45    <DIR>          Links
#2019-07-12 금  오전 08:45    <DIR>          Music
#2019-07-12 금  오후 02:37    <DIR>          OneDrive
#2019-07-12 금  오전 08:45    <DIR>          Pictures
#2019-06-25 화  오후 10:35    <DIR>          projects
#2019-07-12 금  오전 08:45    <DIR>          Saved Games
#2019-07-12 금  오전 08:45    <DIR>          Searches
#2019-07-13 토  오후 03:11                40 test.txt
#2019-07-12 금  오전 08:45    <DIR>          Videos
#               3개 파일                 463 바이트
#              31개 디렉터리  2,907,742,322,688 바이트 남음
#0
#>>>

#############################################
# os.popen 실행한 시스템 명령어의 결과값 받기 #
#############################################
# 시스템 명령어의 실행결과값을 읽기모드 형태의 파일 객체로 리턴한다.
f = os.popen('dir')
print( f )
#<os._wrap_close object at 0x0000021D5142FE48>
print( type(f.read() ))
#<class 'str'>

# 읽어드린 파일 객체의 내용을 보기
print( f.read() )
# C 드라이브의 볼륨에는 이름이 없습니다.
# 볼륨 일련 번호: E0EE-4D5E
#
# C:\Users\aimldl 디렉터리
#
#2019-07-13 토  오후 03:11    <DIR>          .
#2019-07-13 토  오후 03:11    <DIR>          ..
#2019-06-25 화  오후 10:09    <DIR>          .anaconda
#2019-07-12 금  오후 01:30    <DIR>          .android
#2019-07-12 금  오후 01:29    <DIR>          .AndroidStudio3.4
#2019-06-26 수  오전 12:08    <DIR>          .conda
#2019-06-25 화  오후 10:39                43 .condarc
#2019-06-25 화  오후 10:13    <DIR>          .continuum
#2019-07-12 금  오후 12:41    <DIR>          .dotnet
#2019-06-25 화  오후 10:11    <DIR>          .ipython
#2019-06-26 수  오전 12:49    <DIR>          .jupyter
#2019-06-25 화  오후 11:24    <DIR>          .keras
#2019-06-25 화  오후 10:11    <DIR>          .matplotlib
#2019-07-13 토  오후 04:37               380 .python_history
#2019-07-13 토  오전 12:21    <DIR>          .spyder-py3
#2019-07-12 금  오전 08:45    <DIR>          3D Objects
#2019-07-07 일  오후 11:50    <DIR>          Anaconda3
#2019-07-12 금  오전 08:45    <DIR>          Contacts
#2019-07-13 토  오후 02:38    <DIR>          Desktop
#2019-07-12 금  오후 01:05    <DIR>          Documents
#2019-07-12 금  오후 05:02    <DIR>          Downloads
#2019-07-07 일  오후 11:46    <DIR>          Dropbox
#2019-06-25 화  오전 01:20    <DIR>          Evernote
#2019-07-12 금  오전 08:45    <DIR>          Favorites
#2019-07-12 금  오후 02:38    <DIR>          iCloudDrive
#2019-07-12 금  오전 08:45    <DIR>          Links
#2019-07-12 금  오전 08:45    <DIR>          Music
#2019-07-12 금  오후 02:37    <DIR>          OneDrive
#2019-07-12 금  오전 08:45    <DIR>          Pictures
#2019-06-25 화  오후 10:35    <DIR>          projects
#2019-07-12 금  오전 08:45    <DIR>          Saved Games
#2019-07-12 금  오전 08:45    <DIR>          Searches
#2019-07-13 토  오후 03:11                40 test.txt
#2019-07-12 금  오전 08:45    <DIR>          Videos
#               3개 파일                 463 바이트
#              31개 디렉터리  2,907,739,869,184 바이트 남음

#%% 기타 유용한 OS 관련 함수
os.mkdir( directory_name )  # 디렉토리 생성
os.rmdir( directory_name )  # 디렉토리 삭제. 단, 비어있어야 함.
os.unlink( file_name )      # rm, 파일을 지운다.
os.rename(src,dst)          # 파일명 변경

#%% shutil
#   shutil로 파일을 복사할 수 있다.
# shutil — High-level file operations
#   https://docs.python.org/3/library/shutil.html

######################################
# shutil.copy(src, dst) 파일 복사하기 #
######################################
import shutil
shutil.copy('src.txt','dst.txt')

# Q: Why not os.copy? or os.cpy(src,dst)

#%% glob
#   glob 특정 디렉토리에 있는 파일이름을 모두 알아야 할 때...
#     파일명의 전체 리스트를 만들거나,
#     *,? 등의 메타 문자를 써서 원하는 파일만 읽을 수도 있다.

# glob( pathname ) 디렉터리에 있는 파일들의 리스트 만들기

import glob
glob.glob('C:/Python/q*')
# []

# 다른 예
#   (왜냐하면 위의 예는 Win10의 Anaconda Prompt에서 동작하지 않았다.)
os.getcwd()
# 'C:\\Users\\aimldl'
os.system('dir')
# dir의 결과는 위쪽 os.system('dir')의 실행결과를 참고할 것.
glob.glob('D*')
# ['Desktop', 'Documents', 'Downloads', 'Dropbox']

#%% tempfile
#   tempfile은 파일을 임시로 만들어서 사용할 때 유용하다.

#####################
# tempfile.mktemp() #
#####################
# 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 리턴한다.
import tempfile
filename = tempfile.mktemp()
filename
#'C:\\Users\\aimldl\\AppData\\Local\\Temp\\tmpt7qbpmb7'

############################
# tempfile.TemporaryFile() #
############################
# 임시 저장 공간으로 사용될 파일 객체를 리턴
# 이 파일은 기본적으로 바이너리 쓰기 모드 (wb)를 갖는다.
# f.close()가 호출되면 이 파일 객체는 자동으로 사라진다.

import tempfile
f = tempfile.TemporaryFile()
f.close()

# Q: 솔직히 용도를 잘 모르겠음.

#%% time
#   time모듈은 시간과 관련된 유용한 함수가 많다.

##############
# time.sleep #
##############
# 책에는 마직막인데 제일 앞으로 당김.
# 주로 루프 안에서 일정 시간 간격을 두고 루프를 실행할 때 쓰인다.

# sleep1.py
import time
for i in range(10):
  print( i )
  time.sleep(1)  # 1 sec

#############
# time.time #
#############
# UTC (Universal Time Coordinate, 세계표준시)로 현재 시간을 실수 형태로 리턴한다.
# 기준: 1970년 1월 1일 0시 0분 0초
# 기준시간이후로 지난 시간을 초단위로 리턴함.

import time
time.time()
#1563005221.5239825

##################
# time.localtime #
##################
# 연도,월,일,시,분,초의 형태로 바꿔서 리턴한다.
#   time.time()에 의해 반환되는 실수값을 이용
import time

# Option 1
time.localtime()
# time.struct_time(tm_year=2019, tm_mon=7, tm_mday=13, tm_hour=17, tm_min=9, tm_sec=7, tm_wday=5, tm_yday=194, tm_isdst=0)

# Option 2
time.localtime( time.time() )

################
# time.asctime #
################
# time.localtime에서 반환된 튜플형태의 입력을...
# 날짜와 시간을 알아보기 쉬운 형태로 리턴한다.

import time

# Option 1
time.asctime()
# 'Sat Jul 13 17:11:22 2019'

# Option 2
local_time = time.localtime()
time.asctime( local_time )
# 'Sat Jul 13 17:11:22 2019'

# Option 3
time_time = time.time()
local_time = time.localtime( time_time )
time.asctime( local_time )
# 'Sat Jul 13 17:11:22 2019'

##############
# time.ctime #
##############
# Current Time
#   time.asctime()와 같은 포맷으로 시간을 리턴한다.
#   단, 현재 시간만 리턴한다는 것이 다르다.

import time
time.ctime()
# 'Sat Jul 13 17:13:27 2019'

#################
# time.strftime #
#################
# time.strftime( format_code, time.locatime() )
# format_code를 지정할 수 있다.
# 예
import time
time.strftime( '%x', time.localtime() )
#'07/13/19'

time.strftime( '%c', time.localtime() )
#'Sat Jul 13 17:16:54 2019'

#%% format code for time.strftime
# TODO: 관련 링크를 넣을 것.
# 책의 p.259에도 있음.

#%% calendar
#   calendar는 파이썬에서 달력을 볼 수 있게 한다.

#############################
# calendar.calendar( year ) #
#############################
# 입력한 연도의 전체 달력을 볼 수 있다.
import calendar
print( calendar.calendar(2019) )
#                                  2019
#
#      January                   February                   March
#Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#    1  2  3  4  5  6                   1  2  3                   1  2  3
# 7  8  9 10 11 12 13       4  5  6  7  8  9 10       4  5  6  7  8  9 10
#14 15 16 17 18 19 20      11 12 13 14 15 16 17      11 12 13 14 15 16 17
#21 22 23 24 25 26 27      18 19 20 21 22 23 24      18 19 20 21 22 23 24
#28 29 30 31               25 26 27 28               25 26 27 28 29 30 31
#
#       April                      May                       June
#Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
# 1  2  3  4  5  6  7             1  2  3  4  5                      1  2
# 8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
#15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
#22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
#29 30                     27 28 29 30 31            24 25 26 27 28 29 30
#
#        July                     August                  September
#Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
# 1  2  3  4  5  6  7                1  2  3  4                         1
# 8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
#15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
#22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
#29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
#                                                    30
#
#      October                   November                  December
#Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#    1  2  3  4  5  6                   1  2  3                         1
# 7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
#14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
#21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
#28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
#                                                    30 31
                                                    
##########################
# calendar.prcal( year ) #
##########################
# calendar.calendar( year )와 동일한 결과
# Q: 그러면 왜 만들어 놓았나?
import calendar
calendar.prcal( 2019 )

###################################
# calendar.prmonth( year, month ) #
###################################

calendar.prmonth( 2019,7 )
#     July 2019
#Mo Tu We Th Fr Sa Su
# 1  2  3  4  5  6  7
# 8  9 10 11 12 13 14
#15 16 17 18 19 20 21
#22 23 24 25 26 27 28
#29 30 31

########################################
# calendar.weekday( year, month, day ) #
########################################
# 요일정보,
#   0  월요일
#   1  화요일
#      [...]
#   5  토요일
#   6  일요일

calendar.weekday( 2019,7,13 )
# 5
# 토요일

# 07을 입력하면 에러
calendar.weekday( 2019,07,13 )
# SyntaxError: invalid token

#######################
# calendar.monthrange #
#######################
# monthrange는 입력한 년월에 대해
#   (1일의 요일, 몇일까지 있는지 )
#   를 튜플로 리턴한다.

calendar.monthrange( 2015, 12 )
# (1, 31)
# 2015년 12월의
# 1의 의미: 화요일, 1일은 1, 즉 화요일이다.
# 31의 의미: 12월은 31일까지이다.

# prmonth로 결과를 확인해보면...
calendar.prmonth(2015, 12)
#   December 2015
#Mo Tu We Th Fr Sa Su
#    1  2  3  4  5  6
# 7  8  9 10 11 12 13
#14 15 16 17 18 19 20
#21 22 23 24 25 26 27
#28 29 30 31

#다른 예
calendar.monthrange( 2019, 7 )
# (0, 31)
# 2019년 7월 1일은 월요일이고,
# 이 달은 31일까지 있다.

# 2019년 7월도 확인해보면...
calendar.prmonth(2019, 7)
#     July 2019
#Mo Tu We Th Fr Sa Su
# 1  2  3  4  5  6  7
# 8  9 10 11 12 13 14
#15 16 17 18 19 20 21
#22 23 24 25 26 27 28
#29 30 31

#%% random & randint
#   random으로 난수 (규칙이 없는 임의의 수)를 발생시킨다.
#   주의: 난수이므로 출력값은 매번 바뀐다.

import random
random.random()  # 0.0~1.0 사이의 실수
# 0.3234451917255078

random.randint(1,10)  # 1~10 사이의 정수
# 4

random.randint(1,55)  # 1~55 사이의 정수
# 43

# random모듈을 이용해서 재미있는 함수를 만들어본다.
#   리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음 그 값을 리턴한다.
#   pop을 하므로 요소는 하나씩 사라진다.

# 이 스크립트는 별도의 파일로 저장해서 실행해야 한다.
# $ python random_pop.py
# 출력값의 한 예는 다음과 같다. 
#5
#4
#2
#1
#3

#################
# random_pop.py #
#################
import random
def random_pop( data ):
    number = random.randint( 0, len(data)-1 )
    return data.pop( number )

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data: print( random_pop(data) )

# 위의 함수는 random.choice함수를 사용해서 아래처럼 조금 더 직관적으로 만들 수 있다.

##################
# random_pop2.py #
##################
def random_pop2( data ):
    number = random.choice( data )
    data.remove( number )
    return number

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data: print( random_pop2(data) )

##################
# random.shuffle #    
##################
# 리스트의 항목을 무작위로 섞을 때 쓸 수 있다.
import random
data = [1,2,3,4,5]
random.shuffle( data )
data
# [3, 2, 4, 1, 5]

#%% webbrowser
#   webbrowser로 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동실행 할 수 있다.

import webbrowser
webbrowser.open('http://www.google.com')

# open_new함수는 이미 웹브라우저가 실행된 상태이더라도
#   새로운 창으로 해당 주소가 열리도록 한다.
webbrowser.open_new('http://www.google.com')