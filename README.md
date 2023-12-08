# Biomedical TA

### LAB1 
#### 1.Dynamic plot ecg signal 
#### 2.Dynamic plot ppg signal

-------------------------------------------------------------------------------------------------------------------------------------------
### LAB2 
#### 1.Fill some layers of the model on your own
#### 2.Draw the training and validation loss
![](https://drive.google.com/u/2/uc?id=1TLUkFnfZUyaOOd_AMm_YAN70kCz2YZxu&export=download)

-------------------------------------------------------------------------------------------------------------------------------------------
### LAB3 
#### 1.Transfer MIT_BIH.h5 to MIT_BIH.tflite write the code（change_model.py write on your own）
#### 2.Write function to load tflite model

-------------------------------------------------------------------------------------------------------------------------------------------
### LAB4 
#### 1.Shrink tflite model to smaller size 
#### 2.Compare two model size MIT_BIH.tflite and MIT_BIH_quant.tflite
#### 3.Try the model on the embedded system and run the code
<!-- ![](https://drive.google.com/u/2/uc?id=1aBxOBEFG0VTbf5kTwyeSXopGHOxQ39M7&export=download) -->
<img src="https://drive.google.com/u/2/uc?id=1aBxOBEFG0VTbf5kTwyeSXopGHOxQ39M7&export=download" width="50%">

-------------------------------------------------------------------------------------------------------------------------------------------

### Download representative dataset
```bash
$ sh download.sh
```
### Create a new environment
```bash
$ conda create --name DL python=3.9
```
### Install the required packages
```bash
$ pip install -r requirements.txt
```
### Usage 
```bash
$ python3 ecg_ppg.py
$ python3 cnn_train.py
$ python3 cnn_predict.py
$ python3 change_model.py
```
### Slide link(NYCU)
https://docs.google.com/presentation/d/1T-oer6ydYy4zR05BcprUr-sJW5H7oNyNwlYxdRj5aRs/mobilepresent?slide=id.g260a8d390d5_0_373
### Github
https://github.com/mlcommons/tiny/tree/master
