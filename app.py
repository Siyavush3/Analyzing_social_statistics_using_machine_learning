import csv
import json
from flask import Flask
import tensorflow as tf

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

app = Flask(__name__)

@app.route('/history')
def graph():
    return cor(df['Corn'],df['Meal'])




mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

df = pd.read_csv('1.csv')




def family_palov_index(meat,carrot,rise,oil,onion):
    index=0
    index= meat*0.7 + rise + carrot + oil*0.3 + onion*0.3
    return index

def medium(data_arrov):
    for i in range(len(data_arrov)):
        medium += data_arrov[i]
    return medium


def year_heals_eating(fruits,milk_prod,meat,eggs,sugar,fish,oil):
    heals_eating_index = medium(fruits)*100 + medium(milk_prod)*325 + medium(meat)*73 + eggs*26 + sugar*24 + fish*22 + oil*12
    return heals_eating_index

def cor(d1,d2):
    for k in range( len(d1)):
        if d1[k]>d2[k]:
            cor_arr[k]=round(d1[k]/d2[k])
        else:
            cor_arr[k]=round(d2[k]/d1[k])
    cor_data1 = medium(cor_arr)
    if medium(d1)>medium(d2):
        cor_data2 = medium(d1)/medium(d2)
    else:
        cor_data2 = medium(d2)/medium(d1)

    if cor_data1 > cor_data2 :
        return cor_data1/cor_data2
    else:
        return cor_data2/cor_data1


if __name__ == '__main__':
    
    app.run( host='0.0.0.0', port=5000)
	
