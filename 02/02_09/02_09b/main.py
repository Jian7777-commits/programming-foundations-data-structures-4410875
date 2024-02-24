def find_second_smallest(my_list):
    if(len(my_list) > 1):
        sorted_list = sorted(my_list)
        second_smallest = sorted_list[1]
        return second_smallest
    else:
        print("you only have one item on the list")


def find_second_smallest_v2(my_list):
    if(len(my_list) < 2):
        return None
    smallest = float("inf")
    second_smallest = float("inf")
    for i in my_list:
        if(i < smallest):
            second_smallest = smallest
            smallest = i
        elif (i < second_smallest):
            second_smallest = 1

    return second_smallest
print(find_second_smallest_v2([5, 8, 3, 2, 6,1,0]))
