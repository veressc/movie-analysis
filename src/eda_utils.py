import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    """Загрузка данных из CSV файла"""
    return pd.read_csv(filepath)

def show_head(df, n=5):
    """Вывод первых строк таблицы"""
    print(df.head(n))

def show_info(df):
    """Вывод базовой информации о датасете"""
    print(df.info())

def calculate_average_rating(df):
    """Расчёт среднего рейтинга фильмов"""
    average_rating = df['rating'].mean()
    print(f"Средний рейтинг фильмов: {average_rating:.2f}")
    return average_rating

def get_top_10_movies(df):
    """Получение топ-10 фильмов по рейтингу"""
    top_10 = df.sort_values(by='rating', ascending=False).head(10)
    print("Топ-10 фильмов по рейтингу:")
    print(top_10[['title', 'rating']])
    return top_10

def plot_ratings_by_year(df):
    """Построение графика: средний рейтинг по годам"""
    ratings_by_year = df.groupby('year')['rating'].mean()
    plt.figure(figsize=(10, 5))
    plt.plot(ratings_by_year.index, ratings_by_year.values, marker='o')
    plt.title('Средний рейтинг фильмов по годам')
    plt.xlabel('Год выпуска')
    plt.ylabel('Средний рейтинг')
    plt.grid(True)
    plt.savefig('graph.png')
    plt.show()
