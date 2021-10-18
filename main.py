def pocet_suborov():
    while True:
        cislo = input("Zadaj pocet suborov: ")
        try:
            return int(cislo)
        except ValueError:
            print("subor sa nenasiel ")

input = []
cislo_slova = 0
with open("basnicka.txt", encoding="utf-8") as subor:
    for slovo in subor:
        input += slovo.split()

for i in range(pocet_suborov):
    cislo_slova += 1
    if cislo_slova == len(input):
        cislo_slova -= len(input)
    with open(f"""slovo{cislo_slova}""", mode="w") as subor:
        print(input[cislo_slova - 1], file=subor)
