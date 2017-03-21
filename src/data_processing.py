import pandas as pd
import time
# We get some mixed type and low memory warnings, this supresses them
import warnings
warnings.filterwarnings('ignore')

def drop_poorly_formatted_patents(df):
    '''Drop rows from dataframe if 'Patent' column
    errors when converted to numeric'''
    patents = pd.to_numeric(df.Patent, errors='coerce')
    return df[patents.isnull() ==  False]

if (__name__ == "__main__"):
    print("--- LOADING PATENT CLASS DATASET"); t_begin = time.time()
    patent_class = pd.read_csv('data/class.csv')
    #kept just 'Primary' class

    #THIS DIDN"T WORK. NEED TO UPDATE
    patent_class_prim_only = patent_class[patent_class.Prim == 1]
    patent_class_prim_only = patent_class_prim_only[['Patent', 'Class', 'SubClass']]
    patent_class_prim_only = drop_poorly_formatted_patents(patent_class_prim_only)
    print("--- [time elapsed: {}]".format(time.time()-t_begin))

    print("--- LOADING CITATIONS DATASET"); t_begin = time.time()
    citation = pd.read_csv('data/citation.csv')
    citation = citation[['Patent', 'Citation']]
    citation = drop_poorly_formatted_patents(citation)
    print("--- [time elapsed: {}]".format(time.time()-t_begin))

    print("--- LOADING PATENT GRANT DATA"); t_begin = time.time()
    patent = pd.read_csv('data/patent.csv')
    patent = patent[['Patent', 'GDate', 'GYear']]
    patent = drop_poorly_formatted_patents(patent)
    #drop 2013 data (incomplete)
    patent =  patent[patent.GYear != 2013]
    print("--- [time elapsed: {}]".format(time.time()-t_begin))

    print("--- MERGING DATA"); t_begin = time.time()
    intermediate = pd.merge(patent_class_prim_only, citation, on='Patent')
    merged = pd.merge(intermediate, patent, on='Patent')
    print("--- [time elapsed: {}]".format(time.time()-t_begin))

    print("--- SAVING"); t_begin = time.time()
    merged.to_csv('data/processed_patent.csv')
    print("--- [time elapsed: {}]".format(time.time()-t_begin))
