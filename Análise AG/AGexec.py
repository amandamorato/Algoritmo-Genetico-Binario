import AGreal as ag
import matplotlib.pyplot as plt
#import plotly.express as px

def principal(taxa_cruzamento, elitismo, taxa_mutacao, blx, num_geracoes, tam_populacao):
	#gerar população
	xmin = -2
	xmax = 2
	tam_individuo = 3
	melhoresindividuos = []
	melhoresfos = []
	individuos = ag.gera_populacao(tam_populacao, tam_individuo)
	#avaliar individuos
	for i in range(num_geracoes):
		aptidao = []
		for j in individuos:
			aptidao.append(ag.funcao_objetivo(j))
		melhoresindividuos.append(individuos[aptidao.index(min(aptidao))])
		melhoresfos.append(min(aptidao))
		#seleção
		pais = ag.selecao_roleta(individuos, aptidao)
		#cruzamento 
		filhos = ag.cruzamento(pais, tam_individuo, blx, taxa_cruzamento)
		#mutação
		filhos = ag.mutacao(filhos,taxa_mutacao)
		#escolha da população intermediária
		individuos = ag.escolha_populacao_intermediaria(pais, filhos, tam_individuo, elitismo)
		
	#retorna o melhor individuo da ultima geração
	print("Melhor indivíduo:", melhoresindividuos[-1])
	print("FO:",melhoresfos[-1])


#plotar resultado
'''
fig = px.line(y = melhoresfos, custom_data = [melhoresindividuos])
fig.update_traces(textposition="bottom right", 
	hovertemplate="<br>".join([
        "Geração: %{x}",
        "Melhor FO: %{y}",
        "Indivíduo: [%{customdata[0]}]"
    ]))
fig.update_yaxes(	)
fig.update_layout(xaxis_title='Geração', yaxis_title='Valor da Função Objetivo')
fig.update_layout(title={
    'text' : 'Melhores Indivíduos em Cada Geração',
    'y': 0.99,
    'x': 0.5,
	'font':dict(
            family="Arial",
            size=25
            )
})          	
fig.show()
'''