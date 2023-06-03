'''

TensorFlow + SageMaker = love by Enias Cailliau
https://medium.com/radix-ai-blog/tensorflow-sagemaker-d17774417f08
Github: https://github.com/radix-ai/sagemaker-tensorflow-tutorial

pipe input mode
https://aws.amazon.com/about-aws/whats-new/2018/05/pipe-input-mode-is-now-supported-in-amazon-sagemaker-algorithms/
automatic model tuning.
https://aws.amazon.com/blogs/aws/sagemaker-automatic-model-tuning/
'''

import os
import numpy as np
import matplotlib.pyplot as plt
import sagemaker
import tensorflow as tf
print(f'TF Version: {tf.__version__}')

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Shapes of training, test and validation set
print("Fashion MNIST:")
print("Training set (images) shape: {shape}".format(shape=train_images.shape))
print("Training set (labels) shape: {shape}".format(shape=train_labels.shape))

print("Test set (images) shape: {shape}".format(shape=test_images.shape))
print("Test set (labels) shape: {shape}".format(shape=test_labels.shape))

#
labels_lookup = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress',
                 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
                ]
                

plt.figure( figsize=(10,10) )
for ii in range(25):
    plt.subplot( 5,5,ii+1 )
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow( train_images[ii], cmap=plt.cm.binary )  # colormap?
    plt.xlabel( labels_lookup[ train_labels[ii] ] )
    # or plt.xlabel( labels_lookup[ ii ] )
    
# Convert MNIST data to TFRecords file format
#   TFRecords https://medium.com/mostly-ai/tensorflow-records-what-they-are-and-how-to-use-them-c46bc4bbb564
def _int64_feature( value ):
    return tf.train.Feature( int64_list = tf.train.Int64List(value=[value]) )

def _bytes_feature( value ):
    return tf.train.Feature( bytes_list = tf.train.BytesList(value=[value]) )
    
def _float_feature( value ):
    return tf.train.Feature( float_list = tf.train.FloatList(value=[value]) )
    
'''
Traceback (most recent call last):
  File "sagemaker_exercise.py", line 78, in <module>
    convert_mnist_fashion_dataset( train_images, train_labels, 'train', 'data' )
  File "sagemaker_exercise.py", line 63, in convert_mnist_fashion_dataset
    with tf.python_io.TFRecordWriter( filename ) as writer:
  File "/home/ec2-user/anaconda3/envs/tensorflow_p36/lib/python3.6/site-packages/tensorflow/python/lib/io/tf_record.py", line 218, in __init__
    compat.as_bytes(path), options._as_record_writer_options(), status)
  File "/home/ec2-user/anaconda3/envs/tensorflow_p36/lib/python3.6/site-packages/tensorflow/python/framework/errors_impl.py", line 548, in __exit__
    c_api.TF_GetCode(self.status.status))
tensorflow.python.framework.errors_impl.NotFoundError: data/train.tfrecords; No such file or directory
(tensorflow_p36) [ec2-user@ip-172-16-93-32 temp]$
'''

def convert_mnist_fashion_dataset( images, labels, name, directory ):
    _, height, width = images.shape
    
    filename = os.path.join( directory, name+'.tfrecords' )
    print(f'Writing {filename}' ) 
    with tf.python_io.TFRecordWriter( filename ) as writer:
        n_images = len( images )
        for index in range( n_images ):
            labels_int = int( labels[index] )
            image_raw  = images[index].tostring()
            example = tf.train.Example( features = tf.train.Features( feature={
                'height': _int64_feature( height ),
                'width': _int64_feature( width ),
                'channels': _int64_feature( 1 ),
                'label': _int64_feature( labels_int ),
                'image_raw': _bytes_feature( image_raw )
            } ))
            writer.write( example.SerializeToString() )
            
# Store TRRecords to S3
convert_mnist_fashion_dataset( train_images, train_labels, 'train', 'data' )
convert_mnist_fashion_dataset( test_images, test_labels, 'validation', 'data' )

# Model design

bucket = sagemaker.Session().default_bucket()
prefix = 'radix/mnist_fashion_tutorial'
role   = sagemaker.get_execution_role()

import boto3
from time import gmtime, strftime
from sagemaker.tensorflow import TensorFlow
from sagemaker.tuner import IntegerParameter, CategoricalParameter, CoutinuousParameter, HyperparameterTuner

# Build a TensorFlow model compatible with SageMaker
#   TensorFlow’s Estimator API https://www.tensorflow.org/guide/estimators
file_model = cnn_fashion_mnist.py

estimator = TensorFlow( entry_point          = 'file_model',
                        role                 = role,
                        input_mode           = 'Pipe',
                        training_steps       = 20000,
                        evaluation_steps     = 100,
                        train_instance_count = 1,
                        train_instance_type  = 'ml.c5.2xlarge',
                        base_job_name        = 'radix_mnist_fashion' )

# Enable hyperparameter tuning in SageMaker
#   Bayesian optimisation https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html
#   automatic model tuning https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html

# Define objective
objective_metric_name = 'loss'
objective_type = 'Minimize'
metric_definisions = [ {'Name': 'loss',
                        'Regex': 'loss = ([0-9\\.]+)'} ]

# Define hyperparameter ranges
hyperparameter_ranges = {
                            'learning_rate': CoutinuousParameter( 0.00001, 0.01 ),
                            'dropout_rate': CoutinuousParameter( 0.3, 1.0 ),
                            'nw_depth': IntegerParameter( 1, 4 ), 
                            'optimizer_type': CategoricalParameter( ['sgd', 'adam'] )
                        }
                        
# Initialize SageMaker's hyperparametertuner
tuner = HyperparameterTuner( estimator,
                             objective_metric_name,
                             hyperparameter_ranges,
                             metric_definitions,
                             max_jobs = 16,
                             max_parallel_jobs = 4,
                             objective_type = objective_type )

# cnn_fashion_mnist.py
#   https://github.com/radix-ai/sagemaker-tensorflow-tutorial/blob/master/cnn_fashion_mnist.py

train_data = 's3://sagemaker-eu-central-1-959924085179/radix/mnist_fashion_tutorial/data/mnist/train.tfrecords'
eval_data  = 's3://sagemaker-eu-central-1-959924085179/radix/mnist_fashion_tutorial/data/mnist/validation.tfrecords'

tuner.fit( {'train': train_data, 'eval': eval_data}, logs=False )

# Putting your model into production
#   sagemaker.tensorflow.estimator.TensorFlow implementation
#     https://sagemaker.readthedocs.io/en/latest/sagemaker.tensorflow.html

model_artifacts_location = f's3://{bucket}/{prefix}/artifacts'

# This is the same as the lines above
estimator = TensorFlow( entry_point          = 'file_model',
                        role                 = role,
                        input_mode           = 'Pipe',
                        training_steps       = 20000,
                        evaluation_steps     = 100,
                        train_instance_count = 1,
                        train_instance_type  = 'ml.c5.2xlarge',
                        base_job_name        = 'radix_mnist_fashion' )

predictor = estimator.deploy( initial_instance_count=1, instance_type='ml.m4.xlarge' )

random_image_data = np.random.rand( 28, 28, 1 )
predictor.predict( random_image_data )

# (EOF)