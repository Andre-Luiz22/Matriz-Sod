import pandas as pd

# função que adiciona as dados no excel
def cadastrando(nome, cpf, idade, funcao, salario, dt_adimissao):
    banco = pd.read_excel("banco_de_dados.xlsx")
    def cadastrar():
        cadastro = pd.DataFrame(data={"NOME":[nome],
                                "CPF":[cpf],
                                "IDADE":[int(idade)],
                                "FUNÇÃO":[funcao],
                                "SALARIO":[salario],
                                "DT_ADMISSÃO":[dt_adimissao]})

        print(f"{nome}, cadastrado com sucesso!")

        return cadastro
    banco = pd.concat([banco, cadastrar()], ignore_index= False)
    banco.reset_index(drop=True, inplace=True)
    banco.to_excel("banco_de_dados.xlsx", na_rep="#N/A", header= True, index=False)

# função que apaga linhas no excel

def excluir(nome):
    banco = pd.read_excel("banco_de_dados.xlsx")
    nomes = []

    for linha in banco["NOME"]:
        nomes.append(linha)

    if nome in nomes:
        print("Obaa")
        print(nomes.index(nome))
        banco.drop(nomes.index(nome), inplace=True)
        print(banco)
    else:
        print("Nome ainda não cadastrado!")

    banco.to_excel("banco_de_dados.xlsx", na_rep="#N/A", header= True, index=False)

# f