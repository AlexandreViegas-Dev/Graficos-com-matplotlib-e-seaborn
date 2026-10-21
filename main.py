import pandas as pd
import matplotlib.pyplot as mt
import numpy as np
import seaborn as sb

fig, ax = mt.subplots(figsize=(8,5))

opcao = None

while opcao != 0:

    print("Mostrar Dados",
    "1 - Barras",
    "2 - Boxplot",
    "3 - Dispersão",
    "4 - Distribuição",
    "5 - Frequência",
    "6 - Heatmap",
    "7 - Linhas",
    "8 - Pizza",
    "9 - Regressão",
    "0 - Sair"
    )

    opcao = int(input())

    match opcao:
        case 1:
            tabela = pd.read_csv("data/dados_barras.csv")

            sb.barplot(data = tabela, x = 'regiao', y = 'vendas_medias', hue = 'categoria')

            ax.set_title("Dados Barras", fontsize = 14, fontweight = "bold")
            ax.set_xlabel("Regiao", fontsize = 14)
            ax.set_ylabel("Vendas Medias", fontsize = 11)
            ax.legend(title = "Categoria", frameon=True)

            mt.show()

        case 2:
            tabela = pd.read_csv("data/dados_boxplot.csv")

            sb.boxplot(data = tabela, x = 'departamento', y = 'salario')
            ax.set_title("Dados Boxplot", fontsize = 14, fontweight = "bold")
            ax.set_xlabel("Departamento", fontsize = 14)
            ax.set_ylabel("Salario", fontsize = 11)
            ax.legend(title = "Categoria", frameon=True)

            mt.show()


        case 3:
            tabela = pd.read_csv("data/dados_dispersao.csv")

            sb.stripplot(data = tabela, x = 'altura_cm', y = 'peso_kg', hue = 'sexo')

            ax.set_title("Dados Stripplot", fontsize = 14, fontweight = "bold")
            ax.set_xlabel("Altura (cm)", fontsize = 14)
            ax.set_ylabel("Peso (kg)", fontsize = 11)
            ax.legend(title = "Sexo", frameon=True)

            mt.show()

        case 4:
            tabela = pd.read_csv("data/dados_distribuicao.csv")

            sb.histplot(data = tabela, x = 'idade')

            ax.set_title("Dados Distribuição", fontsize = 14, fontweight = "bold")
            ax.set_xlabel("Id Cliente", fontsize = 14)
            ax.set_ylabel("Idade", fontsize = 11)

            mt.show()

        case 5:
            tabela = pd.read_csv("data/dados_frequencia.csv")
            
            sb.countplot(data = tabela, x = 'tipo_atendimento', hue = 'tipo_atendimento')

            ax.set_title("Dados Frequência", fontsize = 14, fontweight = "bold")
            ax.set_xlabel("Id Chamado", fontsize = 14)
            ax.set_ylabel("Tipo de Atendimento", fontsize = 11)

            mt.show()


        case 6:
            tabela = pd.read_csv("data/dados_heatmap.csv")

            tabela = tabela.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
            ordem_dias=["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
            tabela = tabela.reindex([d for d in ordem_dias if d in tabela.index])
            
            sb.heatmap(tabela, annot=True, fmt=".2f")

            # ax.set_title("Dados Heatmap", fontsize = 14, fontweight = "bold")
            # ax.set_xlabel("Id Chamado", fontsize = 14)
            # ax.set_ylabel("Tipo de Atendimento", fontsize = 11)

            mt.show()

        case 7:
            tabela = pd.read_csv("data/dados_linhas.csv")

            sb.lineplot(data = tabela, x = "data", y = "vendas", hue = "loja")

            ax.set_title("Dados Linhas", fontsize = 14, fontweight = "bold")
            ax.set_xlabel("Id Chamado", fontsize = 14)
            ax.set_ylabel("Tipo de Atendimento", fontsize = 11)

            mt.show()

        case 8:
            tabela = pd.read_csv("data/dados_pizza.csv")

            mt.pie(data = tabela, x = "faturamento", labels="canal_venda")
            mt.legend(title="Canal de Venda", frameon=True)

            mt.show()

        case 9:
            tabela = pd.read_csv("data/dados_regressao.csv")

            sb.regplot(data = tabela, x = "renda_mensal", y = "gasto_mensal")
            ax.set_title("Dados Regressão", fontsize = 14, fontweight = "bold")
            ax.set_xlabel("Renda Mensal", fontsize = 14)
            ax.set_ylabel("Gasto Mensal", fontsize = 11)

            mt.show()