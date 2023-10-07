def bubble_sort(arr):
   n = len(arr)
   for i in range(n):
     for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
           arr[j], arr[j + 1] = arr[j + 1], arr[j]

list1 = [1,3,8,9]
list2 = [7,4,7,6]
           
merged_list = list1 + list2
bubble_sort(merged_list)
second_largest = merged_list[-2]
print("Merged List:", merged_list)
print("Second Largest Element:", second_largest)
