# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:32:14 2020

@author: Roman
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# this site provides data per state such as Absentee Voting rules
base_site = "https://www.usvotefoundation.org/vote/state-elections/state-voting-laws-requirements.htm"
r = requests.get(base_site)
r.status_code

# get the HTML content from the webpage
html = r.content

# since tickers in a table can't be scraped using pandas, will update df using BS
dfs = pd.read_html(html)
voting_options = dfs[0]

soup = BeautifulSoup(html, 'lxml')
# The main table on the page
table = soup.find_all("table")[0]

# When ticker in a cell, we get None, when empty cell we get N/A
temp_list = []
for n in range(3,22,2):
    tbl_col = [row.contents[n].string for row in table.find_all('tr')]    
    for n in tbl_col[1:]:
        temp_list.append(1) if n== None else temp_list.append(0)
    voting_options[tbl_col[0]] = temp_list
    temp_list = []
    
# since All-Mail Voting column in many cases doesn't tell which elections
# it is allowed to vote, need to get rid of it
voting_options.drop(['All-Mail Voting'],axis=1,inplace=True)

# print(voting_options.columns)