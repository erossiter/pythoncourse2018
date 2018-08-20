## returns element if it is in the list
def linear_search(mylist, element):
  steps = 0
  for item in mylist:
    steps += 1
    if item == element:
      print steps
      return item
  print steps
  return None


mylist = range(26)

linear_search(mylist, 1)
linear_search(mylist, 5)
linear_search(mylist, 30)



## returns element if it is in sorted list
def binary_search(sorted_list, element):
  print "Input list is {0}".format(sorted_list)
  print "Input size is {0}".format(len(sorted_list))
  middle = len(sorted_list)/2
  median = sorted_list[middle]
  if len(sorted_list)<=1:
    if element == median:
      return median
    else:
      return None
  if element < median:
    left = sorted_list[0:middle]
    return binary_search(left, element)
  else: 
    right = sorted_list[middle:]
    return binary_search(right, element)

mylist = range(25)
binary_search(mylist, 10)




