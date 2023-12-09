import pandas as pd
import matplotlib.pyplot as plt
import json
import csv
import logging
from prettytable import PrettyTable
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

class Loader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_csv(self):
        return pd.read_csv(self.file_path)

class Analyzer:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def find_extremes(self, column):
        return self.dataframe[column].max(), self.dataframe[column].min()

# Завдання 7: Розширені візуалізації
class Visualizer:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.last_figure = None

    def plot_basic(self, column, title, xlabel, ylabel):
        if self.last_figure is not None:
            plt.close(self.last_figure)

        # Розділити малюнок на сітку 2x1 (2 рядки, 1 стовпець)
        self.last_figure, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

        # Перший підграфік: лінійний графік
        ax1.plot(self.dataframe.index, self.dataframe[column])
        ax1.set_title(title)
        ax1.set_xlabel(xlabel)
        ax1.set_ylabel(ylabel)

        # Другий підграфік: стовпчикова діаграма
        value_counts = self.dataframe[column].value_counts()
        ax2.bar(value_counts.index, value_counts.values, color='skyblue', edgecolor='black')
        ax2.set_xlabel(xlabel)
        ax2.set_ylabel('Count')

        # Налаштування розташування підграфіків
        plt.tight_layout()

        plt.show()

    def plot_bar(self, categories, values, title='Bar Chart', xlabel='Category', ylabel='Value'):
        self.last_figure, ax = plt.subplots()
        ax.bar(categories, values)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_histogram(self, column, bins=10):
        self.last_figure, ax = plt.subplots()
        ax.hist(self.dataframe[column], bins=bins)
        plt.show()

    def plot_scatter(self, column_x, column_y):
        self.last_figure, ax = plt.subplots()
        ax.scatter(self.dataframe[column_x], self.dataframe[column_y])
        plt.show()

    def plot_count_by_category(self, category):
        counts = self.dataframe[category].value_counts()
        self.plot_bar(counts.index, counts.values, title='Count of items by category', xlabel='Category', ylabel='Count')

    def get_figure(self):
        return self.last_figure

    def save_figure(self, filename):
        if self.last_figure:
            self.last_figure.savefig(filename)

class Exporter:
    def export_plot(self, figure, filename):
        figure.savefig(filename)

class FileStorage:
    @staticmethod
    def store_data(data, file_format):
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