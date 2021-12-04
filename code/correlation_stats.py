import pandas as pd

def get_correlation_stats(file_name):
    correlation_scores = []

    path = "../processed_data/" + file_name

    # read file from path
    dataFrame = pd.read_excel(path)
    print(dataFrame)

    # print all columns

    # calculate correlation scores

    return correlation_scores