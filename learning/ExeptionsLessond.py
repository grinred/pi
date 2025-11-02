def read_ints(path):
    lst = []
    with open(path, "r") as f:
        for line in f:
            lst.append(int(line.strip()))
    return lst


def count_tree_sum(ints):
    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(1 + i, n):
            for k in range(1 + j, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found in row number: {i+1},{j+1},{k+1}', end='\n')



if __name__ == '__main__':
    print('started main')
    ints = read_ints("1Kints.txt")
    count_tree_sum(ints)
    print("ended main")

