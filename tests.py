# -*- coding: utf-8 -*-
"""
Created on Sat May 22 18:16:03 2021

@author: Usuario
"""

# modifica la lista inicial
a = [1, 2, 3, 4]
a[0] = 2

# uso copy
a = [1, 2, 3, 4]
a[0] = a.copy(2)

#%%

import numpy as np
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')

titanic.groupby('sex')[['survived']].mean()
titanic.pivot_table('survived', index='sex', columns='class')

summary_table_1 = titanic.describe()
summary_table_1 = summary_table_1\
    .to_html()\
    .replace('<table border="1" class="dataframe">','<table class="table table-striped">')