# coding: utf-8
import math
from statistics import mean
import numpy as np
import random
import pandas as pd


def gera_populacao(tam_populacao, tam_individuo):
	individuos = []
	for i in range(tam_populacao):
		individuo = []
		for j in range(tam_individuo):
			n = random.random()
			if n < 0.5:
				individuo.append(0)
			else:
				individuo.append(1)
		individuos.append(individuo)
	return individuos

def converter_binario(individuo, xmin, xmax, n, tam_individuo):
	n1 = individuo[0:int(tam_individuo/2)]
	n2 = individuo[int(tam_individuo/2):(tam_individuo)]
	intn1, intn2 = 0, 0
	for i, j, k in zip(n1, n2, range(len(n1)-1, 0, -1)):
		intn1 = intn1 + (pow(2,k) * i)
		intn2 = intn2 + (pow(2,k) * j)
	x1 = xmin + ((xmax - xmin)/(pow(2,n) - 1)) * intn1
	x2 = xmin + ((xmax - xmin)/(pow(2,n) - 1)) * intn2
	return ([x1, x2])

def funcao_objetivo(x):
	n = float(len(x))
	f_exp = -0.2 * math.sqrt(1/n * sum(np.power(x, 2)))
	t = 0
	for i in range(0, len(x)):
		t += np.cos(2 * math.pi * x[i])
	s_exp = 1/n * t
	f = -20 * math.exp(f_exp) - math.exp(s_exp) + 20 + math.exp(1) 
	return f

def selecao(individuos, aptidao):
	pais = []
	v1 = 0.9
	for i in range(len(individuos)):
		p = random.sample(range(0, len(individuos)), 2)
		if (aptidao[p[0]] > aptidao[p[1]]):
			v2 = random.random()
			if(v2 < v1): #variabilidade
				pais.append(individuos[p[1]])
			else:
				pais.append(individuos[p[0]])
		else:
			v2 = random.random()
			if(v2 < v1):
				pais.append(individuos[p[0]])
			else:
				pais.append(individuos[p[1]])
	return pais

def cruzamento(pais, tam_individuo):
	filhos = []
	pais1 = []
	pais2 = []
	for i in range(0, len(pais), 2):
		pais1.append(pais[i])
		pais2.append(pais[i+1])
	for a, b in zip(pais1, pais2):
		filho1 = a[0:int(tam_individuo/2)] + b[int(tam_individuo/2):(tam_individuo)]
		filho2 = b[0:int(tam_individuo/2)] + a[int(tam_individuo/2):(tam_individuo)]
		filhos.append(filho1)
		filhos.append(filho2)
	return filhos

def mutacao(filhos):
	taxa_mutacao = 0.1
	for i in range(len(filhos)):
		for j in range(len(filhos[i])):
			m = random.random()
			if(m < taxa_mutacao):
				if(filhos[i][j] == 0):
					filhos[i][j] = 1
				else:
					filhos[i][j] = 0
	return filhos

def escolha_populacao_intermediaria(pais, filhos, xmin, xmax, n, tam_individuo):
	aptidaopais = []
	for i in pais:
		iconvertido = converter_binario(i, xmin, xmax, n, tam_individuo)
		fo = funcao_objetivo(iconvertido)
		aptidaopais.append(fo)
	#substitui um dos valores dos filhos pelo melhor pai
	pfilho = random.randint(0, len(filhos)-1)
	filhos.pop(pfilho)
	filhos.append(pais[aptidaopais.index(min(aptidaopais))])
	return filhos
			