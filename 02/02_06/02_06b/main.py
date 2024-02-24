# Tuples are immutable array-like structures
point = (0, 5)

def calculate_square_properties(side_lenght):
  Area = side_lenght * side_lenght
  Perimeter = 4 * side_lenght

  return (Area, Perimeter)

result = calculate_square_properties(5)

print("Area is ", result[0])
print("Perimeter is ", result[1])
