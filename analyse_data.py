import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv('data/teams.csv')
    sb.lmplot(x='athletes', y='medals', data=data, fit_reg=True, ci=None)
    plt.show()
    sb.lmplot(x='age', y='medals', data=data, fit_reg=True, ci=None)
    plt.show()
    data.plot.hist(y='medals')
    plt.show()