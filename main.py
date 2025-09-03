from data_cleaning import get_clean_data
from data_analysis import data_analysis
from ml_process import ml_process

if __name__ == '__main__':
    train_spark_data, test_spark_data, required_columns_spark_df = get_clean_data()
    train_pandas_df = train_spark_data.toPandas()
    test_pandas_df = test_spark_data.toPandas()

    print(train_pandas_df)
    print(test_pandas_df)

    required_columns_pandas_df = required_columns_spark_df.toPandas()
    # data_analysis(required_columns_pandas_df)
    ml_process(train_pandas_df, test_pandas_df)

