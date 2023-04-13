import pandas as pd

class Funcionario:
    
    def __init__(self, nome, cpf, idade, funcao, salario, dt_adimissao):

        # Declaração das variáveis da classe.
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.funcao = funcao
        self.salario = salario
        self.dt_adimissao = dt_adimissao

        # Cadastrando o funcionario no excel.
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

    # Função que apaga um funcionário do excel.
    def excluindo(self, nome):
        banco = pd.read_excel("banco_de_dados.xlsx")
        nomes = []

        for linha in banco["NOME"]:
            nomes.append(linha)

        if nome in nomes:
            print("Obaa")
            print(nomes.index(nome))
            banco.drop(nomes.index(nome), inplace=True)
        else:
            print("Nome ainda não cadastrado!")

        banco.to_excel("banco_de_dados.xlsx", na_rep="#N/A", header= True, index=False)

    def verifica_perfil():
        pass


