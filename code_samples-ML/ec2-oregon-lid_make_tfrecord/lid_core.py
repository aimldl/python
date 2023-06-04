#!/usr/bin/env python3
"""
lid_core.py

"""

# Custom package
from utils import makedirs_if_absent
from utils import save2wav

def identify_language( device_id_, sampling_rate_, payload_ ):
  file    = save2wav( device_id, SAMPLING_RATE, payload )
  print('hello')
  
    # preprocess( payload, SAMPLING_RATE, WINDOW_LENGTH, WINDOW_STEP, NUM_FEATURES )