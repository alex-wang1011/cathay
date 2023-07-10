# 程式邏輯題目一
def transform_list(lst):
    transformed_lst = []
    for num in lst:
        reversed_num = int(str(num)[::-1])
        transformed_lst.append(reversed_num)
    return transformed_lst

input_list = [35, 46, 57, 91, 29]
output_list = transform_list(input_list)
print(output_list)
