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
        verde = '\033[0;32m'
        reset = '\033[0;0m'
        
        mbs_baixados = f'{int(baixado)}/{int(filesize)}'

        # barra de progresso ----------------------------------------------------
        progresso = (filesize - bytes_restantes) / (filesize)
        colunas = int(60 * progresso)
        status = (verde + '█' + reset) * colunas + '▒' * (43 - colunas)
        # -----------------------------------------------------------------------
        
        porcentagem = f'{baixado/filesize:0.2%}'

        barra = f'[ {mbs_baixados:^10}MB ] |{status}| {porcentagem}\r'

        sys.stdout.write(barra)
        sys.stdout.flush()
