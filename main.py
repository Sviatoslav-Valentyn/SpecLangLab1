from lab_runner import LabRunnerFacade

def main():
    runner = LabRunnerFacade()

    while True:
        print("\n==== ЛАБОРАТОРНІ РОБОТИ ====")
        print("1. Виконати лабораторну роботу 1")
        print("2. Виконати лабораторну роботу 2")
        print("3. Виконати лабораторну роботу 3")
        print("4. Виконати лабораторну роботу 4")
        print("5. Виконати лабораторну роботу 5")
        print("7. Виконати лабораторну роботу 7")
        print("8. Виконати лабораторну роботу 8")
        print("0. Вихід")

        choice = input("Введіть номер лабораторної роботи або 0 для виходу: ")

        if choice == '1':
            runner.run_lab1()
        if choice == '2':
            runner.run_lab2()
        elif choice == '3':
            runner.run_lab3()
        elif choice == '4':
            runner.run_lab4()
        elif choice == '5':
            runner.run_lab5()
        elif choice == '7':
            runner.run_lab7()
        elif choice == '8':
            runner.run_lab8()
        elif choice == '0':
            print("Дякую за використання програми. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
