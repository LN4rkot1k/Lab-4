from prettytable import PrettyTable
soldiers = {}
for i in range(1, 6):
    soldiers ["Имя призывника №%d " % i] = input("Введите имя призывника №%d " % i)
    soldiers ["Фамилия призывника №%d " % i] = input("Введите фамилию призывника №%d " % i)
    soldiers ["Отчество призывника №%d " % i] = input("Введите отчество призывника №%d " % i)
    soldiers ["Год рождения призывника №%d " % i] = input("Введите год рождения призывника №%d " % i)
    soldiers ["Заболевание призывника №%d " % i] = input("Введите заболевание призывника №%d " % i)

table = PrettyTable()
columns = ["Имя призывника", "Фамилия призывника", "Отчество призывника", "Год рождения призывника", "Заболевание призывника"]
names = []
surnames = []
otchestvo = []
bornDay = []
illness = []

print(soldiers.keys())

for key in soldiers.keys():
    if "Имя" in key:
        names.append(soldiers[key])
    elif "Фамилия" in key:
        surnames.append(soldiers[key])
    elif "Отчество" in key:
        otchestvo.append(soldiers[key])
    elif "Год" in key:
        bornDay.append(soldiers[key])
    elif "Заболевание" in key:
        illness.append(soldiers[key])

table.add_column(columns[0], names)
table.add_column(columns[1], surnames)
table.add_column(columns[2], otchestvo)
table.add_column(columns[3], bornDay)
table.add_column(columns[4], illness)
print(table)
