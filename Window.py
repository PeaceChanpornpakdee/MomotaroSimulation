import sys
import pygame as pg
from Setup import Color, Rectangle, RectButton, CircleButton,Trapezoid, Capsule, Image, Text, Timer #,InputBox, 

pg.init()
win_x, win_y = 1200, 720
screen = pg.display.set_mode((win_x, win_y))
# screen = pg.display.set_mode((win_x, win_y), pg.FULLSCREEN)

color = Color()

sideWindow  = Rectangle(0,0,828,430,color.white)
topWindow   = Rectangle(0,464,828,256,color.white)
operWindow  = Rectangle(865,0,335,720,color.white)   

topBar1     = Rectangle(0,0,828,125,color.lightyellow)
topBar2     = Rectangle(865,0,335,66,color.lightyellow)

timerTrap   = Trapezoid(300,25,200,100,50,color.darkgray)
timerText   = Timer(287,27,'00.00',40,color.white,color.darkgray)


exitButton  = RectButton(25,25,74,74,color.darkgray)
exitImage   = Image(42,42,'exit')

pauseButton  = RectButton(600,25,74,74,color.darkgray)

startText   = Text(1105,412,'start',40,color.lightgray,color.white)
confirmButton = CircleButton(985,411,42,color.orange)
trueImage   = Image(955,382,'true')

capsule_1   = Capsule(1000,600,200,100,color.darkgray)

topSpinImage   = Image(637,592,'topSpin')

angle = 0
plus = 0

nowAction  = ""
lastAction = ""

play = False

run = True

while run:

    nowAction = ""

    angle += plus
    screen.fill(color.black)

    if( exitButton.isMouseOn() ):
        if( exitButton.isMousePressed() ):
            pg.quit()
            sys.exit()
            run = False
        else:
            exitButton.color = color.red
    else:
        exitButton.color = color.darkgray


    if( pauseButton.isMouseOn()):
        if( pauseButton.isMousePressed() ):
            nowAction = "Press"   

        else:
            pauseButton.color = color.red
    else:
        pauseButton.color = color.darkgray


    if(nowAction == "" and lastAction == "Press"):
        if(play == True):            
            timerText.pauseTime()
        elif(play == False):
            timerText.resumeTime()
        play = not play  



    t = 1
    if( confirmButton.isMouseOn() ):
        if( confirmButton.isMousePressed() ):
            confirmButton.color = color.lightgreen
            timerText.startTime()
            play = True
            t = 100


        else:
            confirmButton.color = color.lightgray
    else:
        confirmButton.color = color.darkgray


    if(play == True):
        timerText.runTime(0.5)
        plus = 6

    else:
        plus = 0

        

    sideWindow.draw(screen)
    topWindow.draw(screen)
    operWindow.draw(screen)

    topBar1.draw(screen)
    topBar2.draw(screen)

    timerTrap.draw(screen)
    timerText.draw(screen)

    exitButton.draw(screen)
    exitImage.draw(screen)

    pauseButton.draw(screen)

    startText.draw(screen)
    confirmButton.draw(screen)
    trueImage.draw(screen)

    capsule_1.draw(screen)

    topSpinImage.rotate(angle,screen)

    # topSpinImage.draw(screen)

    # for text in texts:
    #     screen.blit(text.text, text.textRect)

    # for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
    #     box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
    #     box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        # for box in input_boxes:
        #     box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            run = False

    pg.display.update()
    pg.time.delay(1)

    lastAction = nowAction







# input_box1 = InputBox(100, 100, 140, 32)
# input_box2 = InputBox(100, 200, 140, 32)
# input_box3 = InputBox(100, 300, 140, 32)
# input_boxes = [input_box1, input_box2, input_box3]

# # font = pg.font.Font('freesansbold.ttf', 26) # fontand fontsize
# # text = font.render('First Name', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
# # textRect = text.get_rect() # text size
# # textRect.center = (165, 100)
# text1 = Text(165, 80,'First Name')
# text2 = Text(165,180,'Last Name')
# text3 = Text(125,280,'Age')
# text4 = Text(250,400,'<Please submit your information>',20,(100,100,100))
# # text5 = Text(450,220,'submit',20,(76,153,0))
# text5 = Text(480,220,'submit',40,(25,51,0),(204,255,153))
# texts = [text1, text2, text3, text4, text5]

# btn  = Button(400,190,160,60,(76,153,0))

# run = True

# while run:
#     screen.fill(color.black)

#     if( btn.isMouseOn() ):
#         if( btn.isMousePressed() ):
#             btn.color = (102,178,255)
#             text5.change(480,220,'   OK    ',40,(0,102,204),(153,204,255))

#             if(input_box1.text == ""):
#                 text4.change(270,400,'<ERROR!! : First name is still blank!>',20,(255,0,0))

#             elif(input_box3.text == ""):
#                 text4.change(250,400,'<ERROR!! : Age is still blank!>',20,(255,0,0))

#             elif(not input_box3.text.isdigit()):
#                 text4.change(310,400,'<ERROR!! : Age can only contains number!>',20,(255,0,0))

#             else:
#                 text4.change(win_x/2,400,'Hello '+ input_box1.text +' '+ input_box2.text + '. You are ' + input_box3.text + ' years old.',20,(0,0,0))
#                 pg.quit()
            
#         else:
#             btn.color = (175,175,175)
#             text5.change(480,220,'sure ? ',40,(96,96,96),(200,200,200))
#     else:
#         btn.color = (76,153,0)
#         text5.change(480,220,'submit',40,(25,51,0),(204,255,153))
        
#     btn.draw(screen)

#     for text in texts:
#         screen.blit(text.text, text.textRect)

#     for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
#         box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
#         box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
#     for event in pg.event.get():
#         for box in input_boxes:
#             box.handle_event(event)
#         if event.type == pg.QUIT:
#             pg.quit()
#             run = False

#     pg.time.delay(1)
#     pg.display.update()




# import sys 
# import pygame as pg
# from Setup import Rec, Button

# pg.init()
# run = True
# win_x, win_y = 800, 480
# screen = pg.display.set_mode((win_x, win_y))
# btn  = Button(20,20,100,100)
# btn2 = Button(350,200,50,50,(255,0,0)) 
# rec  = Rec(350,190,100,100) 

# keyboardState = [0,0,0,0]  #[W,A,S,D]

# while(run):
#     screen.fill((255, 255, 255))

#     '''Exercise 0'''
#     # if btn.isMouseOn():
#     #     btn.w = 200
#     #     btn.h = 300
#     # else:
#     #     btn.w = 100
#     #     btn.h = 100
#     # btn.draw(screen)

#     '''Exercise 1'''
#     # if( btn2.isMouseOn() ):
#     #     if( btn2.isMousePressed() ):
#     #         btn2.color = (120,20,220)
#     #     else:
#     #         btn2.color = (122,122,122)
#     # else:
#     #     btn2.color = (255,0,0)
#     # btn2.draw(screen)

#     '''Exercise 2'''
#     # rec.x -= ( keyboardState[1]*2 - keyboardState[3]*2 )
#     # rec.y -= ( keyboardState[0]*2 - keyboardState[2]*2 )
#     # rec.draw(screen)
    
#     pg.display.update()
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()

#         '''Exercise 2'''
#         # if event.type == pg.KEYDOWN:
#         #     if event.key == pg.K_w:
#         #         keyboardState[0] = 1
#         #     elif event.key == pg.K_a:
#         #         keyboardState[1] = 1
#         #     elif event.key == pg.K_s:
#         #         keyboardState[2] = 1
#         #     elif event.key == pg.K_d:
#         #         keyboardState[3] = 1

#         # if event.type == pg.KEYUP:
#         #     if event.key == pg.K_w:
#         #         keyboardState[0] = 0
#         #     elif event.key == pg.K_a:
#         #         keyboardState[1] = 0
#         #     elif event.key == pg.K_s:
#         #         keyboardState[2] = 0
#         #     elif event.key == pg.K_d:
#         #         keyboardState[3] = 0

