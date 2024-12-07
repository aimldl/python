# README.md

## Steps 
1. Create a sub-directory 'vad' under your src directory.
2. Copy webrt_vad.py to the sub-directory vad
3. Add the following lines to run test_run().

```python
from vad.webrt_vad import WebRtVad

vad = WebRtVad()
vad.test_run()
```

The expected output figures are:
* [../figures/webrt_vad-input_signal.png](../figures/webrt_vad-input_signal.png)
* [../figures/webrt_vad-normalized_input_signal.png](../figures/webrt_vad-normalized_input_signal.png)
* [../figures/webrt_vad-speech_samples.png](../figures/webrt_vad-speech_samples.png)

## Comments
The essence of a sequence of working code is to:
1. read in a .wav file
2. 'pack' the samples into binary data
3. partition raw_samples into a_part_of_raw_samples and feed into vad.is_speech( ... )
```python
file = './audio_files/english-0.wav'
samples, fs = self.read_wav( file )
raw_samples = struct.pack( "%dh" % len(samples), *samples)
   ...
is_speech   = self.vad.is_speech( a_part_of_raw_samples, sample_rate=fs )
```
struct.pack and vad.is_speech are error-prone and tricky if the inputs to these functions are not handled properly. 

### struct.pack(format, v1, v2, ..., vn)
struct.pack is used to "pack" the sample values to binary data. For detail, refer to 
[struct.pack(...) the pack function in the struct module](https://blog.naver.com/aimldl/221670484768).

### A working case
is given below for the reference of troubleshooting. Note the following example has a sequence of int16 values in a Numpy array.

```python
ipdb> type(samples)
<class 'numpy.ndarray'>

ipdb> samples
array([-10,  -5,  13, ...,   7,   7,   6], dtype=int16)

ipdb> print( *samples )
-10 -5 13 -2 -12 -12 8 -1 -10 1 6 

  ...

8 2 6 10 14 15 15 5 9 5 2 6 7 7 6

# Just the first 10 samples.
ipdb> print( *samples[:10] )
-10 -5 13 -2 -12 -12 8 -1 -10 1

# Note this fails without print
ipdb> *samples
*** SyntaxError: can't use starred expression here
```

## Troubleshooting
### 1. FileNotFoundError -> Find or specify the correct file location. 
#### Situation/Problem
When you execute text_run(), FileNotFoundError may occur if the example input file is located in the wrong place.
```
FileNotFoundError: [Errno 2] No such file or directory: '../audio_files/english-0.wav'
> project_root/src/vad/webrt_vad.py(41)test_run()
```
#### Task/Problem
To resolve this FileNotFoundError, you may either:
1. move the file to the right location or
2. fix the location in variable 'file' correctly. 

#### Action/Solution
1. Moving the file to the right location
To figure out the directory where vad.test_run() is embedded, os.getcwd() CWD (Current Working Directory) may become handy.

```python
import os
print( os.getcwd() )
```
Say the above lines are inserted to my source code and the output is 'project_root/src'. Copy the .wav file 'english-0.wav' to this directory.

2. Fixing the location in variable 'file' correctly.
After the first attemp above, you may play with the directory name in variable 'file'.

#### Result
1. Copying the .wav file 'english-0.wav' to this directory resolves the FileNotFoundError. Note this is only a temporary solution. But it serves the purpose of test_run() which shows the usage of a working example.

##### Example1
If webrt_vad.py is run as __main__,
```python
if __name__ == '__main__':
    vad = WebRtVad()
    vad.test_run()
```
an error occurs when:
```python
file = '../audio_files/english-0.wav'
os.getcwd()
# '/home/aimldl/Dropbox/sw-done/aws/hula-HunkLabeling/src/vad'
samples, fs = self.read_wav( file )
# *** FileNotFoundError: [Errno 2] No such file or directory: '../audio_files/english-0.wav'
```
The error is fixed when .. is changed to .
```python
file = './audio_files/english-0.wav'
samples, fs = self.read_wav( file )
```
##### Example2
If webrt_vad.py is not run as __main__,
```python
vad.test_run()
```
an error occurs when:
```python
ipdb> os.getcwd()
'/home/aimldl/Dropbox/sw-done/aws/hula-HunkLabeling/src'
ipdb> file = '../audio_files/english-0.wav'

ipdb> samples, fs = self.read_wav( file )
*** FileNotFoundError: [Errno 2] No such file or directory: '../audio_files/english-0.wav'
```
The error is fixed when .. is changed to ./vad
```python
file = './vad/audio_files/english-0.wav'
samples, fs = self.read_wav( file )
```
2. This is not tested for this example, but it's been proved for many other cases. So it works.

### 2. struct.error -> Find or specify the correct file location. 
#### Situation/Problem
When you execute text_run() or run(), struct.error may occur if the input or samples are not integer.
```
struct.error: required argument is not an integer
raw_samples = struct.pack( "%dh" % len(samples), *samples)
```
#### Cause of the Problem
1. The format "%dh" % len(samples) is configures the sample values to h or short int. This error occurs because the sample values and the format do not match.
2. This is an example when samples take in an Numpy array.
```python
ipdb> samples
array([-0.00926745, -0.08785722, -0.37774839, ...,  7.46082969,
        4.06827558,  0.56511622])
ipdb> *samples

```

#### Task/Problem
To resolve this struct.error, you may either:




type( bandpassed_data )
<class 'numpy.ndarray'>

#### Action/Solution

