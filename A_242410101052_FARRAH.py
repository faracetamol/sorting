def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:  
                arr[j], arr[j+1] = arr[j+1], arr[j]  
                swapped = True
        if not swapped:
            break  

data = [64, 34, 25, 12, 22, 11, 90]
print("Sebelum sorting:", data)
bubble_sort(data)
print("Setelah sorting:", data)
