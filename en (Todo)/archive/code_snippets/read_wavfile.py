'''
Rev.2: 2020-01-14 (Tue)
Rev.1: 2019-12-03 (Tue)
Draft: Sometime ago

File name
* Note a function name read_wav already exists.
* Change file name from get_input_wav to read_wavfile.
  
TODO:
1. Check line to ensure file's file extension is .wav.
2. Complete if __name__ == '__main__':
'''

def read_wavfile( file, normalize=True ):
    '''
   
    The following quantities are not used right now, 
    but save them here for future reference.
    nyquist_rate   = fs/2
    n_samples      = len(samples_np)
    n              = np.arange( n_samples ) # 0~ (n_samples-1)
    t              = n / fs
    '''
    from scipy.io import wavfile
    
    fs, samples_np = wavfile.read( file )
    if normalize:
        y_max  = max( abs(samples_np) )
        y_np = samples_np / y_max  # normalize with Peak normalization
    else:
        y_np = samples_np

    return y_np, fs

'''
if __name__ == '__main__':
    read_wavfile()
'''
