from FIFA_k_means_clustering.ml_process import ml_process
from data_cleaning import get_clean_data

if __name__ == '__main__':
    data_path = "data/players_22.csv"
    clean_data = get_clean_data(data_path)
    ml_process(clean_data)