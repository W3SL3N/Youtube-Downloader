import sys
import time

class Progresso:

    def em_progresso(self, stream, chunk, bytes_remaining):

        # conversão de bytes para MB--------------------------------------------
        filesize = stream.filesize / (1024 * 1024)
        bytes_restantes = bytes_remaining / (1024 * 1024)
        baixado = filesize - bytes_restantes
        # ----------------------------------------------------------------------
        self.barra_de_progresso(filesize=filesize, bytes_restantes=bytes_restantes, baixado=baixado)

    def barra_de_progresso(self, filesize, bytes_restantes, baixado):

        porcentagem = f'{baixado/filesize:0.2%}'

        # barra de progresso ----------------------------------------------------
        progresso = (filesize - bytes_restantes) / (filesize)
        colunas = int(60 * progresso)
        status = '█' * colunas + '▒' * (60 - colunas)
        # -----------------------------------------------------------------------

        barra = f'|{status}|{porcentagem:>8}\r'

        sys.stdout.write(barra)
        sys.stdout.flush()
