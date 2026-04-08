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
    a = numbers[low_index,high_index]
    for i in range(len(a)):
        if a[i] > a[(i+1)]
        

def main():
    part_1_list = [[1,2,4], [1,2,3,6], [1,2,3,4,6,12]]
    get_sums(part_1_list)


if __name__ == "__main__":
    main()
