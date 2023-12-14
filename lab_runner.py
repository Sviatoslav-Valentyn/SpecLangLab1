import logging
from lab1 import lab1
from lab2and6 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab7 import lab7
from lab8 import lab8

# Налаштування логування
logging.basicConfig(filename='lab_runner.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)

class LabRunnerFacade:
    def __init__(self):
        # Ініціалізація об'єкта з вказанням доступних лабораторних робіт
        self.lab1 = lab1
        self.lab2and6 = lab2
        self.lab3 = lab3
        self.lab4 = lab4
        self.lab5 = lab5
        self.lab7 = lab7
        self.lab8 = lab8

    def run_lab1(self):
        # Запуск лабораторної роботи 1
        logger.info("Running Lab 1")
        self.lab1.run_lab1()
        logger.info("Lab 2 completed")

    def run_lab2(self):
        # Запуск лабораторної роботи 2
        logger.info("Running Lab 2")
        self.lab2and6.run_lab2()
        logger.info("Lab 2 completed")
        
    def run_lab3(self):
        # Запуск лабораторної роботи 3
        logger.info("Running Lab 3")
        self.lab3.run_lab3()
        logger.info("Lab 3 completed")

    def run_lab4(self):
        # Запуск лабораторної роботи 4
        logger.info("Running Lab 4")
        self.lab4.run_lab4()
        logger.info("Lab 4 completed")
        
    def run_lab5(self):
        # Запуск лабораторної роботи 5
        logger.info("Running Lab 5")
        self.lab5.run_lab5()
        logger.info("Lab 5 completed")

    def run_lab7(self):
        # Запуск лабораторної роботи 7
        logger.info("Running Lab 7")
        self.lab7.run_lab7()
        logger.info("Lab 7 completed")
        
    def run_lab8(self):
        # Запуск лабораторної роботи 8
        logger.info("Running Lab 8")
        self.lab8.run_lab8()
        logger.info("Lab 8 completed")
        
if __name__ == "__main__":
    lab_runner = LabRunnerFacade()