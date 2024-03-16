
from library_metods import*
import os
print("hello")
spisok = []
while(True):

    os.system('cls')
    print("1.Добавить студента \n2.Просмотра списка студентов \n3.Изменение информации студента \n4.Удалить студента \n5.Выход")

    try:
        meny = int(input())

        if meny ==1:
            os.system('cls')
            print("\t\t\tСоздание студента!")
            create_spisok(spisok)
            input()
        elif meny ==2:
            os.system('cls')
            print("\t\t\tСписок студентов!")
            info_get(spisok)
            input()
        elif meny ==3:
            os.system('cls')
            print("\t\t\tИзменение информации студента!")
            info_get(spisok)
            change_InfoStudent(spisok)
            input()
        elif meny ==4:
            os.system('cls')
            print("\t\t\tУдаление студента!")
            info_get(spisok)
            delete_student(spisok)
            input()
        elif meny == 5:break
        else:
            os.system('cls')
            print("\t\t\tОперация выбрана неверно\n\n\t\tНажмите любую кнопку для продолжения")
            input()

    except BaseException as ex:
        os.system('cls')
        print("Ошибка", ex)
        input()

