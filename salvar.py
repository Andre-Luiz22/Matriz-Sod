import pandas as pd

def cadastrando(nome, matricula, idade, turma):
    banco = pd.read_excel("testezin.xlsx")
    def cadastrar():
        cadastro = pd.DataFrame(data={"NOME":[nome],
                                "MATRICULA":[matricula],
                                "IDADE":[int(idade)],
                                "TURMA":[turma]})

        print(f"{nome}, cadastrado com sucesso!")

        return cadastro
    banco = pd.concat([banco, cadastrar()], ignore_index= False)
    banco.reset_index(drop=True, inplace=True)
    banco.to_excel("testezin.xlsx", na_rep="#N/A", header= True, index=False)






cadastrando("Shayene Carolina Vieira", 654321987, 31, "13B")
cadastrando("Daniel da Silva de Sá", 167892321, 22, "13A")
cadastrando("Bruno Damasceno", 167751361, 21, "13F")
cadastrando("Rodrigo Cazemiro Orlando", 199955561, 20, "11F")




