import AGexec

taxa_cruzamento = [0.6, 0.8, 1]
elitismo = [0, 1]
taxa_mutacao = [0.01, 0.05, 0.1]
blx = [1, 2]
num_geracoes = [25, 50, 100]
tam_populacao = [26, 50, 100]
for a in taxa_cruzamento:
    for b in elitismo:
        for c in taxa_mutacao:
            for d in blx:
                for e in num_geracoes:
                    for f in tam_populacao:
                        AGexec.principal(a, b, c, d, e, f)
