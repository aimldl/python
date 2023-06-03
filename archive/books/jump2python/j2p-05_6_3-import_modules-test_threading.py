# -*- coding: utf-8 -*-
"""
j2p-05_6_2-import_modules-test_threading.py
스레드를 다루는 threading 모듈
# 프로세스 (Process)
#   = 컴퓨터에서 동작하고 있는 프로그램
#   1개의 프로세스는 1가지 일만 할 수 있다.
#   스레드를 이용하면 한 프로세스 내에서 2가지 이상의 일을 동시에 수행할 수 있다.
"""

import threading
import time

def say( msg ):
    while True:
        time.sleep(1)
        print( msg )

for msg in ['you', 'need', 'python']:
    t = threading.Thread( target=say,args=(msg,))
    t.daemon = True
    t.start()

for i in range(100):
    time.sleep(0.1)
    print(i)

#%% 아래의 출력결과값에서 볼 수 있듯이,
#   스레드는 메인 프로그램과 별도로 실행되는 것을 알 수 있다.
# 이러한 스레드 프로그래밍을 가능하게 해주는 것이 threading.Thread클래스이다.
# 이 클래스의 첫 번째 인수는 함수명을,
#            두 번째 인수는 이 함수의 입력변수를 받는다.
# 다음과 같이 스레드를 크래스로 정의해도 동일한 결과를 얻는다.

import threading
import time

class MyThread( threading.Thread):
    # 스레드를 클래스로 정의할 경우에는 __init__메서드에서
    # threading.Thread.__init__(self)와 같이 부모 클래스의 생성자를 반드시 호출해야 한다.
    def __init__(self, msg):
        threading.Thread.__init__(self)
        self.msg = msg
        self.daemon = True
        
    # MyThread로 생성된 객체의 start 메서드를 실행할 때는 
    #   MyThread클래스의 run 메서드가 자동으로 수행된다.
    def run(self):
        while True:
            time.sleep(1)
            print(self.msg)

for msg in['you','need','python']:
    t = MyThread(msg)
    t.start()
    
for i in range(100):
    time.sleep(0.1)
    print(i)

#%%
#0
#1
#2
#3
#4
#5
#6
#7
#8
#need
#python
#you
#9
#10
#11
#12
#13
#14
#15
#16
#17
#18
#need
#python
#you
#19
#20
#21
#22
#23
#24
#25
#26
#27
#28
#need
#python
#you
#29
#30
#31
#32
#33
#34
#35
#36
#37
#38
#need
#python
#you
#39
#40
#41
#42