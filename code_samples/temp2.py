    def filter_unknown_vocab_from( self, df_text, df_vocab, max_token_length, verbose=False, debug=False, dummy=False ):
        '''
        Note there're many duplicate reviews AFTER the preprocessing.
        These duplicates should be removed.
          df_text['review'].shape
          (19128,)
          df_text['review'].drop_duplicates().shape
          (18841,)
          df_text['review'].unique().shape
          (18841,)
           
        drop_duplicates() returns a Series while unique() returns a Numpy array.
        
         A valid vocabulary 'nan' causes "KeyError: 'nan'"
           because it's recognized as NaN (Not a number).
         As a quick fix, the vocabulary 'nan' is removed in other script
           because it has only two counts.
         TODO: This is a quick fix. Watch out for this in the later part.

        '''
        assert isinstance( df_text, pd.DataFrame), 'df_text must be a pandas.DataFrame.'
        assert isinstance( df_vocab, pd.DataFrame), 'df_vocab must be a pandas.DataFrame.'
        print( "Filtering unknown vocabularies from 'df_text' with reference to a dictionary 'df_vocab'..." )

        #verbose = True
        token2index_dict = dict( zip( df_vocab['vocabulary'], df_vocab['id'] ) )
        documents_list   = list( df_text['review'] )
        labels_list      = list( df_text['sentiment'] )

        filtered_documents_list = []
        filtered_labels_list    = []
        for index, document in enumerate( documents_list, 0 ):
            tokens = self.nlp.tokenize( document )
            if verbose:
                print( tokens )

            filtered_tokens = []
            token_count = 0
            for token in tokens:  # this token is key of a dictionary
                # If token doesn't exist in the dictionary, it's [unk]
                # vocabulary with low frequency is removed from the vocabulary dictionary. 
                value = token2index_dict.get( token )
                
                if value:              # If found,
                    filtered_tokens.append( token )
                else:                  # If not found,
                    filtered_tokens.append( '[unk]' )
                    
                token_count += 1
            # Filter out a document longer than max_token_count
            if verbose:
                print( index, labels_list[index] )
                print( token_count, document )

            if token_count < max_token_length:
                recreated_document = ' '.join( filtered_tokens )
                filtered_documents_list.append( recreated_document )
                filtered_labels_list.append( labels_list[index] )

        # 1787 reviews are filtered compared to the original review.
        df = pd.DataFrame( filtered_documents_list, columns=['review'] )
        df.insert(0, 'sentiment', filtered_labels_list, False )

        # There're 839 duplicates which are also removed.
        file_duplicated = '../output/df_duplicated.csv'
        df_duplicated = df[ df.duplicated( subset=['review'] ) ]
        df_duplicated = df_duplicated.sort_values( by=['review','sentiment'])
        df_duplicated.to_csv( file_duplicated )
        print('Saved to', file_duplicated)

        # Duplicates in 'review' are removed along with the corresponding 'sentiment'.
        # Note the last one is kept because, at least, one should remain.
        df = df.drop_duplicates( subset=['review'], keep="last" )
        df = df.sort_values( by=['review','sentiment'])
        df_filtered_documents = df

        return df_filtered_documents