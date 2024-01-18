<!--
 * @Author: jeffliu123 jeffliuhappy0228@gmail.com
 * @Date: 2023-12-09 13:59:33
 * @LastEditors: jeffliu123 jeffliuhappy0228@gmail.com
 * @LastEditTime: 2024-01-18 22:03:27
 * @FilePath: /Biomedical_assignment/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# Biomedical TA

### LAB1 
#### 1.Plot ecg signal 
#### 2.Plot ppg signal
#### 3.Calculate Pulse Rate

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
$ python3 assignment1.py
$ python3 assignment2.py
$ python3 cnn_predict.py
$ python3 assignment4.py
```
### Slide link(NYCU)
https://docs.google.com/presentation/d/1T-oer6ydYy4zR05BcprUr-sJW5H7oNyNwlYxdRj5aRs/mobilepresent?slide=id.g260a8d390d5_0_373
### Github
https://github.com/mlcommons/tiny/tree/master
