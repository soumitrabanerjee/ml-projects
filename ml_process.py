import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

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


