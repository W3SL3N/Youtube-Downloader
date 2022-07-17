import os

class Cabecalho:

    def cabecalho(self, titulo):
        os.system('cls')
        print('=' * 70)
        print('\n' + 'Youtube Donwloader'.center(70, ' '))
        print('\n' + '=' * 70)
        print(f'[{titulo}]'.center(70, ' '))
        print('=' * 70 + '\n')
