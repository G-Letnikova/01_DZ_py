'''написать программу, которая проверяет счастливость билета
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
'''
num = input('введите номер билета (6 цифр): ')
if int(num[0])+int(num[1])+int(num[2])-int(num[3])-int(num[4])-int(num[5]) == 0 :
    print('билет счастливый :)')
else :
    print('нет в жизни счастья :()')
