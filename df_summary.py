# Libraries:
import pandas as pd
import seaborn as sns


def check_df(dataframe, head=5):
    print('Head: ')
    print(dataframe.head(head))
    print('Tail: ')
    print(dataframe.tail(head))
    print('Shape: ')
    print(dataframe.shape)
    print('Columns: ')
    print(dataframe.columns)
    print('Index: ')
    print(dataframe.index)
    print('NA: ')
    print(dataframe.isnull().sum())
    print('Type: ')
    print(dataframe.dtypes)
    print('Quantiles: ')
    print(dataframe.quantile([0,0.05,0.5,0.95,0.99,1]).T)



# Test
df = sns.load_dataset('titanic')
check_df(df)
