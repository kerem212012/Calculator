import pgzrun

WIDTH = 600
HEIGHT = 450
numberplace = Actor('number place', (300,64))
place1 = Actor('1',(64,200))
place2 = Actor('1',(150,200))
place3 = Actor('1',(236,200))
place4 = Actor('1',(64,286))
place5 = Actor('1',(150,286))
place6 = Actor('1',(236,286))
place7 = Actor('1',(64,372))
place8 = Actor('1',(150,372))
place9 = Actor('1',(236,372))
place0 = Actor('1',(322,286))
plus = Actor('1',(322,372))
minus = Actor('1',(408,372))
x = Actor('1',(408,286))
point = Actor('1',(494,372))
slash = Actor('1',(494,286))
delete = Actor('delete',(500,200))
deleteall = Actor('delete',(355,200))
enter = Actor('delete',(300,130))
numbers1 = ''
numbers2 = ''
num = 1
can1 = 0
can2 = 0
pointnum2 = 0
pointnum1 = 0
symbol = ''
allnum = 0
maxlen = 43
after_point1 = ''
after_point2 = ''
def draw():
    screen.fill('grey')
    numberplace.draw()
    if num == 1:
        screen.draw.text(f'{numbers1}',color='black',center=(300,64),fontsize=36)
    elif num == 2:
        screen.draw.text(f'{numbers2}', color='black', center=(300, 64), fontsize=36)
    place1.draw()
    screen.draw.text('1',color='black',center=(64,200),fontsize=36)
    place2.draw()
    screen.draw.text('2',color='black',center=(150,200),fontsize=36)
    place3.draw()
    screen.draw.text('3',color='black',center=(236,200),fontsize=36)
    place4.draw()
    screen.draw.text('4',color='black',center=(64,286),fontsize=36)
    place5.draw()
    screen.draw.text('5',color='black',center=(150,286),fontsize=36)
    place6.draw()
    screen.draw.text('6',color='black',center=(236,286),fontsize=36)
    place7.draw()
    screen.draw.text('7',color='black',center=(64,372),fontsize=36)
    place8.draw()
    screen.draw.text('8',color='black',center=(150,372),fontsize=36)
    place9.draw()
    screen.draw.text('9',color='black',center=(236,372),fontsize=36)
    place0.draw()
    screen.draw.text('0',color='black',center=(322,286),fontsize=36)
    delete.draw()
    screen.draw.text('delete', color='black', center=(500,200), fontsize=36)
    deleteall.draw()
    screen.draw.text('delete all', color='black', center=(355,200), fontsize=36)
    enter.draw()
    screen.draw.text('=', color='black', center=(300,130), fontsize=36)
    plus.draw()
    screen.draw.text('+', color='black', center=(322,372), fontsize=36)
    minus.draw()
    screen.draw.text('-', color='black', center=(408, 372), fontsize=36)
    x.draw()
    screen.draw.text('x', color='black', center=(408, 286), fontsize=36)
    point.draw()
    screen.draw.text('.', color='black', center=(494, 372), fontsize=36)
    slash.draw()
    screen.draw.text('÷', color='black', center=(494, 286), fontsize=36)
def on_mouse_down(button,pos):
    global numbers1
    global symbol
    global num
    global pointnum1
    global numbers2
    global pointnum2
    global allnum
    global can1
    global can2
    if button == mouse.LEFT and place1.collidepoint(pos) and len(numbers1) != maxlen and num == 1:
        numbers1 = numbers1.split(' ')
        numbers1.append('1')
        numbers1 = ''.join(numbers1)
    elif button == mouse.LEFT and place2.collidepoint(pos) and len(numbers1) != maxlen and num == 1:
        numbers1 = numbers1.split(' ')
        numbers1.append('2')
        numbers1 = ''.join(numbers1)
    elif button == mouse.LEFT and place3.collidepoint(pos) and len(numbers1) != maxlen and num == 1:
        numbers1 = numbers1.split(' ')
        numbers1.append('3')
        numbers1 = ''.join(numbers1)
    elif button == mouse.LEFT and place4.collidepoint(pos) and len(numbers1) != maxlen and num == 1:
        numbers1 = numbers1.split(' ')
        numbers1.append('4')
        numbers1 = ''.join(numbers1)
    elif button == mouse.LEFT and place5.collidepoint(pos) and len(numbers1) != maxlen and num == 1:
        numbers1 = numbers1.split(' ')
        numbers1.append('5')
        numbers1 = ''.join(numbers1)
    elif button == mouse.LEFT and place6.collidepoint(pos) and len(numbers1) != maxlen and num == 1:
        numbers1 = numbers1.split(' ')
        numbers1.append('6')
        numbers1 = ''.join(numbers1)
    elif button == mouse.LEFT and place7.collidepoint(pos) and len(numbers1) != maxlen and num == 1:
        numbers1 = numbers1.split(' ')
        numbers1.append('7')
        numbers1 = ''.join(numbers1)
    elif button == mouse.LEFT and place8.collidepoint(pos) and len(numbers1) != maxlen and num == 1:
        numbers1 = numbers1.split(' ')
        numbers1.append('8')
        numbers1 = ''.join(numbers1)
    elif button == mouse.LEFT and place9.collidepoint(pos) and len(numbers1) != maxlen and num == 1:
        numbers1 = numbers1.split(' ')
        numbers1.append('9')
        numbers1 = ''.join(numbers1)
    elif button == mouse.LEFT and place0.collidepoint(pos) and len(numbers1) != maxlen and num == 1:
        numbers1 = numbers1.split(' ')
        numbers1.append('0')
        numbers1 = ''.join(numbers1)
    elif button == mouse.LEFT and delete.collidepoint(pos) and num == 1:
        numbers1 = ' '.join(numbers1)
        numbers1 = numbers1.split(' ')
        numbers1.pop()
        numbers1 = ''.join(numbers1)

    elif button == mouse.LEFT and deleteall.collidepoint(pos) and num == 1:
        numbers1 = numbers1.split(' ')
        numbers1.pop()
        numbers1 = ''.join(numbers1)
    elif button == mouse.LEFT and plus.collidepoint(pos) and num == 1 and can1 == True and after_point1 == True:
        symbol = 1
        num = 2
        plus.image = '2'
    elif button == mouse.LEFT and minus.collidepoint(pos) and num == 1 and can1 == True and after_point1 == True:
        symbol = 2
        num = 2
        minus.image = '2'
    elif button == mouse.LEFT and x.collidepoint(pos) and num == 1 and can1 == True and after_point1 == True:
        symbol = 3
        num = 2
        x.image = '2'
    elif button == mouse.LEFT and slash.collidepoint(pos) and num == 1 and can1 == True and after_point1 == True:
        symbol = 4
        num = 2
        slash.image = '2'
    elif button == mouse.LEFT and point.collidepoint(pos) and len(numbers1) != maxlen and num == 1 and pointnum1 == False and can1 == True:
        numbers1 = numbers1.split(' ')
        numbers1.append('.')
        numbers1 = ''.join(numbers1)
    elif button == mouse.LEFT and place1.collidepoint(pos) and len(numbers2) != maxlen and num == 2:
        numbers2 = numbers2.split(' ')
        numbers2.append('1')
        numbers2 = ''.join(numbers2)
    elif button == mouse.LEFT and place2.collidepoint(pos) and len(numbers2) != maxlen and num == 2:
        numbers2 = numbers2.split(' ')
        numbers2.append('2')
        numbers2 = ''.join(numbers2)
    elif button == mouse.LEFT and place3.collidepoint(pos) and len(numbers1) != maxlen and num == 2:
        numbers2 = numbers2.split(' ')
        numbers2.append('3')
        numbers2 = ''.join(numbers2)
    elif button == mouse.LEFT and place4.collidepoint(pos) and len(numbers1) != maxlen and num == 2:
        numbers2 = numbers2.split(' ')
        numbers2.append('4')
        numbers2 = ''.join(numbers2)
    elif button == mouse.LEFT and place5.collidepoint(pos) and len(numbers1) != maxlen and num == 2:
        numbers2 = numbers2.split(' ')
        numbers2.append('5')
        numbers2 = ''.join(numbers2)
    elif button == mouse.LEFT and place6.collidepoint(pos) and len(numbers1) != maxlen and num == 2:
        numbers2 = numbers2.split(' ')
        numbers2.append('6')
        numbers2 = ''.join(numbers2)
    elif button == mouse.LEFT and place7.collidepoint(pos) and len(numbers1) != maxlen and num == 2:
        numbers2 = numbers2.split(' ')
        numbers2.append('7')
        numbers2 = ''.join(numbers2)
    elif button == mouse.LEFT and place8.collidepoint(pos) and len(numbers1) != maxlen and num == 2:
        numbers2 = numbers2.split(' ')
        numbers2.append('8')
        numbers2 = ''.join(numbers2)
    elif button == mouse.LEFT and place9.collidepoint(pos) and len(numbers1) != maxlen and num == 2:
        numbers2 = numbers2.split(' ')
        numbers2.append('9')
        numbers2 = ''.join(numbers2)
    elif button == mouse.LEFT and place0.collidepoint(pos) and len(numbers1) != maxlen and num == 2:
        numbers2 = numbers2.split(' ')
        numbers2.append('0')
        numbers2 = ''.join(numbers2)
    elif button == mouse.LEFT and delete.collidepoint(pos) and num == 2:
        numbers2 = ' '.join(numbers2)
        numbers2 = numbers2.split(' ')
        numbers2.pop()
        numbers2 = ''.join(numbers2)
    elif button == mouse.LEFT and deleteall.collidepoint(pos) and num == 2:
        numbers2 = numbers2.split(' ')
        numbers2.pop()
        numbers2 = ''.join(numbers2)
    elif button == mouse.LEFT and point.collidepoint(pos) and len(numbers1) != maxlen and num == 2 and pointnum2 == False and can2 == True:
        numbers2 = numbers2.split(' ')
        numbers2.append('.')
        numbers2 = ''.join(numbers2)
        pointnum2 = 1
    elif button == mouse.LEFT and enter.collidepoint(pos) and num == 2 and can2 == True and after_point2 == True:
        if symbol == 1 and (pointnum1 == True or pointnum2 == True) :
            allnum = float(numbers1) + float(numbers2)
            num = 1
            numbers1 = str(allnum)
            numbers2 = ''
            pointnum2 = 0
            pointnum1 = 0
            plus.image = '1'
            minus.image = '1'
            x.image = '1'
            slash.image = '1'
        elif symbol == 2 and (pointnum1 == True or pointnum2 == True) :
            allnum = float(numbers1) - float(numbers2)
            num = 1
            numbers1 = str(allnum)
            numbers2 = ''
            pointnum2 = 0
            pointnum1 = 0
            symbol = 0
            plus.image = '1'
            minus.image = '1'
            x.image = '1'
            slash.image = '1'
        elif symbol == 3 and (pointnum1 == True or pointnum2 == True) :
            allnum = float(numbers1) * float(numbers2)
            num = 1
            numbers1 = str(allnum)
            numbers2 = ''
            pointnum2 = 0
            pointnum1 = 0
            symbol = 0
            plus.image = '1'
            minus.image = '1'
            x.image = '1'
            slash.image = '1'
        elif symbol == 4 and (pointnum1 == True or pointnum2 == True) :
            allnum = float(numbers1) / float(numbers2)
            num = 1
            numbers1 = str(allnum)
            numbers2 = ''
            pointnum2 = 0
            pointnum1 = 0
            symbol = 0
            plus.image = '1'
            minus.image = '1'
            x.image = '1'
            slash.image = '1'
        elif symbol == 1 and (pointnum1 == False or pointnum2 == False) :
            allnum = int(numbers1) + int(numbers2)
            num = 1
            numbers1 = str(allnum)
            numbers2 = ''
            pointnum2 = 0
            pointnum1 = 0
            plus.image = '1'
            minus.image = '1'
            x.image = '1'
            slash.image = '1'
        elif symbol == 2 and (pointnum1 == False or pointnum2 == False):
            allnum = int(numbers1) - int(numbers2)
            num = 1
            numbers1 = str(allnum)
            numbers2 = ''
            pointnum2 = 0
            pointnum1 = 0
            symbol = 0
            plus.image = '1'
            minus.image = '1'
            x.image = '1'
            slash.image = '1'
        elif symbol == 3 and (pointnum1 == False or pointnum2 == False):
            allnum = int(numbers1) * int(numbers2)
            num = 1
            numbers1 = str(allnum)
            numbers2 = ''
            pointnum2 = 0
            pointnum1 = 0
            symbol = 0
            plus.image = '1'
            minus.image = '1'
            x.image = '1'
            slash.image = '1'
        elif symbol == 4 and (pointnum1 == False or pointnum2 == False):
            allnum = int(numbers1) / int(numbers2)
            num = 1
            numbers1 = str(allnum)
            numbers2 = ''
            pointnum2 = 0
            pointnum1 = 0
            symbol = 0
            plus.image = '1'
            minus.image = '1'
            x.image = '1'
            slash.image = '1'
def update(dt):
    global pointnum1
    global pointnum2
    global can1
    global can2
    global numbers2
    global numbers1
    global after_point1
    global after_point2
    check1 = ' '.join(numbers1).split(' ')
    check2 = ' '.join(numbers2).split(' ')

    if '0' in check1[0]:
        can1 = True
    elif '1' in check1[0]:
        can1 = True
    elif '2' in check1[0]:
        can1 = True
    elif '3' in check1[0]:
        can1 = True
    elif '4' in check1[0]:
        can1 = True
    elif '5' in check1[0]:
        can1 = True
    elif '6' in check1[0]:
        can1 = True
    elif '7' in check1[0]:
        can1 = True
    elif '8' in check1[0]:
        can1 = True
    elif '9' in check1[0]:
        can1 = True
    else:
        can1 = False


    if '0' in check2[0]:
        can2 = True
    elif '1' in check2[0]:
        can2 = True
    elif '2' in check2[0]:
        can2 = True
    elif '3' in check2[0]:
        can2 = True
    elif '4' in check2[0]:
        can2 = True
    elif '5' in check2[0]:
        can2 = True
    elif '6' in check2[0]:
        can2 = True
    elif '7' in check2[0]:
        can2 = True
    elif '8' in check2[0]:
        can2 = True
    elif '9' in check2[0]:
        can2 = True
    else:
        can2 = False

    if '.' in check1:
        pointnum1 = True
    elif not('.' in check1):
        pointnum1 = False
    elif '.' in check2:
        pointnum2 = True
    elif not('.' in check2):
        pointnum2 = False

    if '0' in check2[-1]:
        after_point2 = True
    elif '1' in check2[-1]:
        after_point2 = True
    elif '2' in check2[-1]:
        after_point2 = True
    elif '3' in check2[-1]:
        after_point2 = True
    elif '4' in check2[-1]:
        after_point2 = True
    elif '5' in check2[-1]:
        after_point2 = True
    elif '6' in check2[-1]:
        after_point2 = True
    elif '7' in check2[-1]:
        after_point2 = True
    elif '8' in check2[-1]:
        after_point2 = True
    elif '9' in check2[-1]:
        after_point2 = True
    else:
        after_point2 = False

    if '0' in check1[-1]:
        after_point1 = True
    elif '1' in check1[-1]:
        after_point1 = True
    elif '2' in check1[-1]:
        after_point1 = True
    elif '3' in check1[-1]:
        after_point1 = True
    elif '4' in check1[-1]:
        after_point1 = True
    elif '5' in check1[-1]:
        after_point1 = True
    elif '6' in check1[-1]:
        after_point1 = True
    elif '7' in check1[-1]:
        after_point1 = True
    elif '8' in check1[-1]:
        after_point1 = True
    elif '9' in check1[-1]:
        after_point1 = True
    else:
        after_point1 = False
pgzrun.go()