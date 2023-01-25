

def exportdata():
    with open('directory.txt','r',encoding='utf-8') as file:
        data = file.read()
        print(data)
    return data
