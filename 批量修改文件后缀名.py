import os
for Populitin_Size in range(100,1000,100):
    for Times_Of_Lacal_search in range(1,5):
        for cofficient in [1e-1,1e-2,1e-3,1e-4,1e-5]:

            dir_path = os.path.join('/C:\\Users\\王家桢\\Desktop\\general_search_final/','\\N=/','doiido')
dir_path = r'C:\Users\王家桢\Desktop\general_search_final'
os.startfile(dir_path)

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)

# def renaming(file):
#     """修改后缀"""
#     ext = os.path.splitext(file)  # 将文件名路径与后缀名分开
#
#     if ext[1] == '.txt':  # 文件名：ext[0]
#         new_name = ext[0] + '.html'  # 文件后缀：ext[1]
#         os.rename(file, new_name)  # tree()已切换工作地址，直接替换后缀
#     elif ext[1] == '.html':
#         new_name = ext[0] + '.txt'
#         os.rename(file, new_name)
#
#
# def tree(path):
#     """递归函数"""
#     files = os.listdir(path)  # 获取当前目录的所有文件及文件夹
#     for file in files:
#         file_path = os.path.join(path, file)  # 获取该文件的绝对路径
#         if os.path.isdir(file_path):  # 判断是否为文件夹
#             tree(file_path)  # 开始递归
#         else:
#             os.chdir(path)  # 修改工作地址（相当于文件指针到指定文件目录地址）
#             renaming(file)  # 修改后缀

# this_path = os.getcwd()  # 获取当前工作文件的绝对路径（文件夹)
# tree(this_path)