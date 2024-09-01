def partition_list(data, low_point, high_point):
  """
  Returns the index of the pivot element where elements on the left side are lower and 
  elements on the right side are greater than the pivot
  """
  
  pivot = data[high_point]
  i = low_point - 1

  for index in range(low_point, high_point):
    if data[index] <= pivot:
      i = i + 1
      data[i], data[index]) = (data[index], data[i]
  data[i + 1], data[high_point] = data[high_point], data[i + 1]
      
  return i + 1

def quicksort(data, low, high):
  """
  Sorts the pivot by recursively calling the partition_list function which sorts the elements before and after the pivot and returns the partition index
  """
  if low < high:  
    pivot = partition_list(data, low, high)
    quicksort(data, low, pivot-1)
    quicksort(data, pivot+1, high)

