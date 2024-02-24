''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''
students_pet_count_list = [1,5,8,0,1,0,2,4,5,2,1,2,1,1,0,0,1]

ITEM_INDEX3 = students_pet_count_list[3]
num_of_students = len(students_pet_count_list)


sum = 0
for pet_count in students_pet_count_list:
  sum += pet_count
average = sum/num_of_students
print(average)

