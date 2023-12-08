import tensorflow as tf
import wfdb
import numpy as np

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
    numberSet = ['234']
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
    delete_point = []
    n=0
    v=0
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
    #===================================================================find not normal
    # for i in range(len(label[see_data_num])):
    #     if (label[see_data_num][i] != 'N') :
    #         print('===',i)
    #===================================================================
    see_data_label_point = label_point[see_data_num]
    i = 3
    j = 230
    model_input = dataSet[see_data_num][see_data_label_point[j]-125 : see_data_label_point[j]+125]
    model_input = model_input.reshape(-1,250,1)
    # print('==++',model_input.shape)
    ground_truth_normal = label[0][i]
    ground_truth_not_normal = label[0][j]
    print('GT_normal: ',ground_truth_normal)
    print('GT_not_normal: ',ground_truth_not_normal)
    print('NORMAL: ',n)
    print('NOT NORMAL: ',v)
    return model_input,ground_truth_normal

if __name__ == '__main__':
    model_path = 'MIT_BIH.h5'
    loaded_model = tf.keras.models.load_model(model_path)
    loaded_model.summary()
    model_input,ground_truth_normal = Preparation_data()
    print(model_input.shape)
    print(model_input)
    predictions = loaded_model.predict(model_input)
    print('-----',predictions)
    if predictions > 0.1:
        print('Not normal caution caution caution!!!!!')
    else:
        print('Normal heart rate signal')