#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_tfrecord.py
"""
import os
import sys
import numpy as np
import tensorflow as tf
import resampy
import pickle
import librosa
import datetime
 
from scipy.io import wavfile
from python_speech_features import mfcc
 
LANGUAGE_LABELS = {'english':0, 'korean':1, 'japanese':2, 'chinese':3, 'spanish':4, 'french':5, 'german':6, 'italian':7}
 
class multi_print():
  def __init__(self, stdouts, orig_stdout):
    self.stdouts = stdouts
    self.orig_stdout = orig_stdout
 
  def __call__(self, sentence, end='\n'):
    for _stdout in self.stdouts:
      sys.stdout = _stdout
      print(sentence, flush=True, end=end)
    sys.stdout = self.orig_stdout
 
class MakeTFRecord():
  def __init__(self, sampling_rate, window_size, window_step, t_min, t_max, n_features,
               data_path_tr_val, meta_path_tr_val, n_tot_data_tr_val, valid_rate,
               data_path_test, meta_path_test, n_tot_data_test,
               tfr_path, tfr_path_trn, tfr_path_val, tfr_path_test, tfr_path_info,
               overwrite_tr_val=False, overwrite_test=False,
               multi_print=print):
    self.window_size = window_size
    self.window_step = window_step
    self.data_min_time = t_min
    self.data_max_time = t_max
    self.n_features = n_features
    self.valid_rate = valid_rate
    self.fs = sampling_rate
   
    self.data_path_tr_val = data_path_tr_val
    self.meta_path_tr_val = meta_path_tr_val
    self.n_tot_data_tr_val = n_tot_data_tr_val
    self.data_path_test = data_path_test
    self.meta_path_test = meta_path_test
    self.n_tot_data_test = n_tot_data_test
   
    self.tfr_path = tfr_path
    self.tfr_path_trn = tfr_path_trn
    self.tfr_path_val = tfr_path_val
    self.tfr_path_test = tfr_path_test
    self.tfr_path_info = tfr_path_info
    self.overwrite_tr_val = overwrite_tr_val
    self.overwrite_test = overwrite_test
   
    self.n_aug = 0
       
    self.feat_mean_set = []
    self.feat_std_set = []
    self.feat_mean_set_aug = []
    self.feat_std_set_aug = []
    self.available_aug_idx = []
    self.mprint = multi_print
   
    self.label_in_dataset = []
    self.make_trn_val_data = False
    self.make_test_data = False
 
  def make_trn_val_tfrecord(self):
    if os.path.exists(self.tfr_path_trn) and os.path.exists(self.tfr_path_val) and not self.overwrite_tr_val:
      self.mprint(Warning('Train, Validation TFRecord is already exists.\nTrain path: %s\nValid path: %s'%(self.tfr_path_trn, self.tfr_path_val)))

    else:
      if self.overwrite_tr_val:
        self.mprint('[WARNING] Overwriting train, validation dataset')

      if not len(self.n_tot_data_tr_val) == len(self.meta_path_tr_val):
        self.mprint('# of dataset != # of meta dir, dataset:%d, meta dir:%d'
              %(len(self.meta_path_tr_val), len(self.n_tot_data_tr_val)))
        self.n_tot_data_tr_val = [self.n_tot_data_tr_val[0]]*len(self.meta_path_tr_val)

      file_paths, labels, data_shape, valid_idx, error_msg = self.load_files(self.data_path_tr_val,
                                                                             self.meta_path_tr_val,
                                                                             self.n_tot_data_tr_val,
                                                                             'Train, Valid')
     
      valid_file_paths = np.array(file_paths)[valid_idx]
      valid_labels = np.array(labels)[valid_idx]
      valid_data_shape = np.array(data_shape)[valid_idx]
     
      trn_file_paths = np.delete(file_paths, valid_idx, axis=0)
      trn_labels = np.delete(labels, valid_idx, axis=0)
      trn_data_shape = np.delete(data_shape, valid_idx, axis=0)
     
	  # 이 부분에 있는 shuffle_idx 관련된 내용은 지워도 될듯
      shuffle_idx = np.random.choice(len(trn_file_paths), size=len(trn_file_paths), replace=False)
	  # 이 밑으로는 다 필요
      self.trn_file_paths = np.array(trn_file_paths)[shuffle_idx]
      self.trn_labels = np.array(trn_labels)[shuffle_idx]
      self.trn_data_shape = np.array(trn_data_shape)[shuffle_idx]
      assert len(self.trn_file_paths) == len(self.trn_labels) == len(self.trn_data_shape), \
      'not equal: %s, %s, %s'%(len(self.trn_file_paths), len(self.trn_labels), len(self.trn_data_shape))
     
	  # 이 부분에 있는 shuffle_idx 관련된 내용은 지워도 될듯
      shuffle_idx = np.random.choice(len(valid_file_paths), size=len(valid_file_paths), replace=False)
      # 이 밑으로는 다 필요
	  self.valid_file_paths = np.array(valid_file_paths)[shuffle_idx]
      self.valid_labels = np.array(valid_labels)[shuffle_idx]
      self.valid_data_shape = np.array(valid_data_shape)[shuffle_idx]
      assert len(self.valid_file_paths) == len(self.valid_labels) == len(self.valid_data_shape), \
      'not equal: %s, %s, %s'%(len(self.valid_file_paths), len(self.valid_labels), len(self.valid_data_shape))
     
      self.mprint('trn dataset: %d, validation dataset: %d'
                  %(len(self.trn_file_paths), len(self.valid_file_paths)))
 
      save_txt_path = os.path.join(self.tfr_path, 'trn_data_list.txt')
      self.save_txt(save_txt_path, "\n".join(self.trn_file_paths[:]), 'Save train data list in %s' %(save_txt_path))
     
      save_txt_path = os.path.join(self.tfr_path, 'trn_data_label_list.txt')
      self.save_txt(save_txt_path, "\n".join(np.array(self.trn_labels[:], dtype=np.str)), 'Save train data label list in %s' %(save_txt_path))
       
      save_txt_path = os.path.join(self.tfr_path, 'val_data_list.txt')
      self.save_txt(save_txt_path, "\n".join(self.valid_file_paths[:]), 'Save validation data list in %s' %(save_txt_path))
     
      if not len(error_msg) == 0:
        save_txt_path = os.path.join(self.tfr_path, 'data_error_msg_trn_val.txt')
        self.save_txt(save_txt_path, "\n".join(error_msg), 'Save error msg for trn/valid dataset in %s' %(save_txt_path))
     
      self.make_tfrecord(self.tfr_path_trn, self.trn_file_paths, self.trn_labels, mode='Train')
      self.make_tfrecord(self.tfr_path_val, self.valid_file_paths, self.valid_labels, mode='Valid')
     
      self.trn_mean = np.mean(self.feat_mean_set, axis=0)
      self.trn_std = np.std(self.feat_std_set, axis=0)
      self.n_trn = len(self.trn_file_paths)
      self.n_valid = len(self.valid_file_paths)
      self.make_trn_val_data = True
	  
	  # 여기까지 함...
     
  def make_test_tfrecord(self):
    if os.path.exists(self.tfr_path_test) and not self.overwrite_test:
      self.mprint(Warning('Test TFRecord is already exists.\nTest path: %s\n'
                          %(self.tfr_path_test)))
    else:
      if self.overwrite_test:
        self.mprint('[WARNING] Overwriting test dataset')
     
      if not len(self.n_tot_data_test) == len(self.meta_path_test):
        self.mprint('# of dataset != # of meta dir, dataset:%d, meta dir:%d'
                    %(len(self.meta_path_test), len(self.n_tot_data_test)))
        self.n_tot_data_test = [self.n_tot_data_test[0]]*len(self.meta_path_test)
     
      file_paths, labels, data_shape, _, error_msg = self.load_files(self.data_path_test,
                                                                     self.meta_path_test,
                                                                     self.n_tot_data_test,
                                                                     'Test')
      shuffle_idx = np.random.choice(len(file_paths), size=len(file_paths), replace=False)
      self.test_file_paths = np.array(file_paths)[shuffle_idx]
      self.test_labels = np.array(labels)[shuffle_idx]
      self.test_data_shape = np.array(data_shape)[shuffle_idx]
     
      if not len(error_msg) == 0:
        save_txt_path = os.path.join(self.tfr_path, 'data_error_msg_test.txt')
        self.save_txt(save_txt_path, "\n".join(error_msg),
                      'Save error msg for test dataset in %s' %(save_txt_path))
     
      self.make_tfrecord(self.tfr_path_test, self.test_file_paths, self.test_labels, mode='test')
     
      label2language = [key for label in self.test_labels for key, val in LANGUAGE_LABELS.items() if label == val]
      testdata_language = np.unique(label2language)
     
      self.n_test = len(self.test_file_paths)
      for language in testdata_language:
        self.mprint('# of test dataset: %d, language: %s'
                    %(int(np.sum(np.array(label2language)==language)), language))  
      self.make_test_data = True
 
  def make_augment_tfrecord(self, tfr_path_aug, aug_type='wn', aug_rate=1, overwrite_aug=False):
    self.aug_type = aug_type
    self.aug_rate = aug_rate
    if os.path.exists(tfr_path_aug) and not overwrite_aug:
      self.mprint(Warning('Augmentation TFRecord is already exists.\nAugmentation path: %s'
                          %(tfr_path_aug)))
    else:
      if overwrite_aug:
        self.mprint('[WARNING] Overwriting augmented dataset')
      if not self.make_trn_val_data:
        saved_txt_path = os.path.join(self.tfr_path, 'trn_data_list.txt')
        self.trn_file_paths = self.read_txt(saved_txt_path, 'Load train data list from %s' %(saved_txt_path))
         
        saved_txt_path = os.path.join(self.tfr_path, 'trn_data_label_list.txt')
        self.trn_labels = self.read_txt(saved_txt_path, 'Load train data label list from %s' %(saved_txt_path))
        if not type(self.trn_labels[0]) == int:
          self.trn_labels = np.array(self.trn_labels, dtype=np.int16)
         
        with open(self.tfr_path_info, 'rb') as f:
          _data_info = pickle.load(f)
          self.trn_data_shape = _data_info['trn_data_shape']
         
      self.make_tfrecord(tfr_path_aug, self.trn_file_paths, self.trn_labels, 'Augmentation')       
      
      self.trn_aug_data_shape = self.trn_data_shape[np.array(self.available_aug_idx)]
      self.trn_aug_mean = np.mean(self.feat_mean_set_aug, axis=0)
      self.trn_aug_std = np.std(self.feat_std_set_aug, axis=0)
 
  def load_files(self, data_path, meta_path, n_data, mode=None):
    file_paths, file_labels, data_shape, file_info, error_msg= [],[],[],[],[]
   
    self.mprint('%s data checking..' %mode)
    for _idx, _meta_path in enumerate(meta_path):
      _file_paths, _file_labels, _data_shape = [],[],[]
      _len_error_msg = len(error_msg)
      _len_file_paths = len(file_paths)
      _dataset_name = os.path.basename(_meta_path).split('.txt')[0]
      _file_dir = os.path.join(data_path, _dataset_name)
      _language = _dataset_name.split('_')[0]
      if not mode == 'Test':
        _label_check = LANGUAGE_LABELS[_language]
        self.label_in_dataset.append(_label_check)       
      
      with open(_meta_path, 'r') as f:
        _meta_data = f.read().splitlines()
      self.mprint('[%s] Load meta data from %s and data from %s'
                  %(_language, _dataset_name, _file_dir))
      np.random.shuffle(_meta_data)
      _data_len_check = len(_meta_data) >= n_data[_idx]
      _max_len = n_data[_idx] if _data_len_check else len(_meta_data)
     
      progress = Progress(_max_len, 20)
      while len(_file_paths) < _max_len:
        try:
          _fname, _label = _meta_data.pop().split(" ")
          if not mode == 'Test':
            assert int(_label) == _label_check, \
            "label of %s is %d, but data is labeled as %d" \
            %(_file_paths, _label_check, int(_label)) 
          else:
            assert int(_label) in self.label_in_dataset, \
            "label of %s is %d, but train dataset is only available %s" \
            %(_file_paths, int(_label), self.label_in_dataset)
        except:
          break
        
        _file_path = os.path.join(_file_dir, _fname)
        _fs, _wav_data = wavfile.read(_file_path)
        if not _fs == self.fs:
          _wav_data = resampy.resample(_wav_data, _fs, self.fs)
          error_msg.append('[(Warning) Sampling rate error] Sampling Rate is required 16kHz, file: %s has %dHz' \
                           %(_file_path, _fs))
        if not mode == 'Test':
          _check_result = self.data_check(_wav_data, _file_path, error_msg)
          # 학습 단계에서는 data를 확인하고 학습 데이터에 포함
        else:
          _check_result = True
          # 테스트 단계에서는 모든 data를 포함
       
        if _check_result:         
          _file_paths.append(_file_path)
          _data_shape.append([len(_wav_data)/_fs, self.window_size*_fs, int(_label)])
          _file_labels.append(int(_label))
       
	    # text file에 저장할 때는, 0, 0.25, 0.50, 0.75, 1.0일때만 progress bar를 text파일에 저장함.
		# 이것이 필요한 이유는 text파일의 경우, new line으로 넘어가서 이렇게 저장횟수를 제한함.
        if len(_file_paths) == 1 or len(_file_paths) == int(_max_len*0.25) or len(_file_paths) == int(_max_len*0.5) or len(_file_paths) == int(_max_len*0.75) or len(_file_paths) == int(_max_len-1):
          progress(_dataset_name, len(_file_paths), len(error_msg)-_len_error_msg, _print=self.mprint)
        # cmd line임.
		else:
          progress(_dataset_name, len(_file_paths), len(error_msg)-_len_error_msg)
	  # end of while

	  
      if not len(_file_paths) == _max_len:

        self.mprint(' Expected: %d, but get: %d' %(_max_len, len(_file_paths)))

      

      if mode == 'Train, Valid':

        _n_valid = int(len(_file_paths) * self.valid_rate)     
		
		# _len_file_paths이 지금은 0인데 왜 있는지 잘 모르겠음...
		# 중요: tr vs. val data를 randomize하는데... 전체 데이터에 대해서가 아니라, 각 dataset에 대해 80:20으로 나누기 위해서.
		# _len_file_paths 로 offset을 해준다.
        _valid_idx = np.random.choice(len(_file_paths), size=_n_valid, replace=False) + _len_file_paths # validation dataset index

        file_info.extend(_valid_idx)

     

      file_paths.extend(_file_paths)

      file_labels.extend(_file_labels)

      data_shape.extend(_data_shape)
	  # end of for
           

    return file_paths, file_labels, data_shape, file_info, error_msg

   

  def data_check(self, _wav_data, _file_path, _error_msg):

    _rec_time = len(_wav_data)/self.fs

 

    if not _wav_data.dtype == np.int16:

      _error_msg.append('[Bits] wavfile is %s \n' %(type(_wav_data)))

      return False

   

    if not 50 < np.std(_wav_data):

      _error_msg.append('[Silence] mean: %.3f, std: %.3f check %s \n' \

                        %(np.mean(_wav_data), np.std(_wav_data), _file_path))

      return False

   

    if _rec_time < self.data_min_time:

      _error_msg.append('[Minimum recording time] Recording time of %s is too short, %.3f \n' \

                        %(_file_path, _rec_time))

      return False

   

    if _rec_time > self.data_max_time:

      _error_msg.append('[Maximum recording time] Recording time of %s is too long, %.3f \n' \

                        %(_file_path, _rec_time))

      return False   

      

    return True

   

  

  def make_tfrecord(self, tfr_path, file_path, labels, mode=None): 

    dataset = zip(file_path, labels)

   

    options = tf.python_io.TFRecordOptions(compression_type=tf.python_io.TFRecordCompressionType.GZIP)   

    writer = tf.python_io.TFRecordWriter(path=tfr_path, options=options)

   

    self.mprint('[%s] Make TFRecord files..' %mode)

    _max_progress = len(file_path)

    progress = Progress(_max_progress, 20)

    for _idx, (_file_path, _label) in enumerate(dataset):

      _fs, _wav_data = wavfile.read(_file_path)

      if not _fs == self.fs:

        _wav_data = resampy.resample(_wav_data, _fs, self.fs)

     

      if mode == 'Augmentation':

        _error_msg = [] # not use

        if self.aug_type == 'wn':

          aug = self.adding_white_noise

        elif self.aug_type == 'stretch':

          aug = self.stretching

        _wav_data = aug(_wav_data, _fs, self.aug_rate) # 0.01 ~ 0.005

        _data_check = self.data_check(_wav_data, _file_path, _error_msg)

        

        if _data_check:

          _splited_data, _seq_length = self.split_frame(_wav_data, _fs, winfunc=np.hamming)

          _feat_data, _mfcc_seq_length = self.mfcc_extractor(_wav_data, _fs)

          assert _seq_length == _mfcc_seq_length, \

          'calculated sequence length: %d, mfcc sequence length: %d, check: %s' \

          %(_seq_length, _mfcc_seq_length, _file_path)

         

          self.write_sequence_tfrecords(writer, _wav_data, _splited_data, _feat_data, _label, _seq_length)

          self.n_aug += 1

          self.available_aug_idx.append(_idx)

          self.feat_mean_set_aug.append(np.mean(_feat_data, axis=0))

          self.feat_std_set_aug.append(np.std(_feat_data, axis=0))

           

      else:     

        _splited_data, _seq_length = self.split_frame(_wav_data, _fs, winfunc=np.hamming)

        _feat_data, _mfcc_seq_length = self.mfcc_extractor(_wav_data, _fs)

        assert _seq_length == _mfcc_seq_length, \

        'calculated sequence length: %d, mfcc sequence length: %d, check: %s' \

        %(_seq_length, _mfcc_seq_length, _file_path)

       

        self.write_sequence_tfrecords(writer, _wav_data, _splited_data, _feat_data, _label, _seq_length)

     

      if mode == 'Train':

        self.feat_mean_set.append(np.mean(_feat_data, axis=0))

        self.feat_std_set.append(np.std(_feat_data, axis=0))

       

      if _idx == 0 or _idx == int(_max_progress*0.25) or _idx == int(_max_progress*0.5) or _idx == int(_max_progress*0.75) or _idx == int(_max_progress-1):

        progress('%s' %mode, _idx+1, _print=self.mprint)

      else:

        progress('%s' %mode, _idx+1)

       

    writer.close()

   

  def write_sequence_tfrecords(self, writer, wav_data, raw_data, feat_data, label, seq_len):   

    _wav_data = np.array(wav_data).tostring()

    _raw_data = np.array(raw_data).tostring()

    _feat_data = np.array(feat_data).tostring()

   

    example_sequence = tf.train.SequenceExample()

   

    example_sequence.context.feature['label'].int64_list.value.append(label)

    example_sequence.context.feature['sequence_length'].int64_list.value.append(seq_len)

   

    fl_wav_data = example_sequence.feature_lists.feature_list['wav_data']

    fl_raw_data = example_sequence.feature_lists.feature_list['raw_data']

    fl_feat_data = example_sequence.feature_lists.feature_list['feat_data']

   

    fl_wav_data.feature.add().bytes_list.value.append(_wav_data)

    fl_raw_data.feature.add().bytes_list.value.append(_raw_data)

    fl_feat_data.feature.add().bytes_list.value.append(_feat_data)

   

    writer.write(example_sequence.SerializeToString())

 

  def mfcc_extractor(self, _wav_data, _fs):  

    _mfcc_data = list(mfcc(_wav_data, self.fs, numcep=self.n_features, nfilt=self.n_features, winlen=self.window_size, winstep=self.window_step, winfunc=np.hamming))

    assert np.shape(_mfcc_data)[1] == self.n_features

       

    _seq_length = np.shape(_mfcc_data)[0]

    return _mfcc_data, _seq_length

 

  def split_frame(self, _wav_data, _fs, winfunc=lambda x:np.ones((x,))):

    slen = len(_wav_data)

    frame_len = int(self.window_size*self.fs)

    frame_step = int(self.window_step*self.fs)

   

    if slen <= frame_len:

      numframes = 1

    else:

      numframes = 1 + int(np.ceil((1.0*slen - frame_len)/frame_step))

   

    padlen = int((numframes-1)*frame_step + frame_len)

 

    zeros = np.zeros((padlen - slen,))

    padsignal = np.concatenate((_wav_data, zeros))

   

    indices = np.tile(np.arange(0, frame_len),(numframes,1)) + np.tile(np.arange(0,numframes*frame_step,frame_step),(frame_len,1)).T

    indices = np.array(indices, dtype=np.int32)

    frames = padsignal[indices]

   

    win = np.tile(winfunc(frame_len),(numframes,1))

    new_frames = frames*win

    _seq_length = len(new_frames)

   

    return new_frames, _seq_length

 

  def adding_white_noise(self, data, fs, rate): # 0.001 ~ 0.005

    _data = data / 32768.0

    wn = np.random.randn(len(data))

    data_wn = np.int16((_data + rate*wn) * 32768.0)

    return data_wn

 

  def stretching(self, data, fs, rate): # 0.8, 0.9, 1.1, 1.2

    _data = data / 32768.0

    data_stretching = np.int16(librosa.effects.time_stretch(_data, rate) * 32768.0)

    return data_stretching

 

  def save_txt(self, path, data, print_msg=None):

    if not print_msg == None:

      self.mprint(print_msg)

    with open(path, 'wt') as f:

      f.writelines(data)

     

  def read_txt(self, path, print_msg=None):

    if not print_msg == None:

      self.mprint(print_msg)

    with open(path, 'rt') as f:

      data = f.read().splitlines()

    return data

 

 

class Progress():

  def __init__(self, max_iter, _max_bar=50):

    self.max_iter = max_iter

    self.max_bar = _max_bar

    self.iter_digit = int(np.log10(max_iter))+1

 

  def __call__(self, language, current_iter, n_error_file=None, _print=sys.stdout.write):

    step = int(round(current_iter/self.max_iter * self.max_bar))

    percent = current_iter/self.max_iter* 100

    bar = '%8.3f%% |' %percent + '#' * step + ' ' * (self.max_bar - step) + '|'

    if not n_error_file == None:

      _print(('\r[%s] [%'+'%dd]'%self.iter_digit + '%s [# of error file: %d]') %(language, current_iter, bar, n_error_file))

    else:

      _print(('\r[%s] [%'+'%dd]'%self.iter_digit + '%s') %(language, current_iter, bar))

    if self.max_iter == current_iter:

      _print('\n')

#    sys.stdout.flush()

 

if __name__ == "__main__":
  flags = tf.app.flags
  flags.DEFINE_string("data_dir", "/home/taehwan/Documents/Data/Speech/voxforge/data", "Traing dataset directory.")
  flags.DEFINE_string("dataset", "english_giga,korean_giga", "Dataset name.")
  flags.DEFINE_string("datatype", "wavfiles", "Type of dataset. default: wavfiles")
  flags.DEFINE_string("dataset_test", "english_LCD,korean_LCD", "Dataset for test")
  flags.DEFINE_string('tfr_dir_name', 'tfrecord', "Directory of TFRecord files.")
  flags.DEFINE_string("n_trn_data", '100', "Total number of training and validation data. default: 100")
  flags.DEFINE_string("n_test_data", '10', "Number of maximum test data. If test dataset is less than maximum test data, then use all test dataset during testing phase. default: 10")
  flags.DEFINE_bool('data_aug', False, "Data augmentation")
  flags.DEFINE_string('aug_type', 'stretch', 'Augmentation type. wn, stretch')
  flags.DEFINE_float('aug_rate', 1.1, 'Augmentation rate. Recommand: [0.01, 0.008, 0.005] for wn, [0.8, 0.9, 1.1, 1.2] for stretch ')
  flags.DEFINE_float('window_size', 0.025, 'Window size for each frame')
  flags.DEFINE_float('window_step', 0.01, 'Window step')
  flags.DEFINE_integer('fs', 16000, 'Sampling rate of wavfiles')
  flags.DEFINE_float('T_min', 0.5, 'Minimum time of wavfile')
  flags.DEFINE_float('T_max', 10, 'Maximum time of wavfile')
  flags.DEFINE_float('valid_rate', 0.2, 'Rate of Validation data. n_trn_data*valid_rate: number of validation dataset')
  flags.DEFINE_integer('n_mfcc_feat', 26, 'Feature dimensions of MFCC. default: 26(maximum)')
  flags.DEFINE_bool('overwrite', False, "Overwrite train/valid tfrecord")
  flags.DEFINE_bool('overwrite_test', False, "Overwrite test tfrecord")
  flags.DEFINE_bool('overwrite_aug', False, "Overwrite augmentation tfrecord")
  flags.DEFINE_string('add_log', '', 'Add someting to TFRecord directory name')
  conf = flags.FLAGS
 
  dataset = conf.dataset.replace(" ", "").split(',')
  dataset_char = "".join(['%c' %i[0] for i in dataset])
  dataset_test = conf.dataset_test.replace(" ", "").split(',')
  dataset_type = conf.datatype
  T_min = conf.T_min
  T_max = conf.T_max
  n_features = conf.n_mfcc_feat
 
  data_dir = os.path.join(conf.data_dir, dataset_type)
  meta_dir = [os.path.join(conf.data_dir, 'meta', '%s.txt' %(_data)) for _data in dataset]
 
  n_trn_data = [int(_val) for _val in conf.n_trn_data.replace(" ", "").split(',')]
  n_test_data = [int(_val) for _val in conf.n_test_data.replace(" ", "").split(',')]
  n_class = len(np.unique([LANGUAGE_LABELS[_dataset.split('_')[0]] for _dataset in dataset]))
  valid_rate = conf.valid_rate
 
  sampling_rate = conf.fs
  window_size = conf.window_size
  window_step = conf.window_step
 
  augmentation = conf.data_aug
  aug_type = conf.aug_type
  aug_rate = conf.aug_rate  
  
  overwrite_tr_val = conf.overwrite
  overwrite_test = conf.overwrite_test
  overwrite_aug = conf.overwrite_aug
 
  LOG_DIR = 'log/%s/%s' %(dataset_char, dataset_type)   
  
  tfrecord_info = os.path.join(dataset_char, 'min_%.1f_max_%.1f_winsize_%s_winstep_%s_ndata_%d'%(T_min, T_max, window_size, window_step, n_trn_data[0]))
  if not conf.add_log == '':
    tfrecord_info += '_%s' %conf.add_log
  tfrecord_path = os.path.join(conf.data_dir, conf.tfr_dir_name, tfrecord_info)
 
  if not os.path.exists(tfrecord_path):
    os.makedirs(tfrecord_path)
   
  tfrecord_path_trn = os.path.join(tfrecord_path, 'raw_mfcc_trn.tfrecords')
  tfrecord_path_valid = os.path.join(tfrecord_path, 'raw_mfcc_val.tfrecords')
  tfrecord_path_test = os.path.join(tfrecord_path, 'raw_mfcc_test.tfrecords')
  tfrecord_path_aug = os.path.join(tfrecord_path, 'raw_mfcc_trn_aug_%s_%s.tfrecords'%(aug_type, aug_rate))
 
  meta_dir_test = [os.path.join(conf.data_dir, 'meta', '%s.txt' %(_data)) for _data in dataset_test]
   tfrecord_path_info = os.path.join(tfrecord_path, 'dataset_info.pkl')
 
  orig_stdout = sys.stdout
 date = datetime.datetime.now().strftime('%Y%m%d_%H:%M')
 txt_stdout = open(tfrecord_path + '/history_%s.txt'%date, 'wt')
 _stdouts = [orig_stdout, txt_stdout]
  mprint = multi_print(_stdouts, orig_stdout)

   config_keys = [key for key in conf]
  config_keys.sort()
  for key in config_keys:
    mprint('%s: %s' %(key, conf[key].value))

  record = MakeTFRecord(sampling_rate, window_size, window_step, T_min, T_max, n_features,
                        data_dir, meta_dir, n_trn_data, valid_rate,
                        data_dir, meta_dir_test, n_test_data,
                        tfrecord_path, tfrecord_path_trn, tfrecord_path_valid, tfrecord_path_test, tfrecord_path_info,
                        overwrite_tr_val, overwrite_test,
                        mprint)
  if not os.path.exists(tfrecord_path_info) or not os.path.exists(tfrecord_path_trn) or not os.path.exists(tfrecord_path_valid) or overwrite_tr_val:
    record.make_trn_val_tfrecord()
    DATA_INFO = dict()

    for key in conf:
      DATA_INFO[key] = conf[key].value if not key in ['dataset', 'dataset_test'] else conf[key].value.replace(" ", "").split(',')
  
    DATA_INFO['LANGUAGE_LABELS'] = LANGUAGE_LABELS
    DATA_INFO['LOG_DIR'] = LOG_DIR
    DATA_INFO['n_class'] = n_class
    DATA_INFO['n_trn'] = record.n_trn
    DATA_INFO['n_valid'] = record.n_valid
    DATA_INFO['label_in_dataset'] = np.unique(record.label_in_dataset)
    DATA_INFO['trn_data_shape'] = record.trn_data_shape
    DATA_INFO['valid_data_shape'] = record.valid_data_shape
    DATA_INFO['trn_mean'] = record.trn_mean
    DATA_INFO['trn_std'] = record.trn_std
    DATA_INFO['tfrecord_path_trn'] = tfrecord_path_trn
    DATA_INFO['tfrecord_path_valid'] = tfrecord_path_valid

    with open(tfrecord_path_info, 'wb') as f:
      pickle.dump(DATA_INFO, f)
  else:
    mprint('Do not make the tfrecord files for train/valid')

  if not os.path.exists(tfrecord_path_test) or overwrite_test:
    if not record.make_trn_val_data:
      with open(tfrecord_path_info, 'rb') as f:
        DATA_INFO = pickle.load(f)
      record.label_in_dataset = DATA_INFO['label_in_dataset']
    record.make_test_tfrecord()

    DATA_INFO['n_test'] = record.n_test
    DATA_INFO['tfrecord_path_test'] = tfrecord_path_test
    DATA_INFO['dataset_test'] = conf['dataset_test'].value.replace(" ", "").split(',')

    with open(tfrecord_path_info, 'wb') as f:
      pickle.dump(DATA_INFO, f)
  else:
    mprint('Do not make the tfrecord files for test')
   

  if augmentation:

    if not os.path.exists(tfrecord_path_aug) or overwrite_aug:             

      record.make_augment_tfrecord(tfrecord_path_aug, aug_type=aug_type, aug_rate=aug_rate, overwrite_aug=overwrite_aug)

     

      with open(tfrecord_path_info, 'rb') as f:

        DATA_INFO = pickle.load(f)

      _backup_name = 'dataset_info_backup_before_%s_%s.pkl'%(aug_type, aug_rate)

      os.rename(tfrecord_path_info, os.path.join(tfrecord_path, _backup_name))

     

      DATA_INFO['n_aug_%s_%s'%(aug_type, aug_rate)] = record.n_aug

      DATA_INFO['tfrecord_path_trn_aug_%s_%s'%(aug_type, aug_rate)] = tfrecord_path_aug

      DATA_INFO['trn_aug_%s_%s_mean'%(aug_type, aug_rate)] = record.trn_aug_mean

      DATA_INFO['trn_aug_%s_%s_std'%(aug_type, aug_rate)] = record.trn_aug_std

      DATA_INFO['trn_aug_data_shape_%s_%s'%(aug_type, aug_rate)] = record.trn_aug_data_shape

      

      with open(tfrecord_path_info, 'wb') as f:

        pickle.dump(DATA_INFO, f)

    else:

      mprint('Do not make the tfrecord files for augmentation')

 

  mprint('Make TFRecord is finished.')

else:

  raise ImportError('Wrong access. This script is for only making tfrecord.')
