# inicializiramo spremenljivke, ki jih bomo potrebovali kasneje
sum_expense = 0
count_people = 0

# odpremo file handler, parameter "r" v funkciji open() je optional in ga lahko izpustimo
with open("files/stroski_izleta.txt", "r") as file_to_read_handler:

    for line in file_to_read_handler:
        # izbrišemo '\n' iz konca vrstice
        line = line.rstrip()

        # če je prvi znak v vrstici # - je to komentar
        if line[0] == "#":
            # vsebino te vrstice pri izračunu preskočimo
            # ukaz continue preskoči trenutno iteracijo v for zanki
            continue

        # vrstico razdelimo na 2 stolpca
        columns = line.split(',')
        # pristejemo stroske te osebe k skupnim stroskom
        sum_expense = sum_expense + int(columns[1])
        # dodamo eno osebo k stevilu vseh osebv
        count_people += 1

print(f"Skupaj so vsi stroski: {sum_expense}")
print(f"Na izletu je bilo {count_people} ljudi")
print(f"Strosek na osebo je { sum_expense/count_people }")
