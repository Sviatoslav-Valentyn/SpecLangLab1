from lab1 import lab1
from lab2and6 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab7 import lab7
from lab8 import lab8

class LabRunnerFacade:
    def __init__(self):
        self.lab1 = lab1
        self.lab2and6 = lab2
        self.lab3 = lab3
        self.lab4 = lab4
        self.lab5 = lab5
        self.lab7 = lab7
        self.lab8 = lab8

    def run_lab1(self):
        self.lab1.run_lab1()

    def run_lab2(self):
        self.lab2and6.run_lab2()
        
    def run_lab3(self):
        self.lab3.run_lab3()

    def run_lab4(self):
        self.lab4.run_lab4()
        
    def run_lab5(self):
       self.lab5.run_lab5()

    def run_lab7(self):
        self.lab7.run_lab7()
        
    def run_lab8(self):
        self.lab8.run_lab8()