with open("object.txt", mode='r', encoding='utf-8') as file1:  # 打开目标内容的文件
    with open("replace.txt", mode='r', encoding='utf-8') as file2:  # 打开待删除内容的文件
        obj_list = []
        result = ''
        for value in file1:
            obj_list.append(value.rstrip("\n"))  # 将目标内容加入列表并删除换行符
        for value in file2:
            result += value.rstrip("\n")

for each in obj_list:
    result = result.replace(each, '')

with open("result.txt", mode='w', encoding="utf-8") as file3:
    file3.writelines(result)
