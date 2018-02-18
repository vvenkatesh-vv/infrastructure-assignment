import os
import shutil
#creates a srtucture to save attributes of files
class objct():
    def __init__(self, type , name, size ):

        self.type = type
        self.name = name
        self.size = size

path1=input('enter path of Desktop(if it is = /Users/Desktop hit enter):')
if path1=='':
    path1='/Users/Desktop'

path3=input('enter path of Documents(if it is = /Users/Documents hit enter):')
if path3=='':
    path3='/Users/Documents/'

files=[]
types=[]
os.chdir(path1)

#takes input from user of folder name
while True:
    foldername = input('enter a valid folder name you want files to move to \n (valid => there should not be any existing folder with that name in Documents):')
    if foldername in os.listdir(path3):
        continue
    else:
        break
path2=path3 +'/'+ foldername

#takes out attributes of files and saves in list called files
for file in os.listdir():
    arr= file.split(".")
    if len(arr)>1:
        new=objct(arr[len(arr)-1],file,os.stat(file).st_size)
        files.append(new)


os.mkdir(path2)
#sorts and moves according to extension
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








