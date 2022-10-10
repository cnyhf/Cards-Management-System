# -*- coding:utf-8 -*- 
# time :2022-07-18
import cards_tools
# 无线循环，由用户决定什么时候退出循环
while True:

    # TODO(ztt)显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()
    # 0退出系统
    elif action_str == "0":
        # 如果在开发程序时不希望立刻编写分支内部代码
        # 可以使用pass表示一个占位符，能够保证程序代码结构正确
        # pass
        print("欢迎再次使用【名片管理系统】")
        break
    # 其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新选择")