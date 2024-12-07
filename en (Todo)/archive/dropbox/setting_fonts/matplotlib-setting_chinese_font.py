#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
matplotlib-setting_chinese_font.py

"""

#import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import numpy as np

true_type_font_list = [ font.name for font in fm.fontManager.ttflist ]
num_ttf = len(true_type_font_list)  # number of true type font
print(f'There are {num_ttf} true type fonts' )  # 311
print( true_type_font_list )

# Chinese fonts
# Get the paths to fonts
jp_font_list = [ (font.name, font.fname) for font in fm.fontManager.ttflist if 'AR PL' in font.name ]
for name, path in jp_font_list:
    print(f'{name}, {path}')

path2font = '/usr/share/fonts/truetype/arphic/ukai.ttc'
fontprop  = fm.FontProperties( fname=path2font, size=12 )

# Generate a random data
data = np.random.randint(-100, 100, 50).cumsum()

# Example with corrupted Korean characters.
plt.plot( range(50), data, 'r' )

plt.title('股价', fontproperties=fontprop )
plt.ylabel('株式', fontproperties=fontprop )
plt.xlabel('時間(分)', fontproperties=fontprop )
plt.text( 0.5,0,'分', fontproperties=fontprop  )

