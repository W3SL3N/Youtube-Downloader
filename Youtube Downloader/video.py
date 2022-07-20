from urllib.error import URLError
from http.client import IncompleteRead,RemoteDisconnected
from pytube import YouTube, Playlist
import pytube.exceptions
import time, sys, re

from diretorio import Diretorio
from progresso import Progresso
from continuar import Continuar
from cabecalho import Cabecalho

class Video(Cabecalho):
    def __init__(self):
        self.cabecalho(titulo='vídeos')
        self.vid_play()

    @staticmethod
    def vid_play():

        amarelo = '\033[1;33m'
        reset = '\033[0;0m'     
   
        sim = ['sim', 's']
        nao = ['nao', 'não', 'n']

        cond = 0

        while cond == 0:

            define = input(' ' * 17 + 'Você vai baixar uma playlist?' + (amarelo + '(S/n)' + reset) + ': ')\
                                                                                            .lower().strip()

            if define in sim:
                playlist = PlaylistVid()
                cond += 1
                
            if define in nao:
                musica = UmVideo()
                cond += 1
                
            else:
                continue

class UmVideo(Continuar, Diretorio, Progresso, Cabecalho):

    def __init__(self):
        self.cabecalho(titulo='vídeos')
        self.url = input('Insira a URL: ').strip()

        try:
            dict = YouTube(self.url).streams.filter(progressive=True).itag_index

        except URLError:
            print('\nVerifique sua conexão e tente novamente...')
            time.sleep(2)
            video = UmVideo()

        except pytube.exceptions.RegexMatchError:
            print('\nURL inválida! Verifique e tente novamente...\n\n')
            time.sleep(2)
            video = UmVideo()

        except pytube.exceptions.ExtractError:
            print('\nURL inválida! Verifique e tente novamente...\n\n')
            time.sleep(2)
            video = UmVideo()

        except KeyError:
            print('\nConteúdo restrito...\n')
            time.sleep(2)
            video = UmVideo()

        except pytube.exceptions.VideoPrivate:
            print('\nConteúdo restrito...\n')
            time.sleep(2)
            video = UmVideo()

        except pytube.exceptions.ExtractError:
            print('\nURL inválida! Verifique e tente novamente...')
            time.sleep(2)
            video = UmVideo()

        else:
            self.qualidades(dict=dict)
            self.baixar(url=self.url, resolucao=self.opcao(dict=dict))
            self.continuar(classe=UmVideo)

    def qualidades(self, dict):
        print(f'\nTítulo: {YouTube(self.url).title}')

        print('\nQualidades disponíveis:\n')

        for itag in dict.keys():
            linha = dict[itag]
            padrao = '(")[\d]{3,4}(p)(")'
            procura = re.search(padrao, str(linha))
            sys.stdout.write(f'|{procura.group()}'.replace('"', ' '))
        sys.stdout.write('|\n\n')

    def opcao(self, dict):

        opcoes = []
        for itag in dict.keys():
            linha = dict[itag]
            padrao = '(")[\d]{3,4}(p)(")'
            procura = re.search(padrao, str(linha))
            opcoes.append(procura.group().replace('"',''))

        cond = 0

        while cond == 0:
            opcao = input('Entre com a qualidade desejada: ')
            opcao = f'{opcao.removesuffix("p")}p'

            if opcao in opcoes:
                cond += 1

            else:
                continue

        return opcao

    def baixar(self, url, resolucao):

        diretorio = self.diretorio(nome='Vídeos')

        print('\n', end='')

        try:
            YouTube(url, self.em_progresso)\
                .streams.get_by_resolution(resolucao)\
                .download(output_path=diretorio)

        except IncompleteRead:
            print('\n\nDownload incompleto, verifque sua conexão e tente novamente...', end='')
            self.tentar_novamente(classe=UmVideo)

        except RemoteDisconnected:
            print('\n\nConexão perdida inesperadamente, verifque sua conexão e tente novamente...', end='')
            self.tentar_novamente(classe=UmVideo)

        except URLError:
            print('\n\nVerifque sua conexão e tente novamente...', end='')
            self.tentar_novamente(classe=UmVideo)


class PlaylistVid(Continuar, Diretorio, Cabecalho, Progresso):

    def __init__(self):
        self.cabecalho(titulo='vídeos-playlists')
        self.url = input('Insira a URL: ').strip()

        try:
            Playlist(self.url).length #Isso está aqui apenas para a verificação da url.

        except URLError:
            print('\nVerifique sua conexão e tente novamente...')
            time.sleep(2)
            playlist = PlaylistVid()

        except KeyError:
            print('\nURL inválida! Verifique e tente novamente...')
            time.sleep(2)
            playlist = PlaylistVid()

        except pytube.exceptions.ExtractError:
            print('\nURL inválida! Verifique e tente novamente...')
            time.sleep(2)
            playlist = PlaylistVid()

        else:
            urls = Playlist(self.url).video_urls
            self.baixar(urls=urls)
            self.continuar(classe=PlaylistVid)

    def baixar(self, urls):
        diretorio = self.diretorio(nome='Vídeos')

        print('\n', end='')

        for url in urls:

            nome = YouTube(url).title

            nome = nome.replace('"', '“').replace("'", "′").replace('/', ' ').replace('~', '-')

            print('-' * 70)
            print(f'\n{nome}\n')
            try:
                YouTube(url, self.em_progresso).streams.get_highest_resolution()\
                    .download(output_path=diretorio, max_retries=5)
                print('\n')

            except KeyError:
                print('\nConteúdo restrito...\n')

            except IncompleteRead:
                print('\n\nDownload incompleto, verifque sua conexão e tente novamente...', end='')
                self.tentar_novamente(classe=PlaylistVid)

            except URLError:
                print('\n\nDownload incompleto, verifque sua conexão e tente novamente...', end='')
                self.tentar_novamente(classe=PlaylistVid)

            except RemoteDisconnected:
                print('\n\nConexão perdida inesperadamente.\n'
                      'Verifque sua conexão e tente novamente...', end='')
                self.tentar_novamente(classe=PlaylistVid)
