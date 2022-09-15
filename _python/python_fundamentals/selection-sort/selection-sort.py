def selection_sort(array, size):

  for idx in range(size):
    min_idx = idx

    for j in range(idx+1, size):
      if array[j] < array[min_idx]:
        min_idx = j

    array[idx], array[min_idx] = array[min_idx], array[idx]

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selection_sort(arr, size)
print(arr)