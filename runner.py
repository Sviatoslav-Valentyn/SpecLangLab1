from utils.input_handling import get_integer_input
import lab1.lab1
import lab2and6.lab2
import lab3.lab3
import lab4.lab4
import lab5.main
import lab2and6.lab6

if __name__ == "__main__":      
    def choose_lab():
        while True:
            lab_number = get_integer_input("Оберіть номер лабораторної (1-5): ")
            if 1 <= lab_number <= 6:
                return lab_number
            else:
               print("Введений номер не відповідає жодній лабораторній роботі (1-5)")


    lab_number = choose_lab()

    while True:
        match lab_number:
            case 1:
                lab1.lab1.main()
            case 2:
                lab26.lab2.main()
            case 3:
                lab3.lab3.main()
            case 4:
                lab4.lab4.main()
            case 5:
                lab5.main.main()
            case 6:
                lab26.lab6.main()
            case 0:
                break