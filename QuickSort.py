comparisonArray = []

def pivotLocator(left, right, switch):
	# Switch = 1 means that the first element in the input Array is the Pivot
	if switch == 1:
		return left
	# Switch = 2 means that the last element in the input Array is the Pivot
	elif switch == 2:
		return right
	# Switch = 3 means that the the median of the first element, the last element and the medium element in the input Array is the Pivot
	elif switch == 3:
		temp = []
		temp.append(arr[left])
		temp.append(arr[right])
		temp.append(arr[int((left + right)/2)])
		temp.sort()
		return arr[left : right+1].index(temp[1]) + left

def swapElements(index1, index2):
	arr[index1], arr[index2] = arr[index2], arr[index1]


def partition(left, right, switch):	
	i = left + 1
	counter = 0

	pivotLocation = pivotLocator(left, right, switch)
	pivot = arr[pivotLocation]
	
	arr[left], arr[pivotLocation] = arr[pivotLocation], arr[left]

	for index in range(left + 1, right + 1):
		if(arr[index] < pivot):
			swapElements(index, i)
			i = i + 1
			# print(arr)
		
		counter = counter + 1
	
	pivotLocation = i - 1
	swapElements(pivotLocation, left)

	comparisonArray.append(counter)
	return pivotLocation


def quickSort(left, right, switch):
	
	if(right - left >= 1):
		pivotLoc = partition(left, right, switch)
		quickSort(left , pivotLoc - 1 , switch)
		quickSort(pivotLoc + 1, right, switch)



switch = int(input("enter the switch: "))

arr = []
for i in range(10000):
	arr.append(int(input()))



quickSort(0 , 9999 , switch)
print(arr)

print(sum(comparisonArray))