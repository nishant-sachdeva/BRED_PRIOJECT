from parse import parse
from scores import calculate_scores
from correlation_stats import get_correlation_stats
from plotting import plot_stats

if __name__ == '__main__':
    parse()
    calculate_scores()
    personality_data, sart_data, correlation_scores = get_correlation_stats("BRED_Project_Values.csv")
    plot_stats(personality_data, sart_data, correlation_scores)
    print('\n================================')