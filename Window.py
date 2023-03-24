import sys
import pygame as pg
import pygame.gfxdraw as pgg
from Setup import Color, Rectangle, Circle, RectButton, CircleButton, Trapezoid, Capsule, Image, GoalTop, GoalSide, Text, Timer, InputBox, Trajectory

class Simulation:
    def __init__(self):
        pass

    def run(self):
        pg.init()
        win_x, win_y = 1200, 720
        screen = pg.display.set_mode((win_x, win_y))
        clock  = pg.time.Clock()

        color       = Color()
        sideWindow  = Rectangle (0,0,828,430,color.white)
        topWindow   = Rectangle (0,464,828,256,color.white)
        operWindow  = Rectangle (865,0,335,720,color.white)   
        topBar1     = Rectangle (0,0,828,125,color.lightyellow)
        topBar2     = Rectangle (865,0,335,66,color.lightyellow)
        timerTrap   = Trapezoid (336,28,230,166,56,color.darkgray)
        timerText   = Timer     (323,27,'00.00',45,color.white)
        s           = Text      (396,34,'S',25,color.white)
        exitButton  = RectButton(25,25,74,74,color.darkgray,True)
        exitImage   = Image     (42,42,'exit')
        rerunButton = RectButton(524,25,74,74,color.darkgray,True)
        rerunImage  = Image     (537,37,'rerun')
        pauseButton = RectButton(624,25,74,74,color.darkgray,True)
        pauseImage  = Image     (645,40,'pause')
        speedButton = RectButton(724,25,74,74,color.darkgray,True)
        speedImage  = Image     (742,64,'speed')
        speedText   = Text      (760,44,'1.0x',27,color.white)
        description = Text      (418,162,"-- !! Let's Start the Simulation !! --",25,color.darkgray)
        confirmText   = Text    (1080,414,'Start',40,color.lightgray)
        confirmButton = CircleButton(985,411,42,color.orange,True)
        confirmImage  = Image   (956,382,'true')
        paraText    = Text      (1040,37,'Parameters',45,color.darkgray)
        paraCap_1   = Capsule   (997,130,214,64,color.darkgray)
        paraTrap_1  = Trapezoid (1077,130,200,108,63,color.darkgray)
        paraCir_1   = Circle    (922,130,25,color.white)
        paraText_1  = Text      (1060,110,'Goal Rotation Speed',20,color.white)
        paraText_11 = Text      (1100,144,'RPM',30,color.white)
        paraImage_1 = Image     (902,110,'rpm')
        paraInput_1 = InputBox  (1010,139,40,'-')
        paraCap_2   = Capsule   (997,218,214,64,color.darkgray)
        paraTrap_2  = Trapezoid (1077,218,200,108,63,color.darkgray)
        paraCir_2   = Circle    (922,218,25,color.white)
        paraText_2  = Text      (1110,200,'Distance',25,color.white)
        paraText_22 = Text      (1095,232,'CM',30,color.white)
        paraImage_2 = Image     (902,200,'distance')
        paraInput_2 = InputBox  (1010,220,50,'-')
        paraCap_3   = Capsule   (997,306,214,64,color.darkgray)
        paraTrap_3  = Trapezoid (1077,306,200,108,63,color.darkgray)
        paraCir_3   = Circle    (922,306,25,color.white)
        paraText_3  = Text      (1110,288,'Loss',25,color.white)
        paraText_33 = Text      (1095,317,'%',30,color.white)
        paraImage_3 = Image     (902,296,'loss')
        paraInput_3 = InputBox  (1010,305,50,'-')
        capsule_1   = Capsule   (1025,530,260,90,color.lightgray,True)
        capsule_2   = Capsule   (1025,648,260,90,color.lightgray,True)
        capText_1   = Text      (1030,506,'Shooting RPM',30,color.white,True)
        capText_2   = Text      (1020,624,'After Signal',30,color.white,True)
        needAngle   = Text      (1020,545,'-',50,color.white,True)  #################################
        needSignal  = Text      (1015,664,'    -  s',50,color.white,True)
        goalTop     = GoalTop   (563,592)
        goalSide    = GoalSide  (563,387)
        shooterSide = Image   (63,367,'shooterSide')
        shooterTop    = Image   (63,571,'shooterTop')
        stripe1     = Image     (0,125,  'stripeBlue')
        stripe2     = Image     (768,125,'stripeBlue')
        stripe3     = Image     (0,464,  'stripeBlue')
        stripe4     = Image     (768,464,'stripeBlue')
        grid        = Image     (1300,820,'grid')
        grid2       = Image     (1300,820,'table')
        traject     = Trajectory(0,0,2,0)
        whiteball_1 = CircleButton(1300,820,12,color.white)
        ball_1      = CircleButton(1300,820,8,color.darkgray)
        whiteball_2 = CircleButton(1300,592,12,color.white)
        ball_2      = CircleButton(1300,592,8,color.darkgray)
        lock        = Image     (1300,820,'lock')
        lockText    = Text      (1300,820,'(0,0)',25,color.orange)

        components = [sideWindow, topWindow, operWindow, topBar1, topBar2, timerTrap, timerText, s, exitButton, exitImage, rerunButton, rerunImage, pauseButton, pauseImage, speedButton, speedImage, speedText, grid, grid2, description,
                    confirmText, confirmButton, confirmImage, paraText, paraCap_1, paraTrap_1, paraCir_1, paraText_1, paraText_11, paraImage_1, paraCap_2, paraTrap_2, paraCir_2, paraText_2, paraText_22, paraImage_2, paraCap_3, paraTrap_3, paraCir_3, paraText_3, paraText_33, paraImage_3,
                    capsule_1, capsule_2, capText_1, capText_2, needAngle, needSignal, shooterSide ,shooterTop, stripe1, stripe2, stripe3, stripe4]

        inputs     = [paraInput_1, paraInput_2,paraInput_3]

        balls      = [whiteball_1, ball_1, whiteball_2, ball_2, lock, lockText]

        nowAction_1  = lastAction_1 = nowAction_2  = lastAction_2 = nowAction_3  = lastAction_3 = nowAction_4  = lastAction_4 = nowAction_5  = lastAction_5 = nowAction_6  = lastAction_6 = ''

        angle = 0
        goalRPM = 0
        errorPercent = 0
        speed = 1.0

        shootRPM = 0
        waitTime = 0
        spinMode = 0 

        readyFirstTime = True
        sim  = False
        play = False
        focus = False
        run = True

        while run:

            lockText.message = '(' + str( int((traject.x1-75)/1.5) ) + ',' + str( int((430 - traject.y1)/1.5) ) + ')'
            description.fontColor = color.darkgray
            stripeName = 'nothing'

            nowAction_1 = nowAction_2 = nowAction_3 = nowAction_4 = nowAction_5 = nowAction_6 = ''
            angle = goalTop.angle  = goalSide.angle = 0

            screen.fill(color.black)


            '''-----------------------------------------------------------------------------------------------------------------------------------------'''

            #---EXIT---
            if( exitButton.isMouseOn() ):
                if( exitButton.isMousePressed() ):
                    pg.quit()
                    sys.exit()
                    run = False
                else:
                    exitButton.color = color.red
            else:
                exitButton.color = color.darkgray

            
            '''-----------------------------------------------------------------------------------------------------------------------------------------'''

            #---INPUTS---
            ready = True
            for inp in inputs:
                if not(inp.message.isnumeric()):
                    sim  = play = ready = False

                if(inp.errorState):
                    description.message = inp.errorMessage
                    description.fontColor = color.red
                    stripeName = 'stripeRed'
                    sim  = play = ready = False
                    break

                if inp == inputs[0] and inp.message.isnumeric():
                    if 5 <= int(paraInput_1.message) <= 20 :
                        goalRPM = int(paraInput_1.message)
                        traject.rpmGoal = goalRPM
                    else:
                        description.message = '-- Please Input Goal Rotation between 5 - 20 RPM --'
                        description.fontColor = color.red
                        paraInput_1.fontColor = color.lightred
                        stripeName = 'stripeRed'
                        sim  = play = ready = False
                        break

                elif inp == inputs[1] and inp.message.isnumeric():
                    if 200 <= int(paraInput_2.message) <= 400 :
                        traject.s = (int(paraInput_2.message) + 12.437 - 60.35 ) / 100
                        goalTop.x  = goalSide.x = int( int(paraInput_2.message)*1.5 ) + 113
                    else:
                        description.message = '-- Please Input Distance between 200 - 400 cm --'
                        description.fontColor = color.red
                        paraInput_2.fontColor = color.lightred
                        stripeName = 'stripeRed'
                        sim  = play = ready = False
                        break

                elif inp == inputs[2] and inp.message.isnumeric():
                    if 0 <= int(paraInput_3.message) <= 50 :
                        errorPercent = int(paraInput_3.message)
                        traject.loss = errorPercent
                    else:
                        description.message = '-- Please Input Error Percent between 0 - 50 % --'
                        description.fontColor = color.red
                        paraInput_3.fontColor = color.lightred
                        stripeName = 'stripeRed'
                        sim  = play = ready = False
                        break

                else:
                    description.message = "-- !! Let's Start the Simulation !! --"
                    stripeName = 'nothing'

            if ready:
                if(readyFirstTime == True):
                    readyFirstTime = False
                    shootRPM, waitTime, spinMode = traject.calculate()
                    goalTop.mode = goalSide.mode = spinMode

                if shootRPM != 0:
                    capsule_1.color = capsule_2.color = color.darkyellow
                    needAngle.message   = (str(shootRPM)+'0')[0:4]
                    needSignal.message  = '  '+ str(waitTime)[0:4] +' s'
                    description.message = "-- Waiting for Simulation.. --"
                    traject.x1 = 95             
                    traject.y1 = 382   
                    whiteball_1.x = ball_1.x = whiteball_2.x = ball_2.x = traject.x1
                    whiteball_1.y = ball_1.y = traject.y1
                    if focus:
                        lock.x = traject.x1 - 36
                        lock.y = traject.y1 - 36
                        lockText.x = traject.x1
                        lockText.y = traject.y1 - 50
                        grid.x = grid2.x = 75
                        grid.y = 128
                        grid2.y = 464
                    else:
                        lock.x = lockText.x = grid.x = grid2.x = 1300
                        lock.y = lockText.y = grid.y = grid2.y = 820

                else:
                    capsule_1.color = capsule_2.color = color.lightgray
                    needAngle.message  = '-'
                    needSignal.message = '    -  s'
                    description.message = "-- Given Parameter is not Capable --"
                    description.fontColor = color.red
                    paraInput_3.fontColor = color.lightred
                    stripeName = 'stripeRed'
                    ready = False
            else:
                capsule_1.color = capsule_2.color = color.lightgray
                needAngle.message  = '-'
                needSignal.message = '    -  s'


            '''-----------------------------------------------------------------------------------------------------------------------------------------'''

            #---CONFIRM---
            if not sim: #(START)
                if( confirmButton.isMouseOn() and ready):
                    if( confirmButton.isMousePressed() ):
                        confirmButton.color = confirmText.fontColor = color.darkgreen
                        nowAction_1 = "Press"   
                    else:          
                        confirmButton.color = confirmText.fontColor = color.lightgreen 
                else:
                    confirmButton.color = confirmText.fontColor = color.lightgray

                if(nowAction_1 == '' and lastAction_1 == "Press"):
                    if ready:
                        traject.generate()
                        sim = True
                        play = True
                        timerText.startTime()
                        
                confirmImage.img = pg.image.load('Image/true.png')
                confirmText.message = "Start"

            else: #(CANCEL)
                if( confirmButton.isMouseOn() and ready):
                    if( confirmButton.isMousePressed() ):
                        confirmButton.color = confirmText.fontColor = color.red
                        nowAction_1 = "Press"   
                    else:          
                        confirmButton.color = confirmText.fontColor = color.lightred 
                else:
                    confirmButton.color = confirmText.fontColor = color.lightgray

                if(nowAction_1 == '' and lastAction_1 == "Press"):
                    if ready:
                        pauseImage.img = pg.image.load('Image/pause.png')
                        timerText.endTime()
                        goalTop.rotate(-angle, screen) 
                        goalSide.rotate(-angle,screen)
                        angle = 0
                        speed = 1.0
                        sim = False
                        play = False
                confirmImage.img = pg.image.load('Image/false.png')
                confirmText.message = "   Cancel!"
            

            '''-----------------------------------------------------------------------------------------------------------------------------------------'''

            #---PAUSE---
            if( pauseButton.isMouseOn() and sim ):
                if( pauseButton.isMousePressed() ):
                    pauseButton.color = color.darkblue
                    nowAction_2 = "Press"   
                else:
                    pauseButton.color = color.blue
            else:
                if sim:
                    pauseButton.color = color.darkgray 
                else:
                    pauseButton.color = color.lightgray

            if(nowAction_2 == '' and lastAction_2 == "Press" and sim):
                if(play == True):            
                    timerText.pauseTime()
                    pauseImage.img = pg.image.load('Image/play.png')
                elif(play == False):
                    timerText.resumeTime()
                    pauseImage.img = pg.image.load('Image/pause.png')
                play = not play  
            

            '''-----------------------------------------------------------------------------------------------------------------------------------------'''

            #---RERUN---
            if( rerunButton.isMouseOn() and sim ):
                if( rerunButton.isMousePressed() ):
                    rerunButton.color = color.darkblue
                    nowAction_3 = "Press"   
                else:
                    rerunButton.color = color.blue
            else:
                if sim:
                    rerunButton.color = color.darkgray 
                else:
                    rerunButton.color = color.lightgray

            if(nowAction_3 == '' and lastAction_3 == "Press" and sim):
                sim = True
                play = True
                goalTop.rotate(-angle, screen) 
                goalSide.rotate(-angle,screen)
                angle = 0
                timerText.startTime()


            '''-----------------------------------------------------------------------------------------------------------------------------------------'''

            #---SPEED---
            if( speedButton.isMouseOn() and ready and not play):
                if( speedButton.isMousePressed() ):
                    speedButton.color = color.darkblue
                    nowAction_4 = "Press"   
                else:
                    speedButton.color = color.blue
            else:
                if ready and not play:
                    speedButton.color = color.darkgray 
                else:
                    speedButton.color = color.lightgray

            if(nowAction_4 == '' and lastAction_4 == "Press" and ready):
                if(speed == 1.0):
                    speed = 0.5
                elif(speed == 0.5):
                    speed = 0.1
                elif(speed == 0.1):
                    speed = 1.0

            speedText.message = str(speed) + 'x'


            '''-----------------------------------------------------------------------------------------------------------------------------------------'''

            #---PLAYING---
            if sim:
                description.message = "-- Simulation Functioning Normally --"
                description.fontColor = color.darkblue
                stripeName = 'stripeBlue'
                angle = - float(timerText.message) * int(paraInput_1.message) * 6

                if play:
                    timerText.runTime(speed)

                if float(timerText.message) > traject.waitTime :
                    n = 0
                    for t in traject.table:
                        n += 1
                        if( t[2]+traject.waitTime > float(timerText.message) ):
                            ball_1.x = ball_2.x = t[0]
                            ball_1.y = t[1]
                            whiteball_1.x = whiteball_2.x = t[0]
                            whiteball_1.y = t[1]
                            if focus:
                                lock.x = t[0] - 36
                                lock.y = t[1] - 36
                                lockText.x = t[0]
                                lockText.y = t[1] - 50
                                lockText.message = '(' + str( int((t[0] - 75)/1.5) ) + ',' + str( int((430 - t[1])/1.5) ) + ')'
                            else:
                                lock.x = lockText.x = 1300
                                lock.y = lockText.y = 820
                            break               
                    if n == len(traject.table):
                        pauseImage.img = pg.image.load('Image/pause.png')
                        timerText.endTime()
                        goalTop.rotate(-angle, screen) 
                        goalSide.rotate(-angle,screen)
                        angle = 0
                        sim = False
                        play = False


            '''-----------------------------------------------------------------------------------------------------------------------------------------'''

            #---BALL CLICK---
            if whiteball_1.isMouseOn():
                if( whiteball_1.isMousePressed() ):
                    ball_1.color = color.darkblue
                    nowAction_5 = "Press"   
                else:
                    ball_1.color = color.blue
            else:
                ball_1.color = color.darkgray

            if nowAction_5 == '' and lastAction_5 == "Press":
                focus = not focus
                if focus:
                    lock.x = traject.x1 - 36
                    lock.y = traject.y1 - 36
                    lockText.x = traject.x1
                    lockText.y = traject.y1 - 50
                    grid.x = grid2.x = 75
                    grid.y = 128
                    grid2.y = 464
                else:
                    lock.x = lockText.x = grid.x = grid2.x = 1300
                    lock.y = lockText.y = grid.y = grid2.y = 820

            if whiteball_2.isMouseOn():
                if( whiteball_2.isMousePressed() ):
                    ball_2.color = color.darkblue
                    nowAction_6 = "Press"   
                else:
                    ball_2.color = color.blue
            else:
                ball_2.color = color.darkgray

            if nowAction_6 == '' and lastAction_6 == "Press":
                focus = not focus
                if focus:
                    lock.x = traject.x1 - 36
                    lock.y = traject.y1 - 36
                    lockText.x = traject.x1
                    lockText.y = traject.y1 - 50
                    grid.x = grid2.x = 75
                    grid.y = 128
                    grid2.y = 464
                else:
                    lock.x = lockText.x = grid.x = grid2.x = 1300
                    lock.y = lockText.y = grid.y = grid2.y = 820



            stripe1.img = stripe2.img = stripe3.img = stripe4.img = pg.image.load('Image/'+stripeName+'.png')



            '''-----------------------------------------------------------------------------------------------------------------------------------------'''

            #---DRAWING---
            for c in components:
                c.draw(screen)

            if focus:
                traject.draw(screen)

            goalTop.rotate(angle, screen) 
            goalSide.rotate(angle,screen)

            for b in balls:
                b.draw(screen)

            for i in inputs:
                i.draw(screen)
                
            for event in pg.event.get():
                for i in inputs:
                    useState = i.handle_event(event)
                    if(useState == True):
                        readyFirstTime = True

                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    run = False

            lastAction_1 = nowAction_1
            lastAction_2 = nowAction_2
            lastAction_3 = nowAction_3
            lastAction_4 = nowAction_4
            lastAction_5 = nowAction_5
            lastAction_6 = nowAction_6

            pg.display.update()
            pg.time.delay(10)
            clock.tick(60)


if __name__ == '__main__':
    sim = Simulation()
    sim.run()