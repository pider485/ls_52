import sqlite3

con = sqlite3.connect('univesity.db')

cursor = con.cursor()


while True:
    print("""
          0.Вихів
          1.Список тстудентів
          2.Список курсів
          3.Додати студента
          """)
    qwesion = input("Введіть дію: ")

    if qwesion == "0":
        break
    elif qwesion == "1":
        cursor.execute(
        """
        SELECT * FROM students    
        """)
        students=cursor.fetchall()
        print(students)

    elif qwesion == "2":
        cursor.execute(
        """
        SELECT * FROM courses    
        """)

        courses=cursor.fetchall()
        print(courses)

    elif qwesion == "3":
        name = input("Введіть ім'я Студента: ")
        age = input('Введіть вік: ')
        major = input('Введіть Курс: ')

        cursor.execute(
            """
            INSERT INTO students(name,age,major)
            VALUES(?,?,?)
            """, (name, int(age),major))
        
        con.commit()
        print("Успішно додано студента")

con.commit
con.close