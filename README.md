# Youtube-Downloader
![Status do Projeto: Desenvolvimento](https://img.shields.io/badge/status-Finalizado-blue)

*Um script Python multiplataforma baseado em Pytube para o download de áudios, vídeos e playlists do Youtube de maneira clara, amigável e objetiva.*

## Índice:
- [Funcionalidades](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#gear-funcionalidades)
- [Sistemas operacionais suportados](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#computer-sistemas-operacionais-suportados)
- [Bibliotecas utilizadas](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#books-bibliotecas-utilizadas)
- [Acesso ao projeto](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#file_folder-acesso-ao-projeto)
- [Rodar o projeto](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#arrow_forward-rodar-o-projeto)
- [Obejtivos do projeto](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#jigsaw-obejtivos-do-projeto)
- [Tecnologias utilizadas](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#hammer_and_wrench-tecnonologias-utilizadas)
- [Script em funcionamento](https://github.com/W3SL3N/Youtube-Downloader/blob/main/README.md#fast_forward-script-em-funcionamento)

### :gear: Funcionalidades:

- `.mp4`:  Fazer downloads de arquivos **.mp4** (e selecionar a qualidade destes);
![download de um .mp4](https://user-images.githubusercontent.com/108354947/180067412-faa8c1d2-4e1f-4786-b11b-553c71f5963b.png)

- `.mp3`:  Fazer downloads de arquivos **.mp3** (e selecionar a qualidade destes);
![download de um .mp3](https://user-images.githubusercontent.com/108354947/180072545-a1abdf93-c5bf-4b46-8cc1-1802dead4021.png)

- `playlists`:  Fazer o download de **playlists** de **.mp3** e **.mp4** <br/>(cuja a qualidade destas está automaticamente apontada para o máximo)
![image](https://user-images.githubusercontent.com/108354947/180302922-e7b6a929-9cd0-49b7-ae27-4ebb0f624f4d.png)

- `diretórios`:  Permitir que o usuário **defina um diretório** para o seu download;
![image](https://user-images.githubusercontent.com/108354947/180302486-0f15d081-6cda-4ab8-952f-9756ab732141.png)

- `verificações de entrada`:  Verificar se as **entradas do usuário são válidas**; 
![mensagem de entrada inválida](https://user-images.githubusercontent.com/108354947/180074013-8d8600f7-c670-4e51-9bf2-6478556a0414.png)
![mensagem de entrada inválida](https://user-images.githubusercontent.com/108354947/180074327-ab2e081a-6ed5-4a88-b2c5-715692ee228f.png)
![mensagem de entrada inválida](https://user-images.githubusercontent.com/108354947/180074679-85296772-8182-4487-8079-d4dcf1b174be.png)

- `barra de progresso`:  Mostrar uma barra de progresso com informações para **acompanhar o download**;
![barra de progresso colorida](https://user-images.githubusercontent.com/108354947/180069500-650d5709-9062-422d-888f-4dedc65bdf65.png)

- `Avisos de conexão`:  Avisa ao usuário se sua conexão for **perdidada ou interrompida**.
![mensagem de perca de falha na conexão](https://user-images.githubusercontent.com/108354947/180070398-aaff871c-7da2-48ec-8051-4c8ea6ffcda7.png)
![mensagem de perca de falha na conexão](https://user-images.githubusercontent.com/108354947/180072901-5e605ff6-7927-4d20-b219-dac5dbf3ae37.png)
![mensagem de perca de falha na conexão](https://user-images.githubusercontent.com/108354947/180069032-93a2d97c-ce39-4714-8ead-7e2fe029712a.png)

### :computer: Sistemas operacionais suportados:

- `Windows`--> Testado.
- `Linux`----> Testado.
- `MacOs`----> Não testado.

###### As bibliotecas `Path` e `platform` inspiraram a ideia de adaptar o script para sistemas operacionais além do Windows, <br/>`platform` identifica o sistema para adaptar certas funcionalidades que funcionavam apenas no `Windows`, enquanto <br/>`Path` é responsável por lidar com os diretórios, que diferem em organização e caracteres entre as plataformas `Windows`, `Linux` e `MacOs`.

### :books: Bibliotecas utilizadas:

`Pytube`
`os`
`sys`
`re`
`time`
`urllib`
`http.client`
`platform`
`Path`

### :file_folder: Acesso ao projeto:

Clique [aqui](https://github.com/W3SL3N/Youtube-Downloader/tree/main/Youtube%20Downloader) para acessar o diretório com os arquivos do projeto.

### :fast_forward: Rodar o projeto:

#### Método 1 

1° - Tenha a última versão do Python em sua máquina, caso contrario, baixe e instale seguindo as intruções do [site oficial do python](https://www.python.org/).<br/>
2° - instale o módulo pytube.<br/>
3° - Baixe o .zip com todos os arquivos.py do projeto [clicando aqui](https://github.com/W3SL3N/Youtube-Downloader/raw/main/YT_Downloader.zip).<br/>
4° - Extraia todos para o mesmo diretorio utilizando o programa de sua preferência.<br/>
5° - Abra o **YT_Downloader.py** com o python de sua máquina.<br/>
6° - Faça bom uso da sua nova ferramenta.

#### Método 2.1 (Windows)

1° - Baixe [**YT_Downloader.exe**](https://github.com/W3SL3N/Youtube-Downloader/raw/main/YT_Downloader.exe).<br/>
2° - Abra-o em sua máquina.<br/>
3° - Se aparecer o aviso 'O Windows protegeu o computador', clique em 'Mais informações' e 'Executar assim mesmo'.<br/>
4° - Faça bom uso da sua nova ferramenta.<br/>

#### Método 2.2 (Linux)

1° - Baixe [**YT_Downloader**](https://github.com/W3SL3N/Youtube-Downloader/raw/main/YT_Downloader).<br/>
2° - Acesse o diretório onde está **YT_Downloader** através do terminal.<br/>
3° - Digite:
```
./YT_Downloader
```
4° - Faça bom uso da sua nova ferramenta.<br/>

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

![script em funcionamento](https://user-images.githubusercontent.com/108354947/180101190-87bb8952-15b2-44a4-9d64-6c608db11c23.gif)


