# coding: utf-8
import csv
# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 
def q_1():
    with open("data.csv", "r") as input:
        n = []
        index = -1
        field = "nationality"
        data = csv.reader(input)
        for i in data:
            index = i.index(field)
            break
        for i in data:
            if i[index] not in n:
                n.append(i[index])
        return len(n)


# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    with open("data.csv", "r") as input:
        n = []
        index = -1
        field = "club"
        data = csv.reader(input)
        for i in data:
            index = i.index(field)
            break
        for i in data:
            if i[index] not in n:
                n.append(i[index])
        return len(n)

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    with open("data.csv", "r") as input:
        n = []
        index = -1
        field = "full_name"
        data = csv.reader(input)
        for i in data:
            index = i.index(field)
            break
        for i in data:
            if len(n) == 20:
                break
            else:
                n.append(i[index])
        return n

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    with open("data.csv", "r") as input:
        n = []
        array = []
        index_wage = -1
        index_name = -1
        wage = "eur_wage"
        name = "full_name"
        data = csv.reader(input)
        for i in data:
            index_wage = i.index(wage)
            index_name = i.index(name)
            break
        n = sorted(data, key=lambda dado: float(dado[index_wage]), reverse=True)

        for i in n[0:10]:
            array.append(i[index_name])
        return array

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    with open("data.csv", "r") as input:

        with open("data.csv", "r") as input:
            n = []
            array = []
            index_age = -1
            index_name = -1
            age = "age"
            name = "full_name"
            data = csv.reader(input)
            for i in data:
                index_age = i.index(age)
                index_name = i.index(name)
                break
            n = sorted(data, key=lambda dado: int(dado[index_age]), reverse=True)

            for i in n[0:10]:
                array.append(i[index_name])
            return array

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    with open("data.csv", "r") as input:
        d = {}
        index_age = -1
        index_name = -1
        age = "age"
        name = "full_name"
        data = csv.reader(input)
        for i in data:
            index_age = i.index(age)
            index_name = i.index(name)
            break
        for i in data:
            try:
                d[int(i[index_age])] = d[int(i[index_age])] + 1
            except:
                d[int(i[index_age])] = 1
        return d


