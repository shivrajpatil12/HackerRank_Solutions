def average(arr):
    plant_set = set(arr)
    avg = sum(plant_set)/len(plant_set)
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)