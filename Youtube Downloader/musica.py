from urllib.error import URLError
from http.client import IncompleteRead, RemoteDisconnected
import pytube.exceptions
from pytube import YouTube, Playlist
import time, sys, re

from diretorio import Diretorio
from progresso import Progresso
from continuar import Continuar
from cabecalho import Cabecalho

class Musica(Cabecalho):

    def __init__(self):
        self.cabecalho(titulo='músicas')
        self.mus_play()

    @staticmethod
    def mus_play():
        
        amarelo = '\033[1;33m'
        reset = '\033[0;0m'

        sim = ['sim', 's']
        nao = ['nao', 'não', 'n']

        cond = 0

        while cond == 0:

            define = input(' ' * 17 + 'Você vai baixar uma playlist?' + (amarelo + '(S/n)' + reset) + ': ')\
                                                                                            .lower().strip()

            if define in sim:
                playlist = PlaylistMus()
                cond += 1
                
            if define in nao:
                musica = UmaMusica()
                cond += 1
                
            else:
                continue

class UmaMusica(Continuar, Diretorio, Progresso, Cabecalho):

    def __init__(self):
        self.cabecalho(titulo='músicas')
        self.url = input('Insira a URL: ').strip()

        try:
            dict = YouTube(self.url).streams.filter(only_audio=True).order_by('abr').itag_index

        except URLError:
            print('\nVerifique sua conexão e tente novamente...')
            time.sleep(2)
            musica = UmaMusica()

        except pytube.exceptions.RegexMatchError:
            print('\nURL inválida! Verifique e tente novamente...\n\n')
            time.sleep(2)
            musica = UmaMusica()

        except pytube.exceptions.ExtractError:
            print('\nURL inválida! Verifique e tente novamente...\n\n')
            time.sleep(2)
            musica = UmaMusica()

        except KeyError:
            print('\nConteúdo restrito...\n')
            time.sleep(2)
            musica = UmaMusica()

        except pytube.exceptions.VideoPrivate:
            print('\nConteúdo restrito...\n')
            time.sleep(2)
            musica = UmaMusica()

        else:
            self.qualidades(dict=dict)
            self.baixar(url=self.url, qualidade=self.opcao(dict=dict))
            self.continuar(classe=UmaMusica)

    def qualidades(self, dict):
        print(f'\nTítulo: {YouTube(self.url).title}')

        print('\nQualidades disponíveis:\n')

        for itag in dict.keys():
            linha = dict[itag]
            padrao = '(")[\d]{2,3}(kbps)(")'
            procura = re.search(padrao, str(linha))
            sys.stdout.write(f'|{procura.group()}'.replace('"', ' '))
        sys.stdout.write('|\n\n')

    def opcao(self, dict):

        opcoes = []
        for itag in dict.keys():
            linha = dict[itag]
            padrao = '(")[\d]{2,3}(kbps)(")'
            procura = re.search(padrao, str(linha))
            opcoes.append(procura.group().replace('"',''))

        cond = 0

        while cond == 0:
            opcao = input('Entre com a qualidade desejada: ')
            opcao = f'{opcao.removesuffix("kbps")}kbps'

            if opcao in opcoes:
                cond += 1

            else:
                continue

        return opcao

    def baixar(self, url, qualidade):
        diretorio = self.diretorio(nome='Músicas')

        print('\n', end='')

        nome = YouTube(url).title
        nome = nome.replace('"', '“').replace("'", "′").replace('/', ' ').replace('|', ' ').replace('~', '-')

        try:
            YouTube(url, self.em_progresso)\
                .streams.filter(abr=qualidade).first()\
                .download(output_path=diretorio, filename=f'{nome}.mp3', max_retries=5)

        except IncompleteRead:
            print('Download incompleto, verifque sua conexão e tente novamente...')
            self.tentar_novamente(classe=UmaMusica)

        except RemoteDisconnected:
            print('\nConexão perdida inesperadamente, verifque sua conexão e tente novamente...', end='')
            self.tentar_novamente(classe=UmaMusica)

        except URLError:
            print('\nO download não pôde iniciar, verifque sua conexão e tente novamente...', end='')
            self.tentar_novamente(classe=UmaMusica)


class PlaylistMus(Continuar, Progresso, Diretorio, Cabecalho):

    def __init__(self):
        self.cabecalho(titulo='músicas-playlists')
        self.url = input('Insira a URL: ')

        try:
            Playlist(self.url).length #Isso está aqui apenas para a verificação da url.

        except URLError:
            print('\nVerifique sua conexão e tente novamente...')
            time.sleep(2)
            playlist = PlaylistMus()

        except KeyError:
            print('\nURL inválida! Verifique e tente novamente...')
            time.sleep(2)
            playlist = PlaylistMus()

        except pytube.exceptions.ExtractError:
            print('\nURL inválida! Verifique e tente novamente...')
            time.sleep(2)
            playlist = PlaylistMus()

        else:
            urls = Playlist(self.url).video_urls
            self.baixar(urls=urls)
            self.continuar(classe=PlaylistMus)

    def baixar(self, urls):
        diretorio = self.diretorio(nome='Músicas')

        print('\n', end='')

        for url in urls:

            nome = YouTube(url).title

            nome = nome.replace('"', '“').replace("'", "′").replace('/', ' ').replace('~', '-').replace('|', ' ')

            print('-' * 70)
            print(f'\n{nome}\n')
            try:
                YouTube(url, self.em_progresso).streams.filter(only_audio=True)\
                    .order_by(attribute_name='abr').last()\
                    .download(filename=f'{nome}.mp3', output_path=diretorio)
                print('\n')

            except KeyError:
                print('\nConteúdo restrito...\n')

            except IncompleteRead:
                print('\n\nDownload incompleto, verifque sua conexão e tente novamente...', end='')
                self.tentar_novamente(classe=PlaylistMus)

            except URLError:
                print('\n\nDownload incompleto, verifque sua conexão e tente novamente...', end='')
                self.tentar_novamente(classe=PlaylistMus)

            except RemoteDisconnected:
                print('\n\nConexão perdida inesperadamente.\n'
                      'verifque sua conexão e tente novamente...', end='')
                self.tentar_novamente(classe=PlaylistMus)
