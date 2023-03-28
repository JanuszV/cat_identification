# %%
# This demo will take you through the steps of running an "out-of-the-box" TensorFlow 2 compatible
# detection model on a collection of images. More specifically, in this example we will be using
# the `Saved Model Format <https://www.tensorflow.org/guide/saved_model>`__ to load the model.
import datetime, shelve
import tensorflow as tf
import collections
import glob
import six
import numpy as np
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor
import matplotlib.pyplot as plt
import warnings
import time
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils

# %%
# Load the model
# ~~~~~~~~~~~~~~
# Next we load the downloaded model
global detect_fn, detect_fn2

PATH_TO_SAVED_MODEL = "C:/Users/barto/Desktop/Third Graph/inference_graph/saved_model" # śćieżka do modelu nr 1
PATH_TO_SAVED_MODEL2 ="C:/Users/barto/Desktop/Identyfikacja kota 2/inference_graph/saved_model" # śćieżka do modelu nr 2

print('Loading model...', end='')
start_time = time.time()

# Load saved model and build the detection function
detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)

end_time = time.time()
elapsed_time = end_time - start_time
print('Done! Took {} seconds'.format(elapsed_time))

print('Loading model nr 2...', end='')
start_time = time.time()

# Load saved model and build the detection function
detect_fn2 = tf.saved_model.load(PATH_TO_SAVED_MODEL2)

end_time = time.time()
elapsed_time = end_time - start_time
print('Done! Took {} seconds'.format(elapsed_time))
