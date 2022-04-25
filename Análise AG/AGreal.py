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
			individuo.append(random.uniform(-2,2))
		individuos.append(individuo)
	return individuos

def funcao_objetivo(x):
	n = float(len(x))
	f_exp = -0.2 * math.sqrt(1/n * sum(np.power(x, 2)))
	t = 0
	for i in range(0, len(x)):
		t += np.cos(2 * math.pi * x[i])
	s_exp = 1/n * t
	f = -20 * math.exp(f_exp) - math.exp(s_exp) + 20 + math.exp(1) 
	return f

def selecao_roleta(individuos, aptidao):
	fitr = []
	roleta = []
	pais = []
	for i in aptidao:
		fitr.append(1/i)
	for i in fitr:
		roleta.append(i/sum(fitr))
	for i in range(len(individuos)):
		r = random.random()
		for j in range(len(roleta)):
			r = r - roleta[j]
			if r <= 0:
				pais.append(individuos[j])
				break
	return pais

def cruzamento(pais, tam_individuo, blx, taxa_cruzamento):
	filhos = []
	pais1 = []
	pais2 = []
	for i in range(0, len(pais), 2):
		pais1.append(pais[i])
		pais2.append(pais[i+1])
	for a, b in zip(pais1, pais2):
		filho1 = []
		filho2 = []
		#blxAlpha
		if (blx == 1):
			alpha = 0.5
			for i in range(tam_individuo):
				d = abs(a[i]-b[i])
				#primeiro filho
				u1 = random.uniform((min(a[i], b[i]) - alpha * d), (max(a[i], b[i]) + alpha * d))
				if u1 > 2 or u1 < -2:
					u1 = random.uniform(-2, 2)
				filho1.append(u1)
				#segundo filho
				u2 = random.uniform((min(a[i], b[i]) - alpha * d), (max(a[i], b[i]) + alpha * d))
				if u2 > 2 or u2 < -2:
					u2 = random.uniform(-2, 2)
				filho2.append(u2)
			filhos.append(filho1)
			filhos.append(filho2)
		#blxAlphaBeta
		elif (blx == 2):
			alpha = 0.75
			beta = 0.25
			for i in range(tam_individuo):
				d = abs(a[i]-b[i])
				if (a[i] <= b[i]):
					u1 = random.uniform(a[i] - alpha * d, b[i] + beta * d)
					filho1.append(u1)
					u2 = random.uniform(a[i] - alpha * d, b[i] + beta * d)
					filho2.append(u2)
				else: 
					u1 = random.uniform(b[i] - beta * d, a[i] + alpha * d)
					filho1.append(u1)
					u2 = random.uniform(b[i] - beta * d, a[i] + alpha * d)
					filho2.append(u2)
			filhos.append(filho1)
			filhos.append(filho2)
		for i in range(int(1 - taxa_cruzamento)*len(filhos)):
			pfilho = random.randind(0, len(filhos)-1)
			filhos.pop(pfilho)
			filhos.append(pais[pfilho])
	return filhos

def mutacao(filhos, taxa_mutacao):
	for i in range(len(filhos)):
		for j in range(len(filhos[i])):
			m = random.random()
			if(m < taxa_mutacao):
				mut = random.uniform(-0.1, 0.1)
				filhos[i][j] = filhos[i][j] * mut 
	return filhos

def escolha_populacao_intermediaria(pais, filhos, tam_individuo, elitismo):
	aptidaopais = []
	for i in pais:
		aptidaopais.append(funcao_objetivo(i))
	#substitui um dos valores dos filhos pelo melhor pai
	if(elitismo == 1):
		pfilho = random.randint(0, len(filhos)-1)
		filhos.pop(pfilho)
		filhos.append(pais[aptidaopais.index(min(aptidaopais))])
	return filhos
			