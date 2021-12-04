import numpy as np
import pandas as pd


def get_correlation_stats(file_name):
    correlation_scores = []

    path = "../processed_data/" + file_name

    dataFrame = pd.read_csv(path)
    dataFrame = dataFrame.fillna(value = np.nan)

    colmNames = list(dataFrame)
    relevantPersonalityDataColmNames = colmNames[4:8]
    relevantSARTDataColmNames = colmNames[9:]

    relevantPersonalityData = dataFrame[relevantPersonalityDataColmNames]
    relevantSARTData = dataFrame[relevantSARTDataColmNames]

    correlation_scores = {}

    # 5 colmns in Personality Data, 2 Colmns in Sart Data
    for personalityColm in relevantPersonalityDataColmNames:
        for sartColm in relevantSARTDataColmNames:
            correlation_scores[personalityColm+" - "+sartColm] = dataFrame[personalityColm].corr(dataFrame[sartColm])
    

    print(correlation_scores)
    return relevantPersonalityData, relevantSARTData, correlation_scores