students = ["Еремян", "Степин", "Чепля", "Леськов"]
course = ["Высшая математика", "Теория систем", "Бух.учёт", "Алгоритмизация"]
dates = ["03.07.26","03.06.26","03.05.26","03.04.26"]
grades = [1,2,3,4,5]
zero = [0, 1, 2, 3]

for c in zero:
    if c == "Бух.учёт":
        for d in zero:
            if d == "03.05.26":
                for s in zero:
                    if s == students[1]:
                        for g in zero:
                            print(s,g,c,d)