# 程式邏輯題目三
def find_last_person(n):
    # 創建同事列表，初始為順序排號
    colleagues = list(range(1, n + 1))

    # 當同事列表中還有超過一個人時，執行報數並移除第三個人，直到只剩下最後一個人
    index = 0
    while len(colleagues) > 1:
        index = (index + 2) % len(colleagues)  # 報數到3的位置
        colleagues.pop(index)

    return colleagues[0]

# 輸入同事人數
n = int(input("請輸入同事的人數: "))

# 計算最後留下的同事的順位
last_person = find_last_person(n)
print("最後留下的同事的順位是:", last_person)