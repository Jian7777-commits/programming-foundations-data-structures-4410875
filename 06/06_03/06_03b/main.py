from collections import deque


history_stack = deque()
history_stack.append("https://www.youtube.com/watch?v=Kmgo00avvEw")
history_stack.append("https://www.youtube.com/watch?v=WZNG8UomjSI")
history_stack.append("https://www.udemy.com/course/java-development-projects/learn/lecture/40480096#overview")


print(history_stack[-1])
print(history_stack.pop())
