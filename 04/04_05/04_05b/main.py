def has_unique_characters(data):
    data_set = set()
    for i in data:
        data_set.add(i)
    if len(data_set) == len(data):
        return True
    else:
        return False

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
