import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def analyse_data(required_columns_df):
    data = required_columns_df
    sb.lmplot(x='athletes', y='medals', data=data, fit_reg=True, ci=None)
    plt.show()
    sb.lmplot(x='age', y='medals', data=data, fit_reg=True, ci=None)
    plt.show()
    data.plot.hist(y='medals')
    plt.show()