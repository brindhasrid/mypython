def game_with_number(arr, n):
    for i in range(n - 1):  # Loop until second last element
        arr[i] = arr[i] ^ arr[i + 1]  # XOR of consecutive elements
    return arr  # Return the modified array
