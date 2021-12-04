import pandas as pd
import numpy as np


def save_sart_files_as_csv(sart_file_names):
    sart_csv_list = []

    for file_name in sart_file_names:
        file_path = "../data/data/" + file_name
        fin = open(file_path, "rt")
        fout = open("out.txt", "wt")

        for line in fin:
            fout.write(' '.join(line.split()))
            fout.write('\n')
        fin.close()
        fout.close()

        account = pd.read_csv("out.txt", delimiter= ' ', error_bad_lines=True)
        csv_name = file_name[:-4] + ".csv"
        account.to_csv("../data/csv_files/" + csv_name, index=None)
        sart_csv_list.append(csv_name)

    return sart_csv_list

def parse(folder_name):
    path = "../data/" + folder_name
    main_data_file = path + "/data.csv"

    main_data = pd.read_csv(main_data_file)
    main_data = main_data[list(main_data)[19:-3]]
    main_data = main_data.dropna()

    # personality_names = ['openness', 'conscientiousness', 'extroversion', 'agreeableness', 'neuroticism']
    personality_names = list(main_data)[:5]
    sart_file_colm = list(main_data)[6]
    personality_data = main_data[personality_names]
    sart_file_names = main_data[sart_file_colm]
    sart_csv_list = save_sart_files_as_csv(sart_file_names)

    return personality_data , sart_csv_list