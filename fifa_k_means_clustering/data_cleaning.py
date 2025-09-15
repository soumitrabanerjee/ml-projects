from pyspark.sql import SparkSession

def get_clean_data(data_path):
    spark = SparkSession.builder.appName('data_cleaning').getOrCreate()

    input_data = spark.read.format('csv'). \
        option('header', 'true'). \
        option('inferSchema', 'true'). \
        load(data_path)

    # select relevant columns for analysis
    selected_columns = input_data.select('overall', 'potential', 'wage_eur', 'value_eur', 'age')

    clean_data = selected_columns.na.drop()

    clean_data.show()

    described_info = clean_data.describe()
    print(described_info.show())

    return clean_data.toPandas()