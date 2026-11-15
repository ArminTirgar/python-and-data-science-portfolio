if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    filter_array = list(set(arr))
    filter_array.sort(reverse=True)
    print(filter_array[1])