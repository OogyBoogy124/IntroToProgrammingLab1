#Parker Wood
#HW 2

def get_sums(list_int):
    #Part 1
    sums = 0
    ints = []
    for i in range(len(list_int)):
        lists = list_int[i]
        for p in range(len(lists)):
            sums = sums + lists[p]
        ints.append(sums)
        sums = 0
    print(ints)

def index_of_max_in_range(numbers, low_index, high_index):
    #Part 2
    x = 0
    y = 0
    for i in range(low_index, high_index):
        if numbers[i] > x:
            x = numbers[i]
            y = i
        else:
            continue
    print(y)


def swap_elements(array, index_a, index_b):
    #Part 3
    b = array[index_a]
    c = array[index_b]
    array[index_a] = c
    array[index_b] = b
    print(array)

def selection_sort(numbers):
    #Part 4
    x = 0
    numbers.append(0)
    print(numbers)
    for i in range(len(numbers)):
        if i + 1 > len(numbers):
            return
        else:
            if numbers[i] > numbers[i+1]:
                print(i)
                a = numbers[i]
                b = numbers[i+1]
                numbers[i] = b
                numbers[i+1] = a
    print(numbers)

def main():
    #Part 1
    #part_1_list = [[1,2,4], [1,2,3,6], [1,2,3,4,6,12]]
    #get_sums(part_1_list)
    #Part 2
    #part_2_list = [4,7,9,7]
    #index_of_max_in_range(part_2_list, 0, 4)
    #part 3
    #part_3_list = [0,1,2,'a','b',5]
    #swap_elements(part_3_list,0,4)
    #Part 4
    part_4_list = [2,3,1,4]
    selection_sort(part_4_list)

if __name__ == "__main__":
    main()
