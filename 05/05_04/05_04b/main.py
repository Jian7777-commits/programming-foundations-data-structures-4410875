from collections import deque

def print_binary_numbers(n):
  if(n <= 0):
    return
  
  queue = deque()
  queue.append(1)

  for i in range(n):
    binary = queue.popleft()
    queue.append(binary * 10)
    queue.append(binary * 10 + 1)
    print(binary)

print_binary_numbers(10)
print_binary_numbers(0)
print_binary_numbers(115)
print_binary_numbers(0)
print_binary_numbers(10)