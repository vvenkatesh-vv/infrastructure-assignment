import os
import shutil
class objct():
    "Stores name and place pairs"
    def __init__(self, type , name, size ):

        self.type = type
        self.name = name
        self.size = size

path1='/Users/venky/Desktop'
path3='/Users/venky/Documents/'
files=[]
types=[]
os.chdir(path1)
while True:
    foldername = input('enter a valid folder name you want files to move to \n (valid => there should not be any existing folder with that name in Documents):')
    if foldername in os.listdir(path3):
        continue
    else:
        break
path2='/Users/venky/Documents/' + foldername

"""takes out attributes of files and saves in list called files"""
for file in os.listdir():
    arr= file.split(".")
    if len(arr)>1:
        new=objct(arr[len(arr)-1],file,os.stat(file).st_size)
        files.append(new)


os.mkdir(path2)
for file in files:
    if file.type=='lnk':
        continue
    if len(types)==0:
        types.append(file.type)
        os.mkdir(path2 +'/'+file.type)
        shutil.move(path1 +'/'+ file.name, path2 + '/' + file.type)
        continue
    elif file.type in types:
        shutil.move(path1 + '/' + file.name, path2 + '/' + file.type)
        continue
    else:
        types.append(file.type)
        os.mkdir(path2 + '/' + file.type)
        shutil.move(path1 + '/' + file.name, path2 + '/' + file.type)
        continue








