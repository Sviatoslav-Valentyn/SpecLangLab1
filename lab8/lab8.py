import pandas as pd
import matplotlib.pyplot as plt
import json
import csv
from prettytable import PrettyTable

class Loader:
    """Клас для завантаження даних з CSV-файлу."""
    def __init__(self, file_path):
        """Ініціалізує об'єкт класу Loader.

        Args:
            file_path (str): Шлях до CSV-файлу.
        """
        self.file_path = file_path

    def load_csv(self):
        """Завантажує дані з CSV-файлу.

        Returns:
            pd.DataFrame: Завантажений DataFrame.
        """
        return pd.read_csv(self.file_path)

class Analyzer:
    """Клас для аналізу даних."""
    def __init__(self, dataframe):
        """Ініціалізує об'єкт класу Analyzer.

        Args:
            dataframe (pd.DataFrame): DataFrame для аналізу.
        """
        self.dataframe = dataframe

    def find_extremes(self, column):
        """Знаходить максимальне та мінімальне значення в колонці.

        Args:
            column (str): Назва колонки.

        Returns:
            tuple: Максимальне та мінімальне значення.
        """
        return self.dataframe[column].max(), self.dataframe[column].min()

class Visualizer:
    """Клас для візуалізації даних."""
    def __init__(self, dataframe):
        """Ініціалізує об'єкт класу Visualizer.

        Args:
            dataframe (pd.DataFrame): DataFrame для візуалізації.
        """
        self.dataframe = dataframe
        self.last_figure = None

    def plot_basic(self, column, title, xlabel, ylabel):
        """Базова візуалізація даних.

        Args:
            column (str): Назва колонки для візуалізації.
            title (str): Заголовок графіку.
            xlabel (str): Підпис осі X.
            ylabel (str): Підпис осі Y.
        """
        if self.last_figure is not None:
            plt.close(self.last_figure)

        self.last_figure, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

        ax1.plot(self.dataframe.index, self.dataframe[column])
        ax1.set_title(title)
        ax1.set_xlabel(xlabel)
        ax1.set_ylabel(ylabel)

        value_counts = self.dataframe[column].value_counts()
        ax2.bar(value_counts.index, value_counts.values, color='skyblue', edgecolor='black')
        ax2.set_xlabel(xlabel)
        ax2.set_ylabel('Count')

        plt.tight_layout()
        plt.show()

    def plot_bar(self, categories, values, title='Bar Chart', xlabel='Category', ylabel='Value'):
        """Створює стовпчату діаграму.

        Args:
            categories (list): Список категорій.
            values (list): Список значень.
            title (str, optional): Заголовок графіку. Defaults to 'Bar Chart'.
            xlabel (str, optional): Підпис осі X. Defaults to 'Category'.
            ylabel (str, optional): Підпис осі Y. Defaults to 'Value'.
        """
        self.last_figure, ax = plt.subplots()
        ax.bar(categories, values)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_histogram(self, column, bins=10):
        """Створює гістограму.

        Args:
            column (str): Назва колонки для гістограми.
            bins (int, optional): Кількість бінів. Defaults to 10.
        """
        self.last_figure, ax = plt.subplots()
        ax.hist(self.dataframe[column], bins=bins)
        plt.show()

    def plot_scatter(self, column_x, column_y):
        """Створює діаграму розсіювання.

        Args:
            column_x (str): Назва колонки для осі X.
            column_y (str): Назва колонки для осі Y.
        """
        self.last_figure, ax = plt.subplots()
        ax.scatter(self.dataframe[column_x], self.dataframe[column_y])
        plt.show()

    def plot_count_by_category(self, category):
        """Створює стовпчату діаграму для підрахунку кількості елементів за категорією.

        Args:
            category (str): Назва колонки категорій.
        """
        counts = self.dataframe[category].value_counts()
        self.plot_bar(counts.index, counts.values, title='Count of items by category', xlabel='Category', ylabel='Count')

    def get_figure(self):
        """Отримує поточну фігуру.

        Returns:
            plt.Figure: Об'єкт поточної фігури.
        """
        return self.last_figure

    def save_figure(self, filename):
        """Отримує поточну фігуру.

        Returns:
            plt.Figure: Об'єкт поточної фігури.
        """
        if self.last_figure:
            self.last_figure.savefig(filename)

class Exporter:
    def export_plot(self, figure, filename):
        """Експортує фігуру в файл.

        Args:
            figure (plt.Figure): Об'єкт фігури.
            filename (str): Ім'я файлу для збереження.
        """
        figure.savefig(filename)

class FileStorage:
    @staticmethod
    def store_data(data, file_format):
        """Зберігає дані у вказаному форматі.

        Args:
            data: Дані для збереження.
            file_format (str): Формат збереження ('json', 'csv', 'txt').
        """
        if file_format == 'json':
            with open('saved_data.json', 'w') as file:
                json.dump(data, file, indent=4)
        elif file_format == 'csv':
            with open('saved_data.csv', 'w', newline='') as file:
                csv_writer = csv.DictWriter(file, fieldnames=data[0].keys())
                csv_writer.writeheader()
                csv_writer.writerows(data)
        elif file_format == 'txt':
            with open('saved_data.txt', 'w') as file:
                file.write(str(data))

def run_lab8():
    # Завдання 1: Вибір CSV-набору даних
    file_path = "saved_data.csv"

    # Завдання 2: Завантаження даних з CSV
    loader = Loader(file_path)
    dataframe = loader.load_csv()

    # Завдання 3: Дослідження даних
    analyzer = Analyzer(dataframe)
    max_value, min_value = analyzer.find_extremes('completed')
    print(f"Max Value: {max_value}\nMin Value: {min_value}")

    # Завдання 4: Вибір типів візуалізацій
    visualizer = Visualizer(dataframe)
    # Завдання 6: Базова візуалізація
    visualizer.plot_basic('completed', 'Completion Status', 'Index', 'Completion Status')

    # Завдання 9: Експорт і обмін
    exporter = Exporter()
    figure = visualizer.get_figure()
    visualizer.save_figure('plot.png')
    exporter.export_plot(figure, 'plot.png')

    file_storage = FileStorage()
    file_storage.store_data(dataframe, 'csv')

if __name__ == "__main__":
    run_lab8()