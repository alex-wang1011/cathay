# 程式邏輯題目二
def count_letters(text):
    letter_count = {}

    # 將所有字母轉換為小寫，以便不區分大小寫
    text = text.upper()

    # 遍歷每個字元
    for char in text:
        # 只處理字母和數字字符
        if char.isalnum():
            # 如果字元已經在字典中，將計數加1
            if char in letter_count:
                letter_count[char] += 1
            # 如果字元不在字典中，將其初始化為1
            else:
                letter_count[char] = 1

    # 將字典按照字元的順序排序
    sorted_count = sorted(letter_count.items())

    return sorted_count


text = "Hello welcome to Cathay 60th year anniversary"
result = count_letters(text)
for char, count in result:
    print(char, ":", count)
