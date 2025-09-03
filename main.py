# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from data_cleaning import data_cleaning_process
from analyse_data import analyse_data

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    train_data, test_data, required_columns_df = data_cleaning_process()
    print(train_data)
    print(test_data)
    required_columns_pandas_df = required_columns_df.toPandas()
    analyse_data(required_columns_pandas_df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
