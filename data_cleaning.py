# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 17:48:39 2020

@author: Roman
"""

import pandas as pd
#import numpy as np

p_state_original =  pd.read_csv('source_data/president_state.csv', index_col='state')
p_state = p_state_original.copy()
p_state = p_state.drop("United States")

p_county_original =  pd.read_csv('source_data/president_county.csv')
p_county = p_county_original.copy()

p_county_cand_oryginal =  pd.read_csv('source_data/president_county_candidate.csv')
p_county_cand = p_county_cand_oryginal.copy()


#state vs counties total check
#state current vs total check

#check for missing values
#print(p_state.head())

# print(p_state.loc['Florida', 'total_votes'])
#print(p_state.loc['Florida', :])
#print(p_state.columns)
#print(p_state.dtypes)

#print(p_state.values)
# print(p_state.shape)
# a=p_state.total_votes
# b=p_state["total_votes"]
# c=p_state[["total_votes"]]
# print(type(a))
# print(type(b))
# print(type(c))

#print(p_county.head(3))

#county_votes = ['county', 'total_votes']
#print(p_county[county_votes].head())

#print(p_county.iloc[1])

#print(p_county.iloc[0:3,2])

#print(p_county.iloc[:,[3,1]]) #all rows, fourth and second column


# print(p_county_cand.sort_values('total_votes',ascending=0))
print('''------------------------------
------Total votes check-------
------------------------------''')
print('County per candidate presidential sum:',sum(p_county_cand.loc[:,'total_votes']))
print('State presidential sum:',sum(p_state.iloc[:,0]))

print('County presidential current sum:',sum(p_county.iloc[:,2]))
print('County presidential total sum:',sum(p_county.iloc[:,3]))


print('''------------------------------
------Counties number check-------
------------------------------''')
# print(p_county.county.value_counts())
print('Count distinct counties:', p_county.county.nunique())
print('Count distinct counties per cand:', p_county_cand.county.nunique())

print('''------------------------------
------Current vs total check-------
------------------------------''')

p_county['diff'] = p_county['total_votes'] - p_county['current_votes']

pd.set_option('display.max_columns', 10, 'display.max_rows', 5)
aaaaa = p_county[p_county["diff"]<0]









