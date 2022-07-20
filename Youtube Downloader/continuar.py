import os

class Continuar:

    def continuar(self, classe):
        amarelo = '\033[1;33m'
        reset = '\033[0;0m'
        
        condicao = 0
        while condicao == 0:
            sim = ['sim', 's']
            nao = ['não', 'nao', 'n']

            continuar = input('\n\nContinuar baixando?' + (amarelo + '(S/n)' + reset) + ': ').lower().strip()

            if continuar in sim:
                a = classe()
                condicao += 1

            if continuar in nao:
                os.system(command=exit())

    def tentar_novamente(self, classe):
        amarelo = '\033[1;33m'
        reset = '\033[0;0m'        
        
        condicao = 0
        while condicao == 0:
            sim = ['sim', 's']
            nao = ['não', 'nao', 'n']

            continuar = input('\n\nTentar novamente?' + (amarelo + '(S/n)' + reset) + ': ').lower().strip()

            if continuar in sim:
                a = classe()
                condicao += 1

            if continuar in nao:
                os.system(command=exit())
               
            else:
                continue
