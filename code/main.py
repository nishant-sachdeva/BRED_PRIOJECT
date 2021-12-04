from parse import parse
from scores import calculate_scores
from correlation_stats import get_correlation_stats
from plotting import plot_stats

if __name__ == '__main__':
    parse()
    calculate_scores()
    get_correlation_stats()
    plot_stats()
    print('\n================================')