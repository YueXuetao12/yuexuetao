#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���ľ������ѧ��
���ڣ�2020/11/21
"""
import random#���ú���
def name_to_number(name):#�����ֶ�Ӧ������
    if name=="ʯͷ":
        number1=0
    if name=="ʷ����":
        number1=1
    if name=="��":
        number1=2
    if name=="����":
        number1=3
    if name=="����":
        number1=4
    return number1


def number_to_name(number):#��������������ֶ�Ӧ������
    if number == 0:
        name2="ʯͷ"
    if number == 1:
        name2="ʷ����"
    if number == 2:
        name2="��"
    if number == 3:
        name2="����"
    if number == 4:
        name2="����"
    return name2


def rpsls(player_choice):#����rspls�����б���Ӯ
    print("--------")
    print("����ѡ��Ϊ��%s"%player_choice)
    player_choice_number=name_to_number(player_choice)
    number2=random.randint(0,4)
    comp_number=number_to_name(number2)
    print("�������ѡ��Ϊ��%s"%comp_number)
    if player_choice_number==0 and number2==3:
        print("��Ӯ�ˣ�")
    if player_choice_number==0 and number2==4:
        print("��Ӯ�ˣ�")
    if player_choice_number==1 and number2==0:
        print("��Ӯ�ˣ�")
    if player_choice_number==1 and number2==4:
        print("��Ӯ�ˣ�")
    if player_choice_number==2 and number2==0:
        print("��Ӯ�ˣ�")
    if player_choice_number==2 and number2==1:
        print("��Ӯ�ˣ�")
    if player_choice_number==3 and number2==1:
        print("��Ӯ�ˣ�")
    if player_choice_number==3 and number2==2:
        print("��Ӯ�ˣ�")
    if player_choice_number==4 and number2==2:
        print("��Ӯ�ˣ�")
    if player_choice_number==4 and number2==3:
        print("��Ӯ�ˣ�")
    if player_choice_number==number2:
        print("���ͼ��������һ����!")
    else:
        print("�����Ӯ�ˣ�")
print("���������ѡ��")
choice = input()
if choice=="ʯͷ" or choice=="ʷ����" or choice=="����" or choice=="����" or choice=="��":#�������������ȷ���������һ��
    result=rpsls(choice)#�����Զ��庯��
    print(result)
else:
    print("Error: No Correct Name")#����������ݲ���ȷ������ʾ















