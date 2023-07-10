# 程式邏輯題目三
def find_last_person(n):
    if n == 0:
        return 0

    colleagues = list(range(1, n + 1))

    index = 0
    while len(colleagues) > 1:
        index = (index + 2) % len(colleagues)
        colleagues.pop(index)

    return colleagues[0]

n = int(input("請輸入同事的人數: "))

last_person = find_last_person(n)
print("最後留下的同事的順位是:", last_person)