#  Словари

# Имеем базу о сотрудниках
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')

# Объединение списков
names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']
list(zip(names, values))                               # zip() объединяет списки

sue =  dict(zip(names, values))                  #  получаем словарь по объекту sue


# Словари можно создавать из последовательностей ключей
fields = ('name', 'age', 'job', 'pay')
# Создает dict из последовательности ключей и необязательного значения    
record = dict.fromkeys(fields, '?')                 

# ---------------------------------------------------------------------------------------------------------------------------------
# Списки словарей  для перебора
people = [bob, sue]
for person in people:
    print(person['name'], person['pay'], sep=' , ')       #Все имена и оклады

for person in people:
    if person['name'] == 'Sue Jones':
        print(person['pay'])


# Выбираем имена
names = [person['name'] for person in people]
names = list(map(lambda x: x['name'], people))      # Тоже самое

sum(person['pay'] for person in people)                    # Сумма   окладов
G = [rec['name'] for rec in people if rec['age'] >= 45]      # Выбираем всех кому за 45   

# Т.к словари являются объектами то к ним можно обращаться с помощью привычного синтаксиса
for person in people:
    print(person['name'].split()[-1])
    person['pay'] *= 1.10                                               # Повысим зарплату

#-------------------------------------------------------------------------------------------------------------------------------------

# Вложенные структуры
bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
                'age': 42,
                'job': ['software', 'writing'],
                'pay': (40000, 50000)}

bob2['name']['last']
for job in bob2['job']: print(job)
bob2['job'].append('janitor')                                           # Боб получает новую должность

# --------------------------------------------------------------------------------------------------------------------------------------

# Словари словарей
bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')

db = {}                                                                          # Инициализация словаря
db['bob'] = bob                                                             # Ссылка на словари в словаре
db['sue'] = sue

for key in db.keys():
     print(key, '=>' , db[key]['pay'])

# Прямой обход значений словаря
for  record in db.values(): print(record['pay'])
x = [db[key]['name'] for key in db]                                # Список имен

# Чтобы добавить новую запись в базу
db['tom'] = dict(name='Tom', age=50, job=None, pay=0)
[rec['name'] for rec in db.values() if rec['age'] >= 45]    # Вернет список имен
list(db.keys())













