import re

f = open("./giftShopInput.txt")
data = f.readline()

id_split = re.split(",", data)
sum = 0

for i in id_split:
    first, second = re.split("-", i)
    id_range = range(int(first), int(second))
    for n in id_range:
        n_length = len(str(n))
        if n_length % 2 == 0:
            n_to_string = str(n)
            first_part, second_part = (
                n_to_string[: len(n_to_string) // 2],
                n_to_string[len(n_to_string) // 2 :],
            )
            if first_part == second_part:
                sum += n

print("answer", sum)
