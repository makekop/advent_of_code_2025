f = open("./input.txt")
data = f.readlines()

value = 50
zero = 0

for i in data:
    clean = i.strip()
    operator = clean[0]
    extract_numbers = clean[1:]
    number_to_calculate = int(extract_numbers[-2:])

    if operator == "R":
        if value + number_to_calculate > 99:  # 50 + 80
            value = value + number_to_calculate - 100  # 130 -100 = 30
        else:
            value += number_to_calculate

    else:
        if value - number_to_calculate < 0:  # 50 - 80
            value = value - number_to_calculate + 100  # -30 +100 = 70
        else:
            value -= number_to_calculate

    if value == 0:
        zero += 1
print(zero)
