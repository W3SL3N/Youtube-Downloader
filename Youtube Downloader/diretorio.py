import os
from urllib.error import URLError
from http.client import IncompleteRead, RemoteDisconnected

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

        print(f'\nPasta padrão para o download: C:\YT Downloader\\{nome}')

        cond = 0

        while cond == 0:
            sim = ['sim', 's']
            nao = ['não', 'nao', 'n']
            pergunta = input('Mudar pasta? (S/n): ').lower().strip()

            diretorio = f'C:\\YT Downloader\\{nome}'

            if pergunta in nao:
                cond += 1

            if pergunta in sim:
                cond = 0

                while cond == 0:

                    diretorio = (input('\033[1;33m' + '\n>>> ' + '\033[0;0m').strip())

                    existe_disco = Diretorio.existe_disco(diretorio)

                    if existe_disco:
                        verifica_sintaxe = Diretorio.verifica_sintaxe(diretorio)

                        if verifica_sintaxe == True:
                            return diretorio
                            cond += 1
                        else:
                            print('\nO nome da pasta não pode conter esses caracteres:', ':', '*', '?', '"', "'", '<', '>',
                                  '|')
                            continue

                    if not existe:
                        print('\nO disco local informado não existe...')
                        continue

            else:
                continue

        return diretorio
