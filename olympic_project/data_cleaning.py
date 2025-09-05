from pyspark.sql import SparkSession
from pyspark.sql.functions import corr
import yaml
import os
import glob
import shutil

def rename_part_file(output_dir, desired_file_name):
    try:
        # Find the part file
        part_file = glob.glob(os.path.join(output_dir, 'part-*.csv'))[0]
        # Rename (move) the part file
        shutil.move(part_file, desired_file_name)
        # Optionally, remove the empty output directory
        shutil.rmtree(output_dir)
    except (IndexError, FileNotFoundError):
        print(f"No part file found in directory: {output_dir}")

def write_to_csv(df, output_path):
    df.coalesce(1).write.format('csv').option('header', 'true').mode('overwrite').save(output_path)

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def get_clean_data(data_path, config_path):
    spark = SparkSession.builder.appName('data_cleaning').getOrCreate()
    configs = load_config(config_path)

    input_data = spark.read.format('csv'). \
        option('header', 'true'). \
        option('inferSchema', 'true'). \
        load(data_path)

    # select relevant columns for analysis
    selected_columns_df = input_data. \
        select('team', 'country', 'year', 'athletes', 'age', 'prev_medals', 'medals')

    selected_columns_df.show()
    print('Total Records: ' + str(selected_columns_df.count()))

    # find strong correlations between medals and other columns
    get_strong_corr = selected_columns_df.select(corr('age', 'medals'),
                               corr('prev_medals', 'medals'),
                               corr('athletes', 'medals'),
                               corr('year', 'medals'))

    get_strong_corr.show(1, False)

    clean_data = selected_columns_df.na.drop()
    print('Total Records after dropping nulls: ' + str(selected_columns_df.na.drop().count()))

    # split the data into training and test sets
    train = clean_data.filter("year < 2012")
    print('Total Records in training set: ' + str(train.count()))
    # save the results to a CSV file
    train_dir = configs['train_output_dir']
    write_to_csv(train, train_dir)
    train_desired_name = configs['train_desired_name']
    rename_part_file(train_dir, train_desired_name)

    # split the data into training and test sets
    test = clean_data.filter("year >= 2012")
    print('Total Records in test set: ' + str(test.count()))

    train_data_percentage = round(train.count() / clean_data.count(), 2) * 100
    test_data_percentage = round(test.count() / clean_data.count(), 2) * 100

    print(f'Train vs Test Data Split Percentage: {train_data_percentage}% : {test_data_percentage}%')
    # save the results to a CSV file
    test_dir = configs['test_output_dir']
    write_to_csv(test, test_dir)
    test_desired_name = configs['test_desired_name']
    rename_part_file(test_dir, test_desired_name)

    return train, test, selected_columns_df




