import os

class Continuar:

    def continuar(self, classe):
        condicao = 0
        while condicao == 0:
            sim = ['SIM', 'S', 'YES', 'Y']
            nao = ['NAO', 'NÃO', 'NO', 'N']

            continuar = input('\n\nContinuar baixando?(S/n): ').upper().strip()

            if continuar in sim:
                a = classe()
                condicao += 1

            if continuar in nao:
                os.system(command=exit())

    def tentar_novamente(self, classe):
        condicao = 0
        while condicao == 0:
            sim = ['SIM', 'S', 'YES', 'Y']
            nao = ['NAO', 'NÃO', 'NO', 'N']

            continuar = input('\n\nTentar novamente?(S/n): ').upper().strip()
            print(' ')

            if continuar in sim:
                a = classe()
                condicao += 1

            if continuar in nao:
                os.system(command=exit())
