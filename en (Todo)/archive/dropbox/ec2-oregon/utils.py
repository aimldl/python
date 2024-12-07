#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os
import numpy as np

from time import gmtime
from time import strftime
from scipy.io import wavfile

from python_speech_features import mfcc

# make a directory under dir_ if no directory exists for device_id_
# The created directory is dir_/device_id_/today_

def makedirs_if_absent( dir_, device_id_ ):
  print(dir_)
#  assert os.path.exists( dir_ ) is True, "dir_ doesn't exist: %s" % dir_
  assert type( device_id_ ) is str, "device_id_ is not a string: %s" % device_id_

  today_ = strftime("%Y%m%d", gmtime() )
  subdir_ = os.path.join( dir_, device_id_, today_ )
  if not os.path.exists( subdir_ ):
    print('Making a directory', subdir_, '...')
    os.makedirs( subdir_ )
	
  return subdir_
 
def save2wav( device_id_, sampling_rate_, payload_ ):
  # assert
  
  now_str_        = strftime("%H-%M-%S", gmtime() )
  file_name_      = "%s.wav" % now_str_  
  target_dir_     = makedirs_if_absent( 'uploads', device_id_ )
  file_           = os.path.join( target_dir_, file_name_ )
  print("Saving payload to %s..." % file)
  wavfile.write( file_, sampling_rate_, payload_ )
  print("payload saved to %s" % file)

  return file_
 
def get_mfcc( signal_, sampling_rate_, window_length_, window_step_, num_features_ ):
  mfcc_feat_      = mfcc( signal_, samplerate=sampling_rate_, winlen=window_length_, winstep=window_step_, numcep=num_features_ )
  mfcc_feat_list_ = list( mfcc_feat_ )
  assert np.shape ( mfcc_feat_list_ )[1] == num_features_, "mfcc_feat_list_'s column size needs to be %d" % num_features_
  
  seq_length_ = np.shape ( mfcc_feat_list_ )[0]
  
  return mfcc_feat_list_, seq_length_

# def split2frames( signal_, sampling_rate_, window_length_, window_step_, num_features_ ):
 
# def preprocess( signal_, sampling_rate_, window_length_, window_step_, num_features_ ):
  # mfcc_feat_list_, seq_length_ = get_mfcc( signal_, sampling_rate_, window_length_, window_step_, num_features_ )
  # split2frames( signal_, sampling_rate_, window_length_, window_step_ )
  
  