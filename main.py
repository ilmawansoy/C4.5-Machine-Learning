import pandas as pd
import numpy as np
import json
from c45 import *

def classify(dframe):
    pop = dframe['popularity']
    ls = []
    for i in range(0,len(pop)):
        v = pop[i]
        if v < 45:
            ls.append('Unpopular')
        elif v > 45 and v < 90:
            ls.append('Moderate')
        elif v > 90 and v < 150:
            ls.append('Popular')
        elif v > 150:
            ls.append('Very Popular')
    dframe['popularity_category'] = ls
    return dframe

def fixDf(dframe):
    genre = dframe['genres']
    print(type(genre))
    ls = []
    for i in genre:
        v = json.loads(i)
        if len(v) != 0:
            ls.append(v[0].get('name'))
        else:
            ls.append('None')
    dframe['genres'] = ls
    return dframe

if __name__ == '__main__':
    df = pd.read_csv('movies.csv')
    df = classify(df)
    ls = df.to_dict('list')
    print(ls.keys())
    df = fixDf(df)
    # print(df['genres'])
    print(gain(ls,'genres','popularity_category'))
