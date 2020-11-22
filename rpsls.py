#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：土木三班岳学涛
日期：2020/11/21
"""
import random#引用函数
def name_to_number(name):#将汉字对应到数字
    if name=="石头":
        number1=0
    if name=="史波克":
        number1=1
    if name=="布":
        number1=2
    if name=="蜥蜴":
        number1=3
    if name=="剪刀":
        number1=4
    return number1


def number_to_name(number):#将随机产生的数字对应到汉字
    if number == 0:
        name2="石头"
    if number == 1:
        name2="史波克"
    if number == 2:
        name2="布"
    if number == 3:
        name2="蜥蜴"
    if number == 4:
        name2="剪刀"
    return name2


def rpsls(player_choice):#根据rspls规则判别输赢
    print("--------")
    print("您的选择为：%s"%player_choice)
    player_choice_number=name_to_number(player_choice)
    number2=random.randint(0,4)
    comp_number=number_to_name(number2)
    print("计算机的选择为：%s"%comp_number)
    if player_choice_number==0 and number2==3:
        print("您赢了！")
    if player_choice_number==0 and number2==4:
        print("您赢了！")
    if player_choice_number==1 and number2==0:
        print("您赢了！")
    if player_choice_number==1 and number2==4:
        print("您赢了！")
    if player_choice_number==2 and number2==0:
        print("您赢了！")
    if player_choice_number==2 and number2==1:
        print("您赢了！")
    if player_choice_number==3 and number2==1:
        print("您赢了！")
    if player_choice_number==3 and number2==2:
        print("您赢了！")
    if player_choice_number==4 and number2==2:
        print("您赢了！")
    if player_choice_number==4 and number2==3:
        print("您赢了！")
    if player_choice_number==number2:
        print("您和计算机出的一样呢!")
    else:
        print("计算机赢了！")
print("请输入你的选择：")
choice = input()
if choice=="石头" or choice=="史波克" or choice=="剪刀" or choice=="蜥蜴" or choice=="布":#如果输入内容正确，则进行下一步
    result=rpsls(choice)#引用自定义函数
    print(result)
else:
    print("Error: No Correct Name")#如果输入内容不正确，则提示















