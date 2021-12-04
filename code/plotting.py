import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_stats(dataFrame, correlation_scores):
    personality_colmns = list(dataFrame)[4:9]
    sart_colmns = list(dataFrame)[9:]

    print(personality_colmns)
    print(sart_colmns)

    for personality_name in personality_colmns:
        for sart_name in sart_colmns:
            dataFrame.sort_values(by=[personality_name], inplace=True)
            retValue = dataFrame.plot(x=personality_name, y=sart_name, kind='line')
            plt.show()

    return