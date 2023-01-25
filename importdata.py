
def importdata():
    newrecord = input('Введите данные нового пользователя через пробел\nимя фамилия номерТелефона комментарий \n')
    with open('directory.txt','a',encoding='utf-8') as file:
        id = ''
        max = 0
        with open('directory.txt','r',encoding='utf-8') as f:
            s = f.readlines()
            for elem in s:
                for i in elem:
                    if i.isdigit():
                        id += i
                    else:
                        if int(id)>max:
                            max = int(id)
                        id = ''
                        break
        file.write(f'{(int(max)+1)} {newrecord}\n')
