from video import Video
from musica import Musica

print('=' * 70)
print('\n' + 'Youtube Donwloader'.center(70, ' ') + '\n')
print('=' * 70 + '\n')

print('Você quer baixar vídeos ou músicas?'.center(70, ' ') + '\n')

cond = 0

while cond == 0:
    escolha = input(' '*22 + '1 - Vídeos / 2 - Músicas: ')

    if escolha == '1':
        video = Video()
        cond += 1
    if escolha == '2':
        musica = Musica()
        cond += 1
    else:
        continue