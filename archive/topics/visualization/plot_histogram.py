##### aimldl/python3/topics/visualization/plot_histogram.py
'''
Draft: 2020-01-14 (Tue)
'''

def plot_histogram( x, title='Histogram', xlabel='x', ylabel='Frequency' ):
    '''
    plot_histogram( sample_length_list, 
                    title='Histogram: Sample Length of Speech Signals',
                    xlabel='Sample Length',
                    ylabel='Frequency' )

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    hist, ax = plt.subplots()
    ax = sns.distplot( x, kde=False )
    ax.set_title( title )
    ax.set_xlabel( xlabel )
    ax.set_ylabel( ylabel )
    plt.show()
    
if __name__ == '__main__':
  # TODO: Replace the input to a more realistic one.
  #       I haven't tested the following input works with the function.
  #       The function does work, though.
  plot_histogram( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] )
