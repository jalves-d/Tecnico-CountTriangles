import time
import collections
arqnum = input("Digite o nome do arquivo e o número de elementos: ").split(" ")

t_begin = time.process_time()
"""read_fileo: Essa função é responsável por ler o arquivo a partir do nome passado, tudo é armazenado como string em uma lista (lines)
para depois ser armazenado no dicionario (data) ao qual armazena todas as conexões entre um vertice e outro sendo a chave o vertice
e os valores os vertices que se conectam com ela. No read_fileo apenas são considerados grafos orientados também assim sendo mais
otimizado para esse tipo de caso poupando memória e tempo
"""

def read_fileo(nome):
	with open(nome, "r") as f:
		lines = f.read().replace("\n", " ").replace(",", " ").replace("\t", " ").split(" ")
	n = 1
	data = {}
	while n < len(lines):
		if int(lines[n-1]) in data:
			data[int(lines[n-1])] += [int(lines[n]),]
		else:
			data[int(lines[n-1])] = [int(lines[n]),]
		n += 2
	return data

"""
read_fileno : Faz a mesma coisa que o read_fileo mas para aceitar apenas grafos não orientados é necessário fazer mais validações assim
aumentando o consumo de memória e de tempo.
"""

def read_fileno(nome):
	with open(nome, "r") as f:
		valores = f.read().replace("\n", " ").replace(",", " ").replace("\t", " ").split(" ")
	n = 1
	data = {}
	while n < len(valores):
		if int(valores[n-1]) in data:
			if int(valores[n]) not in data[int(valores[n-1])]:
				data[int(valores[n-1])] += [int(valores[n]),]
		else:
			data[int(valores[n-1])] = [int(valores[n]),]
		if int(valores[n]) in data:
			if int(valores[n-1]) not in data[int(valores[n])]:
				data[int(valores[n])] += [int(valores[n-1]),]
		else:
			data[int(valores[n])] = [int(valores[n-1]),]
		n += 2
	return data
"""
incrementcont: Foi feita apenas para diminuir o número de if's na hora de incrementar o contador de aparições do vertice
"""
def incrementcont(contador, el):
	if el in contador:
		contador[el] += 1
	else :
		contador[el] = 1
"""
contdata: É utilizado para contar os triângulos, os condicionais m > n e j > m impedem que sejam contados triângulos repitidos
a idéia no código é verificar se na minha chave A existe um valor B que em sua chave correspondente exista um valor C que em sua
chave correspondente tenha o valor A. ex : 1 : (2), 3, 4 | 2 : 1, (3), 5 | 3 : (1), 2, 7  || 1 -> 2 -> 3 -> 1 || 1, 2, 3
"""
def contdata(conttri, dicionario):
	contador = {}
	for n in dicionario:
		for m in dicionario[n]:
			if m > n:
				for j in dicionario[m]:
					if j > m:
						if n in dicionario[j]:
							incrementcont(contador, n)
							incrementcont(contador, m)
							incrementcont(contador, j)
							conttri += 1
	print("Triângulos : " + str(conttri))
	return contador
"""
checknbiggest: Utilizado para identificar os N vértices que aparecem mais vezes em triângulos dando prioridade aos vértices
de menor valor, a lógica aplicada foi de ordenar a partir dos valores das chaves inicialmente e reverter para estarem ordenadas
da maior para menor, em seguida foi ordenado os valores, e foi selecionado apenas os N ultimos elementos da lista, uma vez que
funçao sorted retorna tuplas foi necessário eliminar os segundos elementos de cada tupla assim retornando apenas o valor dos
vértices. ex: [1: 3, 2 : 1, 3: 5, 5: 2, ...] -> [..., (5, 2), (3, 5), (2, 1), (1, 3)] -> [..., (5, 2), (2, 2), (1, 3), (3, 5)] ->
n = 2 -> [(1, 3), (3, 5)] -> [1, 3]
"""
def checknbiggest(contador, num):
	contador = sorted(contador.items(), key= lambda item : item[0])
	contador.reverse()
	ordenado = sorted(contador, key= lambda item : item[1])
	ordenado = ordenado[-int(arqnum[1]):]
	lastitems = [x[0] for x in ordenado]
	print(lastitems)

checknbiggest(contdata(0, read_fileno(arqnum[0])), arqnum[1])

t_end = time.process_time()

print("\nTempo :" + str(t_end - t_begin))
