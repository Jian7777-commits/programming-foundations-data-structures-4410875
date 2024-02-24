seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]


student = seating_chart[2][1]
#print(student)

for i, row in enumerate(seating_chart):
  for j, student in enumerate(row):
    print(f"{student} seat {i+1}{j+1}")
    #print(j + " " + str(seating_chart.index(i))+ " : " + str(i.index(j)))