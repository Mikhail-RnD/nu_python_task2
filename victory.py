import random
fameus_person ={
    'Исаак Ньютон' : '1642',
    'Конфуций' : '-551',
    'Николай Коперник' : '1473',
    'Наполеон I' : '1769',
}

wrong_ansvers = 0
rigth_answers = 0

#name, birth_day = random.choice(list(fameus_person.items()))

fameus_person = random.sample(list(fameus_person.items()), 5)

for key, value in fameus_person:
    if  input(f'Введите дату рождения для \'{key}:\' ') == value:
        rigth_answers += 1
    else:
        wrong_ansvers += 1


print(f'Правильных ответов = {rigth_answers * 100 // len(fameus_person)}')
print(f'Неправильных ответов = {wrong_ansvers * 100 // len(fameus_person)}')