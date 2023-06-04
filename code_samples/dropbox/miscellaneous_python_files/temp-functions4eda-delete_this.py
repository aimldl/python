#    get_percentage( pd_series, '.', 'periods' )
#    get_percentage( pd_series, '?', 'questionmarks' )
#    get_percentage( pd_series, '\n', 'new_lines' )
#    get_percentage( pd_series, '\r', 'returns' )

def get_percentage(pd_series, pattern, name):
    """
    pd_series  Pandas Series
    Usage:
      get_percentage( pd_series, pattern, name )
    Example:
    To find a pattern '.' from reviews and print as 'periods',
      get_percentage( reviews, '.', 'periods' )
        
    The above line is equivalent to the following two lines.
      count_period = pd_series.astype(str).apply( lambda x: '.' in x )
      print('  periods: {:.3f}%'.format( np.mean( count_period )* 100))
    """

    print(type(pattern), repr(pattern) )
    # Using np.mean is a more elegant implementation than using value_counts().
    #series_true_false = pd_series.astype(str).apply( lambda x: '.' in x )
#    series_true_false = pd_series.astype(str).apply( lambda x: repr(pattern) in x )
#    percentage        = np.mean( series_true_false )* 100
    
#    print(f'  {name}: {percentage:.6f}%')

    # For Debugging
    #return series_true_false
    
    # A test code
    #import functions4eda as eda
    #
    # Define what I want.
    # test = ['asdf.', 'efasdf.', 'efasdf.', 'asfefaf.']
    # reviews = pd.Series( test )
    # temp = eda.print_stats( reviews )
    # type(temp)
    # pandas.core.series.Series
    # temp
    # 0     True
    # 1    False
    # 2     True
    # 3     True
    # dtype: bool
