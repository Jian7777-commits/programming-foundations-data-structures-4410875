my_list = [1, 7, 3,9,100,12,123,45,6,78,42,23,55,71,532,79,23,556,65,97]
print(sorted(my_list, reverse=True))

student_grade = [("Sarah" , 99), ("Rebecca", 89), ("Simon", 95)]

print(sorted(student_grade))
print(sorted(student_grade, key=lambda x:x[1]))


