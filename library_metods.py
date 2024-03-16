from Student import Student
import os

def create_spisok(spisok):
    
    try:
        name = input("name: ")
        age = int(input("age:"))
        curs = int(input("curs: "))
        grupa = int(input("grupa: "))
        spisok.append(Student(name,age,curs,grupa))
    
    except BaseException as ex: 
        os.system('cls')
        print("Ошибка ввода: ", ex)

def info_get(spisok):
    for n in spisok:
        print(f"\n{spisok.index(n)}. ", end = "")
        n.get_info()

def delete_student(spisok):

    index_student = int(input("Ввуедите индекс студента которого хотите удалить: "))
    os.system('cls')
    for n in spisok:
        if spisok.index(n) ==index_student:
            spisok.pop(index_student)
            break
    print(("Удаление прошло успешно"))
    
def change_InfoStudent(spisok):
    try:
        index_student = int(input("Введите индекс студента которого хотите удалить: "))
        os.system(('cls'))

        spisok[index_student].get_info()
        print("\n1.name\n2.age\n3.curs\n4.grupa")

        category_change = int(input("Ввыберете категорию которую хотите изменить: "))
        if category_change ==1:
            os.system('cls')
            spisok[index_student].name = input("new_name: ")
            print("\nИзменение прошло удачно")
        elif category_change ==2:
            os.system('cls')
            spisok[index_student].age = input("new age: ")
            print("\nИзменение прошло успешно")
        elif category_change ==3:
            os.system('cls')
            spisok[index_student].curs = input("new curs: ")
            print("\nИзменение прошло успешно")
        elif category_change ==4:
            os.system('cls')
            spisok[index_student].grupa = input("new grupa: ")
            print("\nИзменение прошло успешно")
        else:
            os.system('cls')
            print("Неверный выбор категории")

    except BaseException as ex:
        os.system('cls')
        print("Ошибка:", ex)
        

