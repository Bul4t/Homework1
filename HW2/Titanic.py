f = open("train.csv", "r")
list = f.readlines()
s = []
Male = 0
Women = 0
All = 0
for i in range(1, len(list)):
    s = list[i].split(",")
    if s[1] == '1' and s[5] == 'male':
        Male += 1
    if s[1] and s[5] == 'female':
        Women += 1
All = Male + Women
print('Общее кол-во выживших:', All)
print('Кол-во живых мужчин:', Male)
print('Кол-во живых женщин:', Women)


