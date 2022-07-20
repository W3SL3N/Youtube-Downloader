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
![image](https://user-images.githubusercontent.com/108354947/180067412-faa8c1d2-4e1f-4786-b11b-553c71f5963b.png)

- `.mp3`:  Fazer downloads de arquivos **.mp3** (e selecionar a qualidade destes);
![image](https://user-images.githubusercontent.com/108354947/180072545-a1abdf93-c5bf-4b46-8cc1-1802dead4021.png)

- `playlists`:  Fazer o download de **playlists** de **.mp3** e **.mp4** (cuja a qualidade destas está automaticamente apontada para o máximo.
![image](https://user-images.githubusercontent.com/108354947/180073563-b8df7208-4e25-4992-963a-4875216b9e15.png)

- `diretórios`:  Permitir que o usuário **defina um diretório** para o seu donwload;
![image](https://user-images.githubusercontent.com/108354947/180068068-80166cd4-19da-4f7d-9013-bb26395f415c.png)

- `verificações de entrada`:  Verificar se as **entradas do usuário são válidas**; 
![image](https://user-images.githubusercontent.com/108354947/180074013-8d8600f7-c670-4e51-9bf2-6478556a0414.png)
![image](https://user-images.githubusercontent.com/108354947/180074327-ab2e081a-6ed5-4a88-b2c5-715692ee228f.png)
![image](https://user-images.githubusercontent.com/108354947/180074679-85296772-8182-4487-8079-d4dcf1b174be.png)

- `barra de progresso`:  Mostrar uma barra de progresso com informações para **acompanhar o download**;
![image](https://user-images.githubusercontent.com/108354947/180069500-650d5709-9062-422d-888f-4dedc65bdf65.png)

- `Avisos de conexão`:  Avisa ao usuário se sua conexão for **perdidada ou interrompida**.
![image](https://user-images.githubusercontent.com/108354947/180070398-aaff871c-7da2-48ec-8051-4c8ea6ffcda7.png)
![image](https://user-images.githubusercontent.com/108354947/180072901-5e605ff6-7927-4d20-b219-dac5dbf3ae37.png)
![image](https://user-images.githubusercontent.com/108354947/180069032-93a2d97c-ce39-4714-8ead-7e2fe029712a.png)

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
3° - Se aparecer o aviso 'O Windows protegeu o computador', clique em 'Mais informações' e 'Executar assim mesmo'.<br/>
4° - Faça bom uso da sua nova ferramenta.<br/>


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


