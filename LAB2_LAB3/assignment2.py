import wfdb
import tensorflow as tf
from tensorflow import *
from keras import *
from keras.layers import *
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

def getDataSet(number, X_data,label,label_point):
    record = wfdb.rdrecord("./mit-bih-arrhythmia-database-1.0.0/"+ number,channel_names=['MLII'] )#, channel_names=['MLII'] 
    data = record.p_signal.flatten()
    annotation = wfdb.rdann("./mit-bih-arrhythmia-database-1.0.0/" + number, 'atr')
    Rlocation = annotation.sample  
    Rclass = annotation.symbol
    X_data.append(data)
    label.append(Rclass)
    label_point.append(Rlocation)
    return X_data,label,label_point

def loadData():
    numberSet = ['100', '101', '103', '105', '106', '107', '108', '109', '111', '112', '113', '114', '115',
                '116', '117', '119', '121', '122', '123', '124', '200', '201', '202', '203', '205', '208',
                '210', '212', '213', '214', '215', '217', '219', '220', '221', '222', '223', '228', '230',
                '231', '232', '233']#43 '234'
    dataSet = []
    label = []
    label_point = []
    for n in numberSet:
        dataSet,label,label_point = getDataSet(n, dataSet,label,label_point)
    return dataSet,label,label_point

def Preparation_data():
    print('start load data!')
    dataSet,label,label_point = loadData()
    print('load data done!')
    see_data_num = 0
    save_ecg_all = []
    save_ecg_label_all = []
    while see_data_num < 42:
        delete_point = []
        save_ecg=[]
        save_ecg_label=[]
        n=0
        v=0
        print(see_data_num)
        print('raw label Quantity', len(label[see_data_num]))#2094
        print('raw label_point Quantity', len(label_point[see_data_num]))#2094
        for i in range(len(label[see_data_num])):
            if (label[see_data_num][i] == 'N') :
                n+=1
            elif (label[see_data_num][i] == '+') :
                delete_point.append(i)
            else:
                v+=1
        label_point[see_data_num] = np.delete(label_point[see_data_num], delete_point)
        label[see_data_num] = np.delete(label[see_data_num], delete_point)
        print('new label Quantity', len(label[see_data_num]))
        print('new label_point Quantity', len(label_point[see_data_num]))
        see_data_label_point = label_point[see_data_num]
        for i in range(3,len(see_data_label_point)-1):
            cut_ecg = dataSet[see_data_num][see_data_label_point[i]-125 : see_data_label_point[i]+125]
            save_ecg.append(cut_ecg)
        print(len(save_ecg))
        print(len(save_ecg[0]))
        save_ecg = np.array(save_ecg)
        save_ecg_label = np.array(label[see_data_num])
        save_ecg_label = save_ecg_label[3:-1]
        save_ecg_label = save_ecg_label.reshape(-1,1)
        save_ecg = save_ecg.reshape(save_ecg.shape[0], save_ecg.shape[1], 1)
        print('save_ecg_label.shape', save_ecg_label.shape)
        print('save_ecg.shape', save_ecg.shape)
        save_ecg_label = [0 if label == 'N' else 1 for label in save_ecg_label]
        save_ecg_label = np.array(save_ecg_label)
        for i in range(len(save_ecg_label)):
            save_ecg_label_all.append(save_ecg_label[i])
        for i in range(len(save_ecg)):
            save_ecg_all.append(save_ecg[i])
        see_data_num += 1
    save_ecg_label_array = np.array(save_ecg_label_all)
    save_ecg_label_array = save_ecg_label_array.reshape(-1,1)
    print(save_ecg_label_array.shape)
    save_ecg_array = np.array(save_ecg_all)
    print(save_ecg_array.shape)
    return save_ecg_array, save_ecg_label_array
    
def cnn(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    #=======================================================LAB2_1 model
    model = Sequential()
    model.add(Conv1D(filters=32, kernel_size=3, activation='relu', input_shape=(250,1)))#You can also change this just to let you know the input size
    '''
    add some layers
    '''
    history = model.fit(X_train, y_train, epochs=25, batch_size=64, validation_split=0.1)
    #=======================================================
    model.save('MIT_BIH.h5')

    y_pred = model.predict(X_test)
    y_pred_binary = (y_pred > 0.5).astype(int)

    print(classification_report(y_test, y_pred_binary))

    accuracy = accuracy_score(y_test, y_pred_binary)
    print(f'Accuracy: {accuracy * 100:.2f}%')
    confusion = confusion_matrix(y_test, y_pred_binary)

    plt.figure(figsize=(8, 6))
    sns.heatmap(confusion, annot=True, fmt='d', cmap='Blues', xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'])
    plt.xlabel('Predicted')
    plt.ylabel('Ground Truth')
    plt.title('Confusion Matrix')
    plt.show()
    
if __name__ == '__main__':
    save_ecg, save_ecg_label = Preparation_data()
    cnn(save_ecg,save_ecg_label)
