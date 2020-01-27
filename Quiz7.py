# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:22:44 2019

@author: Steven Solis
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_validate #, cross_val_score, train_test_split
from sklearn import preprocessing

dset = pd.read_csv('train.csv')

sns.countplot(dset['Age'])
plt.figure()

dset = dset.fillna({"Age": "C"})

print('The null values:', dset.isnull().sum() )

le_sex = preprocessing.LabelEncoder()
le_sex.fit(["male", "female"])
dset['Sex'] = le_sex.transform(dset['Sex'])

sexnew = dset[['Sex']]

sns.countplot(dset['Sex'])


'''# or simply:
dset['Sex'].replace(['male','female'], [0,1], inplace=True)
sns.countplot(dset['Sex'])

'''



















