import pandas as pd
import numpy as np

def get_subset(df, column, selector):
    '''Return subset of dataframe for given column name (string) and
    given subset criterion'''
    return df[df[column] == selector]

 year_dfs = {g: get_subset(patent, 'GYear', g) for g in patent.GYear.unique()}

def get_class_subset(df, class_number):
    '''Return subset of dataframe where Class matches class_number '''
    return df[df.Class == class_number]

year_class335_dfs = {g: get_class_subset(year_dfs[g], 335) for g in year_dfs}

## Number of citations within class 335, annually
[year_class335_dfs[g].shape[0] for g in year_class335_dfs]

#export dataframes

#get max pagerank
for p in pr:
    if pr[p] == max(pr.values())

import operator

def get_most_influential(pr_dictionary):
    '''Return patent with highest pagerank'''
    return max(pr.iteritems(), key=operator.itemgetter(1))[0]

def most_influential_over_time(dict_of_dfs):
    '''Get patent with highest pagerank for each year'''
    class_pageranks = []
    for g in patent.GYear.unique():
        G = nx.from_pandas_dataframe(dict_of_dfs[g], source='Patent', target='Citation')
        pr = nx.pagerank(G, alpha=0.9)
        class_pageranks.append((g, get_most_influential(pr)))
    return class_pageranks

## make graph of total
G_total = nx.from_pandas_dataframe(patent, source='Patent', target = 'Citation')


year_bins = [patent.GYear.unique()[i:i + 5] for i in range(0, len(patent.GYear.unique()), 5)]
year_bins = year_bins[:-1]

year_bins_df = {x: patent[patent.GYear in set(year_bins)] for x in year_bins}

#drop citations to non-utility patents
patent_edgelist = patent[['Patent', 'Citation', 'GYear', 'Class', 'SubClass']]
patent_clean = pd.umeric(patent_edgelist.Citation, errors='coerce')
patent_edgelist = patent_edgelist[patent_clean.isnull() ==  False]

##create sub-dfs for visualization
df1 = patent_edgelist[patent_edgelist.GYear < 1980]
df2 = patent_edgelist[(patent_edgelist.GYear > 1979) & (patent_edgelist.GYear < 1985)]
df3 = patent_edgelist[(patent_edgelist.GYear > 1984) & (patent_edgelist.GYear < 1990)]
df4 = patent_edgelist[(patent_edgelist.GYear > 1989) & (patent_edgelist.GYear < 1995)]
df5 = patent_edgelist[(patent_edgelist.GYear > 1994) & (patent_edgelist.GYear < 2000)]
df6 = patent_edgelist[(patent_edgelist.GYear > 1999) & (patent_edgelist.GYear < 2005)]

df1 = df1[['Patent', 'Citation']]
df2 = df2[['Patent', 'Citation']]
df3 = df3[['Patent', 'Citation']]
df4 = df4[['Patent', 'Citation']]
df5 = df5[['Patent', 'Citation']]
df6 = df6[['Patent', 'Citation']]

df1.to_csv('edgelist_1975.txt', sep='\t', header=False, index=False)
df2.to_csv('edgelist_1980.txt', sep='\t', header=False, index=False)
df3.to_csv('edgelist_1985.txt', sep='\t', header=False, index=False)
df4.to_csv('edgelist_1990.txt', sep='\t', header=False, index=False)
df5.to_csv('edgelist_1995.txt', sep='\t', header=False, index=False)
df6.to_csv('edgelist_2000.txt', sep='\t', header=False, index=False)
