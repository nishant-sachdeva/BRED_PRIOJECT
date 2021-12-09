import pandas as pd
import numpy as np

def get_score(file_name):
    file_path = "../data/csv_files/" + file_name
    dataFrame = pd.read_csv(file_path)
    dataFrame = dataFrame.dropna()

    response_times = dataFrame.iloc[:, -1]
    responses = dataFrame.iloc[:,-2].value_counts(sort=False)

    average_resoponse_time = response_times.mean()
    average_correctness = (responses[1]*100) / (responses[1] + responses[0])

    return average_resoponse_time, average_correctness


personalityAverage = []
def get_personality_averages(personality_data):
    data_desc = personality_data.describe()
    print(data_desc)
    return

def calculate_scores(personality_data, sart_csv_list):
    #  we have the personality data, sart_csv_list 
    # personality data => pandas dataframe
    # sart csv list => simple list of all files
    get_personality_averages(personality_data)
    sart_scores = []
    for file_name in sart_csv_list:
        correctness, response_time = get_score(file_name)
        sart_scores.append([correctness, response_time])

    sartDataFrame =pd.DataFrame(sart_scores, columns = ['Response Time', 'Correctness'])

    completeDataFrame = personality_data.copy()
    completeDataFrame = completeDataFrame.assign(ResponseTime = sartDataFrame['Response Time'])
    completeDataFrame = completeDataFrame.assign(Correctness = sartDataFrame['Correctness'])

    completeDataFrame.to_csv("../processed_data/BRED_Project_Values.csv")
    return completeDataFrame
    
    