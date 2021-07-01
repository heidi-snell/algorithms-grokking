
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = list[middle]

        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
        else:
            low = middle + 1
        return None


my_list = [1, 3, 5, 7, 9]
my_item = 5
index = binary_search(my_list, my_item)

print("your item {} appears in index {} of the list {}.".format(
    my_item, index, my_list))
