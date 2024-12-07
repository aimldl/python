# -*- coding: utf-8 -*-
"""
* Draft: 2020-12-21 (Mon)

"""

def html2txt( input_file, output_file ):
    # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    assert isinstance( input_file, str), "input_file must be a string."
    assert isinstance( output_file, str), "output_file must be a string."

    from bs4 import BeautifulSoup
    with open( input_file ) as f:
        soup = BeautifulSoup( f, 'lxml' )
    f.close()

    print( 'Title:', soup.title )
    full_text = soup.get_text()
    #print( full_text )
    with open( output_file, 'w') as f:
        f.write( full_text )
    f.close()
    return full_text

def ls( pattern ):
    # https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    import glob
    return glob.glob( pattern )

def get_filename( file ):
    # https://www.kite.com/python/examples/4300/os-remove-the-file-extension-from-a-filename
    import os
    return os.path.splitext( file )[0]

def get_files_to_translate():
    list_all_txt_files = ls( "*.txt" )
    # ['chapter-8.txt', 'chapter-3.txt', 'chapter-2.txt', 'chapter-1.txt', 'chapter-7.txt', '_formatted_all.txt', 'chapter-1_2.txt', 'chapter-4.txt', 'chapter-5.txt', 'chapter-9.txt', 'index.txt', 'chapter-6.txt', 'chapter-10.txt', 'appendix.txt']
    
    # Exclude '_formatted_all.txt' from the list of text files to translate
    list_txt_files_to_translate = []
    for file in list_all_txt_files:
        if file != text_file_name:
            #print( file )
            list_txt_files_to_translate.append( file )

    #print( list_txt_files_to_translate )    
    #['chapter-8.txt', 'chapter-3.txt', 'chapter-2.txt', 'chapter-1.txt', 'chapter-7.txt', 'chapter-1_2.txt', 'chapter-4.txt', 'chapter-5.txt', 'chapter-9.txt', 'index.txt', 'chapter-6.txt', 'chapter-10.txt', 'appendix.txt']
    return list_txt_files_to_translate

def sent_tokenize( text ):
    # Google search: python read each sentences from file
    # https://stackoverflow.com/questions/27209278/reading-sentences-from-a-text-file-and-appending-into-a-list-with-python-3
    # pip install nltk
    # And then getting your sentences would be a fairly straightforward (although highly customizable) affair. Here's a simple example using the provided sentence tokenizer
    # import nltk
    # with(open('text.txt', 'r') as in_file):
    #     text = in_file.read()
    #     sents = nltk.sent_tokenize(text)
       
    import nltk
    nltk.download('punkt')

    sentences = nltk.sent_tokenize( text )
    return sentences

def translate( sentences, csv_file_name,  index_from=0, verbose=True ):
    # https://pypi.org/project/googletrans/
    # https://github.com/ssut/py-googletrans
    # Installation with the following command will cause an error.
    #   $ pip install googletrans
    # when the following codes are executed.
    #   from googletrans import Translator
    #   translator = Translator()
    #   print( translator.detect('이 문장은 한글로 쓰여졌습니다.') )\
    # AttributeError: 'NoneType' object has no attribute 'group'
    #
    # Change the command to 
    # $ pip install googletrans==4.0.0-rc1
    # Source:
    #   Google search:
    #     googletrans AttributeError: 'NoneType' object has no attribute 'group'
    #   https://github.com/ssut/py-googletrans/issues/234
    #   The successfull command is in the middle of discussions.


    # limit = 5000    # GCP has 5,000 character limit.

    # 3017
    # C.1.2.
    # Traceback (most recent call last):
    
    #   File "/home/aimldl/github/tests/kubeflow_for_machine_learning_html/html2txt.py", line 99, in <module>
    #     translated_sentence = translator.translate( sentence, dest='ko' ).text
    
    #   File "/home/aimldl/anaconda3/lib/python3.8/site-packages/googletrans/client.py", line 194, in translate
    #     data, response = self._translate(text, dest, src)
    
    #   File "/home/aimldl/anaconda3/lib/python3.8/site-packages/googletrans/client.py", line 122, in _translate
    #     if r.status_code != 200 and self.raise_Exception:
    
    # AttributeError: 'Translator' object has no attribute 'raise_Exception'
    # texts_df.to_csv( csv_file_name )

    assert isinstance( sentences, list ), 'sentences must be a list.'
    
    import pandas as pd
    from googletrans import Translator
    translator = Translator()
        
    texts_df = pd.DataFrame( sentences, columns=['original'] )
    texts_df['google_translate'] = ''
    
    for index, columns in texts_df.iterrows():
        # If an error occurs in the middle, skipp until the index where the error occurred.
        if index >= index_from:
            sentence = columns['original']
            translated_sentence = translator.translate( sentence, dest='ko' ).text
            texts_df['google_translate'].loc[index] = translated_sentence
            if verbose:
                print( index, ':', sentence )    

    print( 'Saving the original and translated sentences to ', csv_file_name)
    texts_df.to_csv( csv_file_name )
    
    return texts_df

# def translate_with_naver_papago():

#     # TODO: Make this work. 2020-12-21 (Mon)
#     text = '테스트입니다'
    
#     client_id     = 'dummy_id'
#     client_secret = 'dummy_api_key '
#     url = 'https://'
#     val = {
#       'source': 'ko'
#       'target': 'zh-CN'
#       'text': text
#     }
#     headers = {
#         'X-NCP-APIGW-API-KEY-ID': client_id,
#         'X-NCP-APIGW-API-KEY': client_secret
#     }
    
#     response =  requests.post( url, data=val, headers=headers )
#     rescode = response.status_code


if __name__ == '__main__':
    
    import os.path
    
    html_file_name = '_formatted_all.html'
    text_file_name = '_formatted_all.txt'
    csv_file_name  = get_filename( text_file_name ) + '.csv'
    
    if not os.path.isfile( text_file_name ):
        # https://linuxize.com/post/python-check-if-file-exists/
        full_text = html2txt( html_file_name, text_file_name )
    else:
        with open( text_file_name ) as f:
            full_text = f.read()
    #print( full_text )
    #input( 'pause' )

    sentences = sent_tokenize( full_text )
    #print( sentences[0] )
    #sentences = ['This is a test.', 'Another test sentence.']
    
    index_from = 3017
    sentences_df = translate( sentences, csv_file_name, index_from )


    # from googletrans import Translator
    # translator = Translator()
    # # print( translator.detect('이 문장은 한글로 쓰여졌습니다.') )\
    # # Detected(lang=ko, confidence=None)
    
    # #print( translator.translate('안녕하세요.', dest='ja') )
    # #Translated(src=ko, dest=ja, text=こんにちは。, pronunciation=Kon'nichiwa., extra_data="{'confiden...")
    
    # # print( translator.translate('안녕하세요.', dest='en') )
    # # Translated(src=ko, dest=en, text=Good morning., pronunciation=None, extra_data="{'confiden...")
    
    # #print( translator.translate('안녕하세요.', dest='en').text )
    # #Good morning.
    
    # # print( translator.translate('Hello, world!', dest='ko').text )
    # # 안녕하세요, 세상!
    
    # for file in list_txt_files_to_translate:
    #     translated_sentences = []
    #     with open( file ) as f:
    #         text = f.read( )
    #         sentences = nltk.sent_tokenize( text )
    #         sentences = ['This is a test.', 'Another test sentence.']
    #         for sentence in sentences:
    #             #print( sentence )
    #             translated_sentence = translator.translate( sentence, dest='ko').text
    #             #print( translated_sentence )
    #             #input('pause')
    #             translated_sentences += [ ' '.join( char ) for char in translated_sentence ]
                
    #     f.close()
              
    #     file_output = get_filename( file ) + '-ko.txt'
    #     #print( file_output )
    #     input('pause')
    #     print( translated_sentences )
    #     with open( file_output, 'w' ) as f:
    #         f.write( translated_sentences )
    #     f.close()

    #     input('pause')
        
    # _formatted_all.txt was checked manually.
    # It looked OK. Each chapter is broken down into several files.
    
    #list_files_to_translate = get_files_to_translate()
