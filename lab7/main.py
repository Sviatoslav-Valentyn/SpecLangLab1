from cgi import FieldStorage
import requests
import json
import csv
import re
import pandas as pd
import logging
from prettytable import PrettyTable

# Завдання 7: Ініціалізація логування
logging.basicConfig(filename='api_client.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

class FileStorage:
    @staticmethod
    def store_data(data, file_format):
        # Завдання 6: Збереження даних у чіткому та читабельному форматі JSON, CSV та TXT
        if file_format == 'json':
            with open('saved_data.json', 'w') as file:
                json.dump(data, file, indent=4)
        elif file_format == 'csv':
            dataframe = pd.DataFrame(data)
            dataframe.to_csv('saved_data.csv', index=False)
        elif file_format == 'txt':
            with open('saved_data.txt', 'w') as file:
                file.write(str(data))

class ApiClient:
    def __init__(self, api_url):
        # Завдання 1: Вибір провайдера API
        self.api_url = api_url

    def make_request(self, endpoint, params=None):
        try:
            headers = {'Accept': 'application/json'}
            # Завдання 2: Інтеграція API
            response = requests.get(f'{self.api_url}/{endpoint}', headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as err:
            # Завдання 7: Обробка помилок
            logging.error(f'Помилка виклику API: {err}')
            return None
    def add_todo(self, todo_data):
        try:
            endpoint = 'todos'
            headers = {'Content-Type': 'application/json'}
            response = requests.post(f'{self.api_url}/{endpoint}', headers=headers, json=todo_data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as err:
            logging.error(f'Помилка виклику API: {err}')
            return None

class UserInterface:
    def __init__(self, api_client):
        self.api_client = api_client
        self.history = []

    def display_data(self, data):
        if data:
            headers = data[0].keys()
            rows = [d.values() for d in data]
            table = PrettyTable()
            table.field_names = headers
            table.add_rows(rows)
            print(table)
        else:
            print('Немає даних для відображення.')

    def display_menu(self):
        # Завдання 3: Введення користувача
        # Просте українське меню
        print("Виберіть опцію:")
        print("1. Переглянути список справ")
        print("2. Зберегти дані")
        print("3. Додати нову справу")
        print("exit. Вийти з програми")

        user_input = input('Введіть свій вибір: ')
        return user_input

    def process_command(self, command):
        try:
            if command == '1':
                endpoint = 'todos'
                params = None
                # Завдання 5: Відображення результатів
                api_response = self.api_client.make_request(endpoint, params)
                self.history.append({'command': command, 'data': api_response})
                self.display_data(api_response)
            elif command == '2':
                # Зберегти останній відповідь API
                if self.history:
                    last_response = self.history[-1]['data']
                    self.save_data(last_response, 'json')
                    self.save_data(last_response, 'csv')
                    self.save_data(last_response, 'txt')
                    print("Дані успішно збережено.")
                else:
                    print("Немає даних для збереження.")
            elif command == '3':
                self.add_new_todo()
            elif command.lower() == 'exit':
                print("Вихід з програми.")
            else:
                print('Невірна команда. Будь ласка, введіть правильний номер опції або "exit".')
        except Exception as e:
            # Завдання 7: Обробка помилок
            logging.error(f'Помилка обробки команди {command}: {e}')

    def add_new_todo(self):
        title = input('Введіть назву нової справи: ')
        completed = input('Чи завершена справа? (True/False): ').lower() == 'true'

        new_todo = {'userId': 1, 'title': title, 'completed': completed}
        self.history.append({'command': 'add_todo', 'data': new_todo})
        print('Нову справу успішно додано.')
        
    def save_data(self, data, file_format):
        FileStorage.store_data(data, file_format)

    def run(self):
        while True:
            command = self.display_menu()
            if command.lower() == 'exit':
                break
            self.process_command(command)

if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    api_client = ApiClient(api_url)
    interface = UserInterface(api_client)

    while True:
        command = interface.display_menu()

        if command.lower() == 'exit':
            break

        interface.process_command(command)