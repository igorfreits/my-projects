import matplotlib.pyplot as plt
from data import lista_de_carros, placa_generate, cpf_generate, id
from time import sleep
from datetime import datetime, timedelta
from random import randint
from typing import Dict, List
import json


class estacionamento:
    def __init__(self):

        self.vaga = {
            'parking1': {'Vaga': 1, 'Nome': None, 'CPF': None,
                         'ID': None, 'Status': 'Livre',
                         'Carro': None, 'Placa': None,
                         'Entrada': None},
            'parking2': {'Vaga': 2, 'Nome': None, 'CPF': None,
                         'ID': None, 'Status': 'Livre',
                         'Carro': None, 'Placa': None,
                         'Entrada': None},
            'parking3': {'Vaga': 3, 'Nome': None, 'CPF': None,
                         'ID': None, 'Status': 'Livre',
                         'Carro': None, 'Placa': None,
                         'Entrada': None},
            'parking4': {'Vaga': 4, 'Nome': None, 'CPF': None,
                         'ID': None, 'Status': 'Livre',
                         'Carro': None, 'Placa': None,
                         'Entrada': None},
            'parking5': {'Vaga': 5, 'Nome': None, 'CPF': None,
                         'ID': None, 'Status': 'Livre',
                         'Carro': None, 'Placa': None,
                         'Entrada': None},
            'parking6': {'Vaga': 6, 'Nome': None, 'CPF': None,
                         'ID': None, 'Status': 'Livre',
                         'Carro': None, 'Placa': None,
                         'Entrada': None},
            'parking7': {'Vaga': 7, 'Nome': None, 'CPF': None,
                         'ID': None, 'Status': 'Livre',
                         'Carro': None, 'Placa': None,
                         'Entrada': None},
            'parking8': {'Vaga': 8, 'Nome': None, 'CPF': None,
                         'Id': None, 'Status': 'Livre',
                         'Carro': None, 'Placa': None,
                         'Entrada': None},
            'parking9': {'Vaga': 9, 'Nome': None, 'CPF': None,
                         'Id': None, 'Status': 'Livre',
                         'Carro': None, 'Placa': None,
                         'Entrada': None},
            'parking10': {'Vaga': 10, 'Nome': None, 'CPF': None,
                          'Id': None, 'Status': 'Livre',
                          'Carro': None, 'Placa': None,
                          'Entrada': None}
        }
        self.money = 0
        self.entrada = 0

    def adicionar_carro(self, nome, cpf, carro, placa, codigo):

        self.nome = nome
        self.carro = carro
        self.placa = placa
        self.cpf = cpf
        self.id = codigo

        data = datetime.now()

        for x in range(1, len(self.vaga)+1):
            if self.vaga[f'parking{x}']['Status'] == 'Livre':
                self.vaga[f'parking{x}']['Status'] = 'Ocupado'
                self.vaga[f'parking{x}']['Nome'] = self.nome
                self.vaga[f'parking{x}']['Carro'] = self.carro
                self.vaga[f'parking{x}']['Placa'] = self.placa
                self.vaga[f'parking{x}']['CPF'] = self.cpf
                self.vaga[f'parking{x}']['ID'] = self.id
                self.vaga[f'parking{x}']['Entrada'] = data

                print(
                    f"\033[32m{'A vaga ':->20}{x}{' foi ocupada':-<19}\033[m")
                self.entrada += 1
                break
        else:
            print(
                f'\033[31m{"Todas as vagas estão ocupadas":-^40}\033[m')
            sleep(0.5)

    def vagas(self):
        a = 1
        while a <= len(self.vaga):
            for x, y in self.vaga[f'parking{a}'].items():
                print(f"{x}-\033[35m{y}\033[m")
            print()
            a += 1
        else:
            sleep(2)

    def remover_carro(self, vaga=0):
        for x in range(1, len(self.vaga)+1):
            if self.vaga[f'parking{x}']['Status'] == 'Ocupado':
                self.vagas()
                sleep(2)

                remover = str(
                    input('Digite o nome da vaga que você quer remover o carro: '))
                if remover:
                    self.vaga[f'parking{remover}']['Status'] = 'Livre'
                    self.vaga[f'parking{remover}']['Carro'] = None
                    self.vaga[f'parking{remover}']['Placa'] = None
                    self.vaga[f'parking{remover}']['Nome'] = None
                    self.vaga[f'parking{remover}']['CPF'] = None
                    self.vaga[f'parking{remover}']['ID'] = None

                    entrada = self.vaga[f'parking{remover}']['Entrada']

                    saida = entrada + \
                        timedelta(minutes=randint(10, 180))

                    diferenca = saida - \
                        entrada

                    tempo = diferenca.seconds // 60

                    if tempo <= 30:
                        print(
                            f'\033[31mVocê ficou {tempo} minutos e terá que pagar R$7\033[m')
                        self.money += 7
                    elif tempo <= 60:
                        print(
                            f'\033[31mVocê ficou {tempo} minutos e terá que pagar R$15\033[m')
                        self.money += 15
                    elif tempo <= 90:
                        print(
                            f'\033[31mVocê ficou {tempo} minutos e terá que pagar R$25\033[m')
                        self.money += 30
                    elif tempo >= 120:
                        print(
                            f'\033[31mVocê ficou {tempo} minutos e terá que pagar R$35\033[m')
                        self.money += 35

                    self.vaga[f'parking{remover}']['Entrada'] = None

                    print(
                        f"\033[32m{'Vaga ':->20}{remover}{' liberada':-<19}\033[m")
                    break
        else:
            print(
                f'\033[32m{"Todas as vagas estão Livres!":-^40}\033[m')

    def liberar(self):
        for x in range(1, len(self.vaga)+1):
            self.vaga[f'parking{x}']['Status'] = 'Livre'
            self.vaga[f'parking{x}']['Nome'] = None
            self.vaga[f'parking{x}']['Carro'] = None
            self.vaga[f'parking{x}']['Placa'] = None
            self.vaga[f'parking{x}']['CPF'] = None
            self.vaga[f'parking{x}']['ID'] = None
        print(f'{"Todas as vagas foram liberadas!":-^40}')

    def relatorio_parking(self):
        date = datetime.now()
        print(
            f'\033[32m{"Relatório de estacionamento":-^40}\033[m\n'

            f'\n\033[1m-Data e hora atual: {date.strftime("%d/%m/%Y - %H:%M:%S")}\033[m\n'

            f'\033[1m-Total de dinheiro recebido: R${self.money}\033[m\n'

            f'\033[1m-Total de carros estacionados: {self.entrada}\033[m\n')

        try:
            with open('data/relatorio.json', 'r') as f:
                relatorio = json.load(f)
        except FileNotFoundError:
            relatorio = {}

        relatorio[date.strftime("%d/%m/%Y")] = {
            'Caixa': self.money}

        with open('data/relatorio.json', 'w') as f:
            json.dump(relatorio, f, indent=4)

        # Fazer grafico com os dados do json
        with open('data/relatorio.json', 'r') as f:
            relatorio = json.load(f)

        data = []
        caixa = []
        for x in relatorio:
            data.append(x)
            caixa.append(relatorio[x]['Caixa'])

        plt.plot(data, caixa)
        plt.title('Caixa do Parking')
        plt.xlabel('Data')
        plt.ylabel('Dinheiro')
        plt.show()


parking = estacionamento()
