# Youtube-Downloader
![Status do Projeto: Desenvolvimento](https://img.shields.io/badge/Status-Desenvolvimento-brightgreen)
![Meu Twitter](https://img.shields.io/twitter/url?label=%40W3SL3N&style=social&url=https%3A%2F%2Ftwitter.com%2FW3SL3N)

*Um script Python baseado em Pytube para o download de áudios, vídeos e playlists, do Youtube de maneira clara, amigável e objetiva.*

## Índice:
- [Funcionalidades](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#gear-funcionalidades)
- [Bibliotecas utilizadas](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#books-bibliotecas-utilizadas)
- [Acesso ao projeto](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#file_folder-acesso-ao-projeto)
- [Rodar o projeto](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#arrow_forward-rodar-o-projeto)
- [Aviso importante](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#warning-aviso-importante)
- [Obejtivos do projeto](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#jigsaw-obejtivos-do-projeto)
- [Tecnologias utilizadas](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#hammer_and_wrench-tecnonologias-utilizadas)
- [Script em funcionamento](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#fast_forward-script-em-funcionamento)

### :gear: Funcionalidades:

- `.mp4`:  Fazer downloads de arquivos **.mp4** (e selecionar a qualidade destes);
- `.mp3`:  Fazer downloads de arquivos **.mp3** (e selecionar a qualidade destes);
- `playlists`:  Fazer o download de **playlists** (cuja a qualidade destas está automaticamente apontada para o máximo.
- `diretórios`:  Permitir que o usuário **defina um diretório** para o seu donwload;
- `verificações de entrada`:  Verificar se as **entradas do usuário são válidas**; 
- `barra de progresso`:  Mostrar uma barra de progresso para **acompanhar o download**.
- `Avisos de conexão`:  Avisa ao usuário se sua conexão for **perdidada ou interrompida**.

### :books: Bibliotecas utilizadas:

`Pytube`
`os`
`sys`
`re`
`time`
`urllib`
`http.client`

### :file_folder: Acesso ao projeto:

Clique [aqui](https://github.com/W3SL3N/Youtube-Downloader/tree/main/Youtube%20Downloader) para acessar o diretório com os arquivos do projeto.

### :arrow_forward: Rodar o projeto:

#### Primeiro método 
###### (recomendado para devs que queiram fazer alterações nos arquivos)

1° - Tenha a última versão do Python em sua máquina, caso contrario, baixe e instale seguindo as intruções do [site oficial do python](https://www.python.org/).<br/>
2° - Baixe o .zip com todos os arquivos.py do projeto [clicando aqui](https://github.com/W3SL3N/Youtube-Downloader/raw/main/YT_Downloader.zip).<br/>
3° - Extraia todos para o mesmo diretorio utilizando o programa de sua preferência.<br/>
4° - Abra o **YT_Downloader.py** com o python de sua máquina.<br/>
5° - Faça bom uso da sua nova ferramenta.

#### Segundo método 
###### (recomendado para quem quer utilizar a ferramenta em seu estádo atual)

1° - Baixe o **YT_Downloader.exe** [clicando aqui](https://github.com/W3SL3N/Youtube-Downloader/raw/main/YT_Downloader.exe).<br/>
2° - Abra-o em sua máquina.<br/>
3° - Faça bom uso da sua nova ferramenta.<br/>

### :warning: Aviso importante:

Para usuários Linux ou MacOs, alterar a linha 6 do arquivo cabecalho.py, que está assim:

```
os.system('cls')
```

Altere para:

```
os.system('clear')
```

### :jigsaw: Obejtivos do projeto:

- Consolidar conhecimentos e praticar habilidades em Python;
- Manter qualidade no código, separando responsabilidades em diferentes arquivos, <br/>afim de poder fazer alterações e correções facilmente;
- Interagir de forma amigável e clara com o usuário final;
- Tratar erros sem que eles fechassem abruptamente o script.

### :hammer_and_wrench: Tecnonologias utilizadas:

- `Python`
- `Pycharm`
- `paradigma de orientação a objetos`

### :fast_forward: Script em funcionamento:

###### Neste exemplo estarei fazendo o download de um vídeo.

![exemplo](https://user-images.githubusercontent.com/108354947/179423866-5b611938-d53a-4438-b51a-b496b2ecd1c2.gif)


