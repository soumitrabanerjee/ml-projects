import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def data_analysis(required_columns_df):
    var = required_columns_df.describe()['medals']

    data = required_columns_df
    sb.lmplot(x='athletes', y='medals', data=data, fit_reg=True, ci=None)
    plt.show()
    sb.lmplot(x='age', y='medals', data=data, fit_reg=True, ci=None)
    plt.show()
    data.plot.hist(y='medals')
    plt.show()