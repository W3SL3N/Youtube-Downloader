import os, platform

class Cabecalho:

    def cabecalho(self, titulo):
        op = platform.system().lower()

        if op == 'windows':
            os.system('cls')

        else:
            os.system('clear')

        amarelo = '\033[1;33m'
        reset = '\033[0;0m'

        titulos = amarelo + f'{titulo}' + reset

        print('=' * 70)
        print('\n' + 'Youtube Donwloader'.center(70, ' '))
        print('\n' + '=' * 70)
        print(f'[{titulos}]'.center(82, ' '))
        print('=' * 70 + '\n')
