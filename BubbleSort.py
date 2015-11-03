
def arr():
	import random
	i = 0
	arr = []
	while i < 101:
		rand = random.randint(0,10000)
		arr.append(rand)
		i+=1
	return arr

def bubble(arr):
	length = len(arr)-1
	sort = False

	while not sort:
		sort = True
		for i in range(length):
			if arr[i] > arr[i+1]:
				sort = False
				arr[i], arr[i+1] = arr[i+1], arr[i]
arr = arr()

bubble(arr)

print(arr)