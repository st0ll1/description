#  Ссылки в виде списков для объединения данных
# База данных о сотрудниках


bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 50000.0, 'hardware']

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# База представлена в виде списка people
people = [bob, sue]
for person in people:
    print(person)

for person in people:
    print(person[0].split()[-1])        # Вывести фамилию
    person[2] *=1.20                       # увеличить оклад на 20%


# Выбираем все оклады используя генератор списков
pays = [person[2] for person in people]
# То же что и выше только используя map() 
 #pays = map(lambda x: x[2], people)
 # list(pays)

sum(person[2] for person in people) # Сумма окладов


# Добавим нового сотрудника
people[-1][0]                                       # Информация о Томе
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

""" Свяжем имена с позициями полей в записи. Кстати хреновое решение, нет обратной связи значения с именем поля
Можно использовать для этого списки списков что позволит менять поля        
"""
# NAME, AGE, PAY = range(3)
# bob[NAME]                                           # Имя Боба

bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]

#  Просматриваем имена полей в цикле, отыскивая необходимые
for person in people:
    for (name, value) in person:
        if name == 'name': print(value)

# Функция которая реализует функционал просмотра (строка 43)
def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:
            return fvalue

field(bob, 'name')
field(sue, 'pay')

# Выводит средний возраст людей
for rec in people:
    print(field(rec, 'age'))
 

