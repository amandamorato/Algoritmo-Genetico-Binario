import AGbinario as ag
import plotly.express as px

tam_populacao = 100
tam_individuo = 12
num_geracoes = 40
xmin = -2
xmax = 2
n = 6

#gerar população
melhoresindividuos = []
melhoresfos = []
individuos = ag.gera_populacao(tam_populacao, tam_individuo)
#avaliar individuos
for i in range(num_geracoes):
	aptidao = []
	for j in individuos:
		iconvertido = ag.converter_binario(j, xmin, xmax, n, tam_individuo)
		fo = ag.funcao_objetivo(iconvertido)
		aptidao.append(fo)
	melhoresindividuos.append(individuos[aptidao.index(min(aptidao))])
	melhoresfos.append(min(aptidao))
	#seleção
	pais = ag.selecao(individuos, aptidao)
	#cruzamento 
	filhos = ag.cruzamento(pais, tam_individuo)
	#mutação
	filhos = ag.mutacao(filhos)
	#escolha da população intermediária
	individuos = ag.escolha_populacao_intermediaria(pais, filhos, xmin, xmax, n, tam_individuo)
	
#retorna o melhor individuo da ultima geração
print("Melhor indivíduo:", melhoresindividuos[-1])
print("FO:",melhoresfos[-1])

#plotar resultado
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
