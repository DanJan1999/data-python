open_file = open('CupcakeInvoices.csv')

# for line in open_file:
#     print(line)

# for line in open_file:
#     for type in line:
#         list = line.split(',')
#     print(list[2])

total_list = []

for line in open_file:
    for type in line:
        list = line.split(',')
    qnt = float(list[3])
    price = float(list[4])
    total = round(qnt * price, 2)
    print(total)
    total_list.append(total)

print(round(sum(total_list), 2))

open_file.close()