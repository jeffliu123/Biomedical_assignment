'''
Author: jeffliu123 jeffliuhappy0228@gmail.com
Date: 2023-12-09 01:02:38
LastEditors: jeffliu123 jeffliuhappy0228@gmail.com
LastEditTime: 2023-12-09 14:38:17
FilePath: /Biomedical_assignment/LAB4/assignment4.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
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
