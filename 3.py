students = ["Еремян", "Степин", "Чепля", "Леськов"]
course = ["Высшая математика", "Теория систем", "Бух.учёт", "Алгоритмизация"]
dates = ["03.07.26","03.06.26","03.05.26","03.04.26"]
grades = [1,2,3,4,5]

for c in course:
    if c == "Бух.учёт":
        for d in dates:
            if d == "03.05.26":
                for s in students:
                    for g in grades:
                        print(s,g,c,d)