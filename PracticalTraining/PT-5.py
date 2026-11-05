def print_info():
    #打印提示信息，返回输入信息
    print("欢迎访问学生信息管理系统，请按提示输入操作！")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询学生信息")
    print("5.浏览学生信息")
    print("6.退出系统")
    input_num = input("请输入要操作的序号：")   #input输入的结果的类型是字符串
    return input_num

#添加函数
def add_stu_info():
    name = input("请输入姓名：")
    stu_id = input("请输入学号：")
    age = input("请输入年龄：")
    stu_info = {"stu_name":name,"stu_id":stu_id,"stu_age":age}
    stu_list.append(stu_info)
    print("添加成功")

#浏览学生信息
def get_stu_info():
    for stu_info in stu_list:
        print("原始数据：",stu_info)
        #按格式输出：姓名，学号，年龄
        name = stu_info["stu_name"]
        stu_id = stu_info["stu_id"]
        age = stu_info["stu_age"]

#查询学生信息
def get_single_info(name):
    exist = False
    for stu_info in stu_list:
        if stu_info["stu_name"] == name:
            exist = True
            name = stu_info["stu_name"]
            stu_id = stu_info["stu_id"]
            age = stu_info["stu_age"]
            print("姓名：{}，学号：{}，年龄：{}".format(name,stu_id,age))
    if exist == False:
        print("{}学生信息不存在".format(name))     #不能放在循环体内

#修改学生信息
def modify_stu_info(name):
    exist = False
    for stu_info in stu_list:
        if stu_info["stu_name"] == name:
            exist = True
            stu_id = input("请输入要修改的学号：")
            age = input("请输入要修改的年龄：")
            stu_info["stu_id"] = stu_id
            stu_info["stu_age"] = age
            print("修改成功！")
    if exist == False:
        print("{}学生信息不存在".format(name))

#删除学生信息
stu_list = [{"stu_name":"张三","stu_id":1,"stu_age":18}]
def del_stu_info(name):
    exist = False
    for stu_info in stu_list:
        if stu_info["stu_name"] == name:
            exist = True
            stu_list.remove(stu_info)
            print("删除成功！")
    if exist == False:
        print("{}学生信息不存在".format(name))

#定义运行的主函数
def main():
    while True:
        input_num=print_info()
        if input_num == "1":
            print("执行添加操作")
            add_stu_info()
        elif input_num == "2":
            print("执行删除操作")
            name = input("请输入要删除的学生姓名：")
            del_stu_info(name)
        elif input_num == "3":
            print("执行修改操作")
            name = input("请输入要修改的学生姓名：")
            modify_stu_info(name)
        elif input_num == "4":
            print("执行查询操作")
            name = input("请输入要查询的学生姓名：")
            get_single_info(name)
        elif input_num == "5":
            print("执行浏览操作")
            get_stu_info()
        elif input_num == "6":
            break
        else:
            print("字符输入错误，请按提示输入！")

main()
