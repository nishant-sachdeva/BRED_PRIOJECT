import pandas as pd
import numpy as np

from parse import parse
from scores import calculate_scores
from correlation_stats import get_correlation_stats
from plotting import plot_stats

if __name__ == '__main__':
    personality_data, sart_csv_list = parse("data")
    finalScoresDataFrame = calculate_scores(personality_data, sart_csv_list)
    # dataFrame, correlation_scores = get_correlation_stats(finalScoresDataFrame)
    # plot_stats(dataFrame, correlation_scores)
    print('\n================================')