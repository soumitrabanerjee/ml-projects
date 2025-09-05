import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np

def ml_process(train_pandas_df, test_pandas_df):
    print(train_pandas_df.shape)
    print(test_pandas_df.shape)

    reg = LinearRegression()

    predictors = ['athletes', 'prev_medals']
    target = 'medals'

    reg.fit(train_pandas_df[predictors], train_pandas_df[target])

    predictors = reg.predict(test_pandas_df[predictors])
    test_pandas_df["predictions"] = predictors
    test_pandas_df.loc[test_pandas_df['predictions'] < 0, 'predictions'] = 0
    test_pandas_df['predictions'] = test_pandas_df['predictions'].round().astype(int)

    print(test_pandas_df)

    error = mean_absolute_error(test_pandas_df['medals'], test_pandas_df['predictions'])
    print('Mean Absolute Error: ' + str(error))

    usa_prediction = test_pandas_df[test_pandas_df['team'] == 'USA']
    print(usa_prediction)

    india_prediction = test_pandas_df[test_pandas_df['team'] == 'IND']
    print(india_prediction)

    errors = (test_pandas_df['medals'] - test_pandas_df['predictions']).abs()
    print(errors)

    error_by_team = errors.groupby(test_pandas_df['team']).mean()
    print(error_by_team)

    medals_by_team = test_pandas_df['medals'].groupby(test_pandas_df['team']).mean()

    error_ratio = error_by_team / medals_by_team
    error_ratio = error_ratio[~pd.isnull(error_ratio)]
    print('Error Ratio: ', error_ratio)

    error_ratio = error_ratio[np.isfinite(error_ratio)]
    print('Error Ratio after removing infinite values: \n', error_ratio)

    error_ratio.plot.hist()
    # plt.show()
    sorted_data = error_ratio.sort_values(ascending=False)
    print('sorted data\n', sorted_data)