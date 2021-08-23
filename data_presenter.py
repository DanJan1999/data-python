open_file = open('CupcakeInvoices.csv')

# for line in open_file:
#     print(line)

# for line in open_file:
#     for type in line:
#         list = line.split(',')
#     print(list[2])

# total_list = []

# for line in open_file:
#     for type in line:
#         list = line.split(',')
#     qnt = float(list[3])
#     price = float(list[4])
#     total = round(qnt * price, 2)
#     print(total)
#     total_list.append(total)

# print(round(sum(total_list), 2))

chocolate_total = []
vanilla_total = []
strawberry_total = []

for line in open_file:
    for type in line:
        list = line.split(',')
    qnt = float(list[3])
    price = float(list[4])
    total = round(qnt * price, 2)

    if list[2] == "Chocolate":
        chocolate_total.append(total)
    elif list[2] == "Vanilla":
        vanilla_total.append(total)
    elif list[2] == "Strawberry":
        strawberry_total.append(total)

print(round(sum(chocolate_total), 2))
print(round(sum(vanilla_total), 2))
print(round(sum(strawberry_total), 2))




open_file.close()