def output():
    with open('directory.txt','r',encoding='utf-8') as f:
        name =''
        a = f.readlines()
        for f in range(len(a)):
            for i in range(len(a[f])):
                if a[f][i] ==' ':
                    j = i+1
                   
                    while not a[f][j].isdigit() :
                        name += a[f][j]
                        j+=1
                    a[f]  = f'{name}\n'
                    print(name)
                    name = ''
                    break
    

             



    