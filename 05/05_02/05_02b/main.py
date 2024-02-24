from collections import deque

printer_queue = deque()
printer_queue.append('LebronJamesStats.pdf')
printer_queue.append('forextrading.pdf')
printer_queue.append('AnnualBudget.pdf')

print(printer_queue)
while(len(printer_queue) > 0):
  document = printer_queue.pop()
  print(document)