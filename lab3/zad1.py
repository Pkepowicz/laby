import os
import shutil

print(os.listdir('zadanie1'))
for file in os.listdir('zadanie1'):
    try:
        os.mkdir('zad1o/'+ file[0])
    except:
        pass
    shutil.copy('zadanie1/' + file, 'zad1o/' + file[0])