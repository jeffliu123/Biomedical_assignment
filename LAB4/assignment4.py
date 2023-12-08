import tensorflow as tf
import numpy as np
import glob
import os 
import pandas as pd

def representative_dataset_generator():
    '''
    here
    '''

if __name__ == '__main__':
    model_path = 'MIT_BIH.h5'
    model = tf.keras.models.load_model(model_path)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    tflite_model_path = 'MIT_BIH.tflite'
    with open(tflite_model_path, 'wb') as f:
        f.write(tflite_model)
    print("TensorFlow Lite model saved to", tflite_model_path)

    # Create a new converter for quantization
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    '''
    here
    '''
