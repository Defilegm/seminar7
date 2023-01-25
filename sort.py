
def search(x):
    name =''
    for i in range(len(x)):
        if x[i] ==' ':
            j = i+1
            while x[j] != ' ':
                name += x[j]
                j+=1
            break
    return name
def sorting():
    with open('directory.txt','r', encoding='utf-8') as f:
        a = f.readlines()
        result = sorted(a, key = search)  
    with open('directory.txt','w',encoding='utf-8') as f:
        for elem in result:
            f.write(elem)


