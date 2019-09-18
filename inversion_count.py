def count(ar):
	if len(ar) == 1:
		return ar, 0
	else:
		ar1, x = count(ar[:int(len(ar)/2)])
		ar2, y = count(ar[int(len(ar)/2):])
		ar3, z = split_count(ar1, ar2)
		return ar3, x + y + z


def split_count(a1, a2):
	print("___"*23)
	i = 0
	j = 0
	t1 = len(a1) - 1
	t2 = len(a2) - 1
	end = []
	inversions = 0
	sentinel = 999999999999
	a1.append(sentinel)
	a2.append(sentinel)
	
	for k in range(t1 + t2 + 2):
		print(k)
		if a1[i] <= a2[j]:
			end.append(a1[i])
			print("i ",a1[i])
			i=i+1
				

		else:
			end.append(a2[j])
			print("j ",a2[j])
			j+= 1
			inversions= inversions + t1 - i + 1
		
			

	return end, inversions

arr=[]

for i in range(100000):
	arr.append(int(input()))


a, n = count(arr)
print(n)
print(a)


