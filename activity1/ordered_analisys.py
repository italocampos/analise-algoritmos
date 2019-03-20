# Ranges: 1k, 10k, 20k, 50k, 70k
from random import randint
from time import time
from matplotlib import pyplot as chart

def insertion_sort(lista):
	for i in range(1, len(lista)):
		chave = lista[i]
		k = i
		while k > 0 and chave < lista[k - 1]:
			lista[k] = lista[k - 1]
			k -= 1
		lista[k] = chave

def bubble_sort(lista):
	elementos = len(lista)-1
	ordenado = False
	while not ordenado:
		ordenado = True
		for i in range(elementos):
			if lista[i] > lista[i+1]:
				lista[i], lista[i+1] = lista[i+1],lista[i]
				ordenado = False
	return lista

def selection_sort(A):
	for i in range(len(A)):       
		# Find the minimum element in remaining unsorted array
		min_idx = i 
		for j in range(i+1, len(A)): 
			if A[min_idx] > A[j]: 
				min_idx = j 

		# Swap the found minimum element with the first element         
		A[i], A[min_idx] = A[min_idx], A[i]

def get_vector(length, mode = 'r'):
	if mode == 'r':
		vector = []
		for _ in range(length):
			vector.append(randint(0,length))
		return vector
	elif mode == 'o':
		return list(range(length))
	elif mode == 'i':
		return list(range(length))[::-1]
	else:
		raise('Unknown list generation mode.')

values = [500, 1000, 1500, 2000, 2500, 3000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
#values = [500, 1000, 1500, 2000]
times_bubble = []
times_insertion = []
times_selection = []

# Execução dos algoritmos utilizando vetores ordenados inversamente
for value in values:
	# Execução do buuble sort
	average = 0
	for i in range(3):
		initial = time()
		bubble_sort(get_vector(value, 'o'))
		average += time() - initial
		print('{a} - Iteration #{b} from bubble finished.'.format(a = value, b = i))
	average /= 3
	times_bubble.append(average)
	print('Tests for {a} vaules finished. Computed time: {b}'.format(a = value, b = average))

	# Execução do insertion sort
	average = 0
	for i in range(3):
		initial = time()
		insertion_sort(get_vector(value, 'o'))
		average += time() - initial
		print('{a} - Iteration #{b} from insertion finished.'.format(a = value, b = i))
	average /= 3
	times_insertion.append(average)
	print('Tests for {a} vaules finished. Computed time: {b}'.format(a = value, b = average))

	# Execução do selection sort
	average = 0
	for i in range(3):
		initial = time()
		selection_sort(get_vector(value, 'o'))
		average += time() - initial
		print('{a} - Iteration #{b} from selection finished.'.format(a = value, b = i))
	average /= 3
	times_selection.append(average)
	print('Tests for {a} vaules finished. Computed time: {b}'.format(a = value, b = average))

# Mostrar gráficos
# Bubble sort
chart.title('Bubble sort')
chart.plot(values, times_bubble, color = 'red')
chart.xlabel('Tamanho da entrada')
chart.ylabel('Tempo médio')
chart.grid(True)
chart.savefig('bubble.png')
chart.show()

# Insertion sort
chart.title('Insertion sort')
chart.plot(values, times_insertion, color = 'blue')
chart.xlabel('Tamanho da entrada')
chart.ylabel('Tempo médio')
chart.grid(True)
chart.savefig('insertion.png')
chart.show()

# Selection sort
chart.title('Selection sort')
chart.plot(values, times_selection, color = 'black')
chart.xlabel('Tamanho da entrada')
chart.ylabel('Tempo médio')
chart.grid(True)
chart.savefig('selection.png')
chart.show()

# Joining
chart.title('Algoritmos de ordenação')
chart.plot(values, times_bubble, color = 'red', label = 'Bubble sort')
chart.plot(values, times_insertion, color = 'blue', label = 'Insertion sort')
chart.plot(values, times_selection, marker = 'o', color = 'black', label = 'Selection sort')
chart.xlabel('Tamanho da entrada')
chart.ylabel('Tempo médio')
chart.grid(True)
chart.legend(loc='best')
chart.xlim(0,10000)
chart.ylim(0,0.02)
chart.savefig('join.png')
chart.show()

# Escrevendo dados em arquivo
file = open('data.txt', 'w')
file.write('Tamanho da entrada: {lista}'.format(lista = values))
file.write('\nTempo de execução bubble sort: {lista}'.format(lista = times_bubble))
file.write('\nTempo de execução insertion sort: {lista}'.format(lista = times_insertion))
file.write('\nTempo de execução selection sort: {lista}'.format(lista = times_selection))
file.close()