import os

class Diretorio():

    @staticmethod
    def existe_disco(disco):

        procura = disco[0:3]

        existe = os.path.isdir(procura)

        return existe

    @staticmethod
    def verifica_sintaxe(caminho):

        caracteres_proibidos = [':', '*', '?', '"', '<', '>', '|']
        compara = set(caminho[3:]) & set(caracteres_proibidos)

        if len(compara) > 0:
            return False
        else:
            return True

    def diretorio(self, nome):

        amarelo = '\033[1;33m'
        reset = '\033[0;0m'

        print(f'\nPasta padrão para o download: D:\YT Downloader\\{nome}')

        cond = 0

        while cond == 0:

            sim = ['sim', 's']
            nao = ['não', 'nao', 'n']
            pergunta = input('Mudar pasta?' + (amarelo + '(S/n)' + reset) + ': ').lower().strip()

            diretorio = f'D:\\YT Downloader\\{nome}'

            if pergunta in nao:
                return diretorio

            if pergunta in sim:
                cond = 0

                while cond == 0:

                    diretorio = (input(amarelo + '\n>>> ' + reset).strip())


                    existe_disco = Diretorio.existe_disco(diretorio)

                    if existe_disco:
                        verifica_sintaxe = Diretorio.verifica_sintaxe(diretorio)

                        if verifica_sintaxe == True:
                            return diretorio

                        else:
                            print('\nO nome da pasta não pode conter esses caracteres:', ':', '*', '?', '"', "'", '<', '>',
                                  '|')
                            continue

                    if not existe_disco:
                        print('\nO disco local informado não existe...')
                        continue

                    cond += 1

            else:
                continue

            cond += 1


