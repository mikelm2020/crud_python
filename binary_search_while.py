import random


def binary_search(data, target, low_index, high_index):
    while low_index <= high_index:
        if low_index == high_index:
            if target == data[low_index]:
                return True
            else:
                return False
            break
        mid_index = (low_index + high_index) // 2

        if target == data[mid_index]:
            return True
            break
        else:
            if target < data[mid_index]:
                high_index = mid_index -1
            else:
                low_index = mid_index + 1


if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)]

    data.sort()

    print(data)
    target = int(input('What number would you like to find? '))
    found = binary_search(data, target, 0, len(data) - 1)
    
    print(found)