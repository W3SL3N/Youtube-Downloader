# Youtube-Downloader
Downloads: Vídeos, Músicas, Playlists

### Motivações do projeto:

###### Gostaria de deixar esclarecidas algumas coisas<br/>antes de prosseguir com as explicações do meu script.

- Iniciei o projeto para fins de estudos e testes das minhas habilidades.
- Os downloaders online existentes não são muito confiaveis então porque não fazer o meu?

###### Isso foi o que me bastou para prosseguir.

### Este script é capaz de:

- Fazer downloads de arquivos .mp4 (e selecionar a qualidade destes);
- Fazer downloads de arquivos .mp3 (e selecionar a qualidade destes);
- Fazer o download de playlists (cuja a qualidade destas está automaticamente apontada para o máximo.

### Este script não é capaz de:

- Fazer o donwload de qualquer conteúdo privádo ou restrito a idade;
- Logar em uma conta do google;
- Fazer o donwload de alguns vídeos muito grandes na melhor qualidade;
- Definir um diretório específico para o download e com isso, <br/>verificar se o disco local especificado existe e a sintaxe do nome dos diretórios.

### Sobre o Projeto:

Procurei utilizar o máximo do que conheço em bibliotecas python (e que fazem sentido para este projeto)<br/>
até o momento desta publicação (17/07/2022).<br/> 

A base para este projeto foi a biblioteca [Pytube](https://pypi.org/project/pytube/), que oferece meios simples e claros para o <br/>
download de conteúdos livres do Youtube

### Obejtivos do Projeto:

- Manter qualidade no código, separando responsabilidades em diferentes arquivos, <br/>afim de poder fazer alterações e correções facilmente;
- Interação amigável e clara para o usuário final;
- Tratar erros sem que eles fechassem abruptamente o script.

### Utilização:

Se você ja tem pytohn instalado em sua máquina, basta baixar os arquivos .py deste repositório e abrir o 'YT_Downloader.py'.<br/>
Se não, estarei deixando um executável [aqui](https://github.com/W3SL3N/Youtube-Downloader/raw/main/YT_Downloader.exe), basta abrir e utilizar.

### Aviso importante:

Este projeto possui funcionalidades que só funcionarão no windows<br/>
como por exemplo a seguinte linha no arquivo cabecalho.py:

```
os.system('cls')
```

Ela está la para limpar o cmd, portanto se estiver utilizando MacOs ou Linux,<br/>
basta apagar estas linhas ou substituir seus comandos.
