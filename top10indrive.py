import os
count = 0
list = None

def printf(list):
    temp=list
    while temp!=None:
        print(temp.name,end=' ')
        print('& size = ', end='')
        print(temp.size, end='')
        print(' & path = ', end='')
        print(temp.path)
        temp=temp.next

def size(list):
    temp=list
    x=0
    while temp!=None:
        x+=1
        temp=temp.next
    print(x)

class objct():
    "Stores name , size and path"
    def __init__(self,name=None, size=None , path=None, next=None ):
        self.name = name
        self.size = size
        self.path = path
        self.next = next

def insertwithoutr(new,list):
    global count
    temp=list
    prev=list
    if temp.size>new.size:
        new.next=temp
        list=new
        count+=1

        return list
    while temp.size<new.size and temp.next!=None:
        prev=temp
        temp=temp.next
    if prev.size<new.size and temp.size>=new.size:
        new.next=temp
        prev.next=new
        count+=1
        return list
    elif temp.next==None:

        temp.next=new
        count+=1
        return list

def insertwithr(new,list):
    temp=list
    prev=list
    while temp.size<new.size and temp.next!=None:
        prev=temp
        temp=temp.next
    if prev.size<new.size and temp.size>=new.size:
        new.next=temp
        prev.next=new
        new=list.next

    elif temp.next==None:
        temp.next=new
        new=list.next
    return new

def top(path ):
    global list
    global count
    for file in os.listdir(path):

        arr= file.split(".")
        if len(arr) == 1:
            top(path + '/' + file)
        elif len(arr)>1:
            new=objct(file,os.stat(path+'/'+file).st_size,path+'/'+file,)
            if list==None:
                list=new
                count+=1
            elif count<10:
                list=insertwithoutr(new,list)

            elif list.size<new.size:

                list=insertwithr(new,list)
    return list

path1= input('enter directory you want to search in (eg: /Users/Downloads ):')
os.chdir(path1)
list=top(path1)
printf(list)

