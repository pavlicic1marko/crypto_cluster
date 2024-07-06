import os
import math
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from tslearn.clustering import TimeSeriesKMeans
from sklearn.preprocessing import MinMaxScaler


directory = '.'
mySeries = []
clusters = 3


# create Change column by subtracting open from close
namesofMySeries = []
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        df = pd.read_csv(filename)
        open_values = np.array(df['Open'].T)
        close_values = np.array(df['Close'].T)
        change_values = open_values-close_values
        df.insert(1,"Change",change_values,True)
        df = df.loc[:,["Date","Change"]]
        df.set_index("Date",inplace=True)
        # ,set the date columns as index
        df.sort_index(inplace=True)
        # and lastly, ordered the data according to our date index

        # While we are at it I just filtered the columns that we will be working on
        print(df)
        mySeries.append(df)
        namesofMySeries.append(filename.split('_')[0])








print(len(namesofMySeries))
series_lengths = {len(series) for series in mySeries}
print(series_lengths)

for i in namesofMySeries:
    print(i)

for i in range(len(mySeries)):
    scaler = MinMaxScaler()
    mySeries[i] = MinMaxScaler().fit_transform(mySeries[i])
    mySeries[i]= mySeries[i].reshape(len(mySeries[i]))


print("max: "+str(max(mySeries[0]))+"\tmin: "+str(min(mySeries[0])))
print(mySeries[0][:5])



# A good rule of thumb is choosing k as the square root of the number of points in the training data set in kNN

km = TimeSeriesKMeans(n_clusters=4, metric="dtw")

labels = km.fit_predict(mySeries)


fancy_names_for_labels = [f"Cluster {label}" for label in labels]
test1=pd.DataFrame(zip(namesofMySeries,fancy_names_for_labels),columns=["Series","Cluster"]).sort_values(by="Cluster").set_index("Series")
print(test1)