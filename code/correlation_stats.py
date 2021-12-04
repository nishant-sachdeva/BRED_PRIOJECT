import numpy as np
import pandas as pd


def get_correlation_stats(dataFrame):
    correlation_scores = []
    colmNames = list(dataFrame)
    relevantPersonalityDataColmNames = colmNames[4:9]
    relevantSARTDataColmNames = colmNames[9:]

    correlation_scores = {}

    # 5 colmns in Personality Data, 2 Colmns in Sart Data
    for personalityColm in relevantPersonalityDataColmNames:
        for sartColm in relevantSARTDataColmNames:
            correlation_scores[personalityColm+" - "+sartColm] = dataFrame[personalityColm].corr(dataFrame[sartColm])
    

    return dataFrame, correlation_scores