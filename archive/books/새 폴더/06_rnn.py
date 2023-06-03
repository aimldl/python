# -*- coding: utf-8 -*-
"""
6장. 순환 신경망

* Draft: 2020-0322 (Sun)

@author: aimldl
"""

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

n_hidden = 35
lr = 0.01
epochs = 1000

string = "hello pytorch. how long can a rnn cell remember?"
chars = "abcdefghijklmnopqrstuvwxyz ?!.,:;01"
char_list = [i for i in chars]
n_letters = len(char_list)