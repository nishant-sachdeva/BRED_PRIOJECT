import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_stats(dataFrame, correlation_scores):
    personality_colmns = list(dataFrame)[:5]
    sart_colmns = list(dataFrame)[5:]

    for personality_name in personality_colmns:
        for sart_name in sart_colmns:
            dataFrame.sort_values(by=[personality_name], inplace=True)
            dataFrame.plot(x=personality_name, y=sart_name, kind='line')
            plt.savefig("../results/"+personality_name+sart_name+ ".png")
            plt.show()

    return