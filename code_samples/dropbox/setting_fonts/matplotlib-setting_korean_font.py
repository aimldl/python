#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
matplotlib-setting_korean_font.py
matplotlib 한글폰트 사용하기
http://corazzon.github.io/matplotlib_font_setting
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import os
import numpy as np

# Generate a random data
data = np.random.randint(-100, 100, 50).cumsum()

# Example with corrupted Korean characters.
plt.plot( range(50), data, 'r' )
mpl.rcParams['axes.unicode_minus'] = False

# Korean characters are corrupted.
plt.title('시간별 가격 추이')
plt.ylabel('주식 가격')
plt.xlabel('시간(분)')
plt.text( 0.5,0,'시간(분)' )

# Related information about matplotlib
print ('버전: ', mpl.__version__)
print ('설치 위치: ', mpl.__file__)
print ('설정 위치: ', mpl.get_configdir())
print ('캐시 위치: ', mpl.get_cachedir())
print ('설정파일 위치: ', mpl.matplotlib_fname())

'''
버전:  3.1.0
설치 위치:  /home/aimldl/anaconda3/envs/hula/lib/python3.7/site-packages/matplotlib/__init__.py
설정 위치:  /home/aimldl/.config/matplotlib
캐시 위치:  /home/aimldl/.cache/matplotlib
설정파일 위치:  /home/aimldl/anaconda3/envs/hula/lib/python3.7/site-packages/matplotlib/mpl-data/matplotlibrc
'''

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
num_font_list = len(font_list)
print( num_font_list ) # 319
'''
/home/aimldl/anaconda3/envs/hula/lib/python3.7/site-packages/matplotlib/backends/backend_agg.py:211: 
 RuntimeWarning: Glyph 49884 missing from current font. font.set_text(s, 0.0, flags=flags)
  ...
/home/aimldl/anaconda3/envs/hula/lib/python3.7/site-packages/matplotlib/backends/backend_agg.py:180: 
 RuntimeWarning: Glyph 51060 missing from current font. font.set_text(s, 0, flags=flags)
'''

'''
In a terminal,
444 fonts are installed on my Ubuntu Linux machine (version 18.04.02 LTS).
  $fc-list | wc -l
  444
Among them, 272 are truetype and 172 are X11-Type1.

* True type font
  $ fc-list | grep '/usr/share/fonts/truetype' | wc -l
  272
To list all of them, type in:
  $ fc-list | grep '/usr/share/fonts/truetype'

* X11 type1 font    
  $ fc-list | grep -v '/usr/share/fonts/truetype' | wc -l
  172    
To list all of them, type in:
  $ fc-list | grep -v '/usr/share/fonts/truetype'    
  /usr/share/fonts/X11/Type1/s050000l.pfb: Standard Symbols L:style=Regular
  /usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc: Noto Sans CJK JP,Noto Sans CJK JP Bold:style=Bold,Regular
    ...
  /usr/share/fonts/type1/gsfonts/n019003l.pfb: Nimbus Sans L:style=Regular
'''

'''
TODO: Get the standard output and save it to a variable font_list_ubuntu.

cmd = "fc-list | grep '/usr/share/fonts/truetype' | wc -l"
font_list_ubuntu = os.system( cmd )  # 272
#272
#0
font_list_ubuntu saves the returned status of os.system.
num_font_list_ubuntu = len(font_list_ubuntu)
print( num_font_list_ubuntu )

'''

true_type_font_list = [ font.name for font in fm.fontManager.ttflist ]
num_ttf = len(true_type_font_list)  # number of true type font
print(f'There are {num_ttf} true type fonts' )  # 311
print( true_type_font_list )
'''
['DejaVu Serif', 'STIXGeneral', 'STIXGeneral', 'DejaVu Sans', 'DejaVu Sans Mono', 
'STIXSizeOneSym', 'DejaVu Sans', 'STIXNonUnicode', 'DejaVu Sans', 'cmex10', 'cmsy10', 
'cmtt10', 'STIXGeneral', 'DejaVu Sans Mono', 'DejaVu Sans Mono', 'cmmi10', 'cmss10', 
'DejaVu Serif Display', 'STIXSizeFourSym', 'STIXSizeThreeSym', 'DejaVu Serif', 
'STIXNonUnicode', 'DejaVu Sans', 'cmb10', 'STIXSizeTwoSym', 'cmr10', 'STIXSizeThreeSym', 
'STIXNonUnicode', 'DejaVu Sans Mono', 'DejaVu Serif', 'STIXSizeOneSym', 'STIXNonUnicode', 
'STIXSizeFiveSym', 'DejaVu Serif', 'DejaVu Sans Display', 'STIXSizeTwoSym', 'STIXSizeFourSym', 
'STIXGeneral', 'Sawasdee', 'Georgia', 'Ubuntu', 'Arial', 'Mukti Narrow', 'Noto Mono', 
'Laksaman', 'Waree', 'Verdana', 'NanumBarunGothic', 'NanumGothic', 'Georgia', 
'Liberation Sans', 'KacstQurn', 'Karumbi', 'Liberation Mono', 'Tlwg Typewriter', 
'Tlwg Typewriter', 'Garuda', 'Georgia', 'KacstScreen', 'Umpush', 'Waree', 'Dyuthi', 
'Samyak Gujarati', 'Droid Sans Fallback', 'ori1Uni', 'Tlwg Typist', 'Padauk Book', 
'Manjari', 'Trebuchet MS', 'KacstBook', 'FreeMono', 'Courier New', 'Norasi', 'padmaa', 
'Keraleeyam', 'Tlwg Mono', 'Times New Roman', 'FreeMono', 'Liberation Mono', 'Courier New', 
'Verdana', 'Liberation Sans Narrow', 'Kinnari', 'Tlwg Mono', 'Liberation Serif', 'Garuda', 
'Tlwg Typo', 'KacstPoster', 'Liberation Mono', 'KacstLetter', 'Noto Sans CJK JP', 
'Liberation Serif', 'Kinnari', 'KacstArt', 'Arial', 'Andale Mono', 'KacstOne', 'Umpush', 
'Jamrul', 'Ubuntu Mono', 'Vemana2000', 'Courier New', 'Lohit Gurmukhi', 'Liberation Sans', 
'Padauk', 'Tlwg Typist', 'Lohit Kannada', 'Lohit Tamil Classical', 'Times New Roman', 
'Arial', 'Noto Serif CJK JP', 'NanumSquare', 'Purisa', 'Pagul', 'Liberation Serif', 
'Ubuntu Mono', 'Sawasdee', 'FreeMono', 'Liberation Sans', 'Trebuchet MS', 
'Liberation Sans Narrow', 'Norasi', 'FreeSans', 'Arial Black', 'Sarai', 'Samyak Devanagari', 
'Noto Sans CJK JP', 'Liberation Serif', 'Sawasdee', 'Verdana', 'Ubuntu', 'Arial', 
'Liberation Sans Narrow', 'Ubuntu', 'Ubuntu', 'Comic Sans MS', 'Manjari', 'Tlwg Typewriter', 
'Tlwg Typist', 'Tlwg Mono', 'Liberation Sans', 'Suruma', 'NanumSquareRound', 'Georgia', 
'Courier New', 'Lohit Gujarati', 'Lohit Assamese', 'NanumGothic', 'Laksaman', 'KacstFarsi', 
'FreeSerif', 'Ubuntu', 'FreeSerif', 'Noto Serif CJK JP', 'KacstNaskh', 'NanumMyeongjo', 
'Khmer OS System', 'Verdana', 'TakaoMincho', 'Times New Roman', 'padmaa', 'Verdana', 
'NanumMyeongjo', 'Impact', 'KacstOne', 'Purisa', 'Georgia', 'Kinnari', 'D2Coding', 
'Verdana', 'Trebuchet MS', 'Times New Roman', 'aakar', 'Mitra Mono', 'RaghuMalayalam', 
'Georgia', 'Kinnari', 'Abyssinica SIL', 'LKLUG', 'FreeSerif', 'Garuda', 'Loma', 'Kalimati', 
'Liberation Sans Narrow', 'Ubuntu', 'Georgia', 'Noto Sans CJK JP', 'FreeMono', 'Trebuchet MS', 
'Andale Mono', 'NanumBarunGothic', 'Trebuchet MS', 'Ubuntu Mono', 'Ubuntu Condensed', 
'Rekha', 'NanumSquareRound', 'Waree', 'FreeSans', 'TakaoPMincho', 'Noto Serif CJK JP', 
'Noto Serif CJK JP', 'Arial', 'Norasi', 'Webdings', 'Ubuntu', 'Noto Sans CJK JP', 
'Norasi', 'Waree', 'Courier New', 'AnjaliOldLipi', 'Noto Sans CJK JP', 'Umpush', 
'Khmer OS', 'Umpush', 'Garuda', 'Georgia', 'Ubuntu', 'Noto Sans CJK JP', 'Tlwg Typo', 
'Laksaman', 'Arial', 'Tlwg Typist', 'Purisa', 'Navilu', 'Courier New', 'Padauk Book', 
'Lohit Odia', 'Webdings', 'Times New Roman', 'Trebuchet MS', 'Arial', 'Noto Serif CJK JP', 
'Lohit Bengali', 'padmaa-Bold.1.1', 'Trebuchet MS', 'Noto Sans CJK JP', 'Kinnari', 
'Tlwg Typo', 'Norasi', 'TakaoPMincho', 'KacstDecorative', 'Sawasdee', 'Ubuntu Mono', 
'Comic Sans MS', 'Umpush', 'Sahadeva', 'Arial', 'Mukti Narrow', 'KacstTitleL', 'Norasi', 
'Noto Serif CJK JP', 'Manjari', 'Samyak Tamil', 'Times New Roman', 'Purisa', 'Verdana', 
'Tlwg Typewriter', 'KacstOffice', 'Ani', 'FreeSans', 'Tibetan Machine Uni', 'Courier New', 
'Rachana', 'Courier New', 'KacstTitle', 'OpenSymbol', 'Uroob', 'Saab', 'Gargi', 
'Arial Black', 'Loma', 'Liberation Mono', 'Noto Serif CJK JP', 'Rachana', 'Meera', 
'Comic Sans MS', 'Samanata', 'Likhan', 'Lohit Malayalam', 'Trebuchet MS', 'Verdana', 
'Tlwg Mono', 'Pothana2000', 'Loma', 'Tlwg Typo', 'Loma', 'D2Coding', 'KacstDigital', 
'Laksaman', 'Padauk', 'FreeSans', 'Phetsarath OT', 'Lohit Devanagari', 'Chandas', 
'Times New Roman', 'Impact', 'Kinnari', 'Lohit Tamil', 'Chilanka', 'Gubbi', 
'Lohit Telugu', 'Comic Sans MS', 'Samyak Malayalam', 'Umpush', 'Nakula', 'FreeSerif', 
'Times New Roman', 'Kalapi', 'NanumSquare', 'KacstPen', 'mry_KacstQurn']
'''

# List font names with CJK
true_type_font_list_CJK = [ font.name for font in fm.fontManager.ttflist if 'CJK' in font.name]
num_ttf_CJK = len(true_type_font_list_CJK)  # number of true type font
print(f'There are {num_ttf_CJK} CJK fonts.' )  # 14
print( true_type_font_list_CJK )
'''
['Noto Sans CJK JP', 'Noto Serif CJK JP', 'Noto Sans CJK JP', 'Noto Serif CJK JP', 
 'Noto Sans CJK JP', 'Noto Serif CJK JP', 'Noto Serif CJK JP', 'Noto Sans CJK JP', 
 'Noto Sans CJK JP', 'Noto Sans CJK JP', 'Noto Serif CJK JP', 'Noto Sans CJK JP', 
 'Noto Serif CJK JP', 'Noto Serif CJK JP']
'''

# List font names with Nanum
true_type_font_list_nanum = [ font.name for font in fm.fontManager.ttflist if 'Nanum' in font.name]
num_ttf_nanum = len(true_type_font_list_nanum)  # number of true type font
print(f'There are {num_ttf_nanum} Nanum fonts.' )  # 10
print( true_type_font_list_nanum )
'''
['NanumBarunGothic', 'NanumGothic', 'NanumSquare', 'NanumSquareRound', 'NanumGothic', 
 'NanumMyeongjo', 'NanumMyeongjo', 'NanumBarunGothic', 'NanumSquareRound', 'NanumSquare']
'''

# Get the paths to fonts
kr_font_list = [ (font.name, font.fname) for font in fm.fontManager.ttflist if 'NanumMyeongjo' in font.name ]
for name, path in kr_font_list:
    print(f'{name}, {path}')
'''
NanumMyeongjo, /usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf
NanumMyeongjo, /usr/share/fonts/truetype/nanum/NanumMyeongjoBold.ttf
'''

#  There're three options to set a font.
#  (1) Use FontProperties
path2font = '/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf'
fontprop  = fm.FontProperties( fname=path2font, size=12 )

plt.title('시간별 가격 추이', fontproperties=fontprop )
plt.ylabel('주식 가격', fontproperties=fontprop )
plt.xlabel('시간(분)', fontproperties=fontprop )
plt.text( 0.5,0,'시간(분)', fontproperties=fontprop  )


# (2) Use rcParams

plt.title('시간별 가격 추이')
plt.ylabel('주식 가격')
plt.xlabel('시간(분)')
plt.text( 0.5,0,'시간(분)' )

plt.rcParams["font.family"] = 'NanumMyeongjo'
plt.rcParams["font.size"]   = 12

plt.title('시간별 가격 추이')
plt.ylabel('주식 가격')
plt.xlabel('시간(분)')
plt.text( 0.5,0,'시간(분)' )


# Japanese fonts
# Get the paths to fonts
jp_font_list = [ (font.name, font.fname) for font in fm.fontManager.ttflist if 'Noto Serif CJK JP' in font.name ]
for name, path in jp_font_list:
    print(f'{name}, {path}')
'''
Noto Serif CJK JP, /usr/share/fonts/opentype/noto/NotoSerifCJK-Black.ttc
Noto Serif CJK JP, /usr/share/fonts/opentype/noto/NotoSerifCJK-Light.ttc
Noto Serif CJK JP, /usr/share/fonts/opentype/noto/NotoSerifCJK-Medium.ttc
Noto Serif CJK JP, /usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc
Noto Serif CJK JP, /usr/share/fonts/opentype/noto/NotoSerifCJK-ExtraLight.ttc
Noto Serif CJK JP, /usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc
Noto Serif CJK JP, /usr/share/fonts/opentype/noto/NotoSerifCJK-SemiBold.ttc
'''
path2font = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc'
fontprop  = fm.FontProperties( fname=path2font, size=12 )

plt.title('時間', fontproperties=fontprop )
plt.ylabel('株式', fontproperties=fontprop )
plt.xlabel('分', fontproperties=fontprop )
plt.text( 0.5,0,'分', fontproperties=fontprop  )