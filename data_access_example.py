# -*- coding: utf-8 -*-
import pandas as pd


singersdf = pd.DataFrame()
singersdf['singer'] = pd.Series([
                        'The Rolling Stones',
                        'Beatles',
                        'Guns N\' Roses',
                        'Metallic'])
singersdf['song'] = pd.Series([
                        'Satisfaction',
                        'Let It Be',
                        'Don\'t Cry',
                        'Nothing Else Matters'])
print(singersdf)
singersdf.to_csv('data_acces.csv')

result = pd.read_csv('data_access.csv')
print('')
print(list(result['song']))
