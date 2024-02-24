# Linear Search

my_list = [1, 3, 4, 6, 19, 2, 4, 8, 0, 1, 4, 6, 7, 12, 45, 6, 12, 56]
ITEM = 12

def linear_search(item, list):
  for i, element in enumerate(list):
    if(element.__eq__(item)):
      return True
  return False

print(linear_search(ITEM, my_list))