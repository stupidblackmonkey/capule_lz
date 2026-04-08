from graphic_stats import GraphicStatistics
from logs import log
@log
def main():
    df_path = 'states.csv'
    stats = GraphicStatistics(df_path)
    stats.histogram()
@log
def example_function():
    return "Результат"

example_function()


if __name__ == '__main__':
    main()