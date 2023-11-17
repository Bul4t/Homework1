import re

# У меня температура и мне очень не легко думать, так что извиняюсь за недочёты, я пытался как мог

#1

def Tnum(str):

#bibi
    if re.match(pattern='\w\d{3}\w{2}\d{2,3}', string=str):
        return 'Частный'

#taxi
    elif re.match(pattern='\w{2}\d{3}\d{2,3}', string=str):
        return 'Такси'
    else:
        return 'Не номер'

str = 'С227НА777 КУ22777 Т22В7477 М227К19У9 С227НА777'
str_splited = str.split(" ")

for num in str_splited:
    print(Tnum(num), end=" ",)

print(' ')

#2

def words(word):
    words = re.findall(r'\b[А-Яа-яA-Za-z]+[-][А-Яа-яA-Za-z]+\b|\b[А-Яа-яA-Za-z]+\b', word)
    num_of_words = len(words)
    return num_of_words, words
print(words('sdf sfsdfsdf qwewe прпрп-рывыа '))

#3                                                     ([0-23]{1,2}:)?[0-59]{2}:[0-59]{2}\b|)

def time_repl(text):
    new_text = re.sub(r'((([0-1])[0-9])|([0-2])[0-3]):[0-5][0-9](:[0-5][0-9])?\b', '(TBD)', text)
    return new_text
print(time_repl('Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 9:00:01 я за себя не отвечаю. PS. С отношением 25:50 всё нормально!'))








