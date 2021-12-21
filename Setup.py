import time
import math
import sys
import pygame as pg
import pygame.gfxdraw as pgg


'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class Color:
    def __init__(self):
        self.black     = (0,0,0)
        self.lightgray = (191,191,191)
        self.darkgray  = (89,89,89)
        self.lightred  = (255,170,170)
        self.red       = (255,0,0)
        self.orange    = (242,149,76)#(244,177,131)
        self.lightyellow  = (255, 225, 115)#(255,235,175)
        self.darkyellow   = (255,192,0)
        self.lightblue = (149,238,234)
        self.blue      = (150,220,220)
        self.darkblue  = (90,150,150)
        self.lightgreen   = (169,209,142)
        self.darkgreen = (112,173,71)
        self.white     = (255,255,255)
        

'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class Rectangle:   
    def __init__(self,x=0,y=0,w=0,h=0,color=(0,0,0),shadow=False):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.color = color
        self.shadow = shadow

    def draw(self,screen):
        if self.shadow: pg.draw.rect(screen,(160,160,160),(self.x+3,self.y+3,self.w,self.h))
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))


'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class Circle:
    def __init__(self,x=0,y=0,r=0,color=(0,0,0),shadow=False):
        self.x = x # Position X
        self.y = y # Position Y
        self.r = r # Radius
        self.color = color
        self.shadow = shadow

    def draw(self,screen):
        if self.shadow: pgg.filled_circle(screen,self.x+3,self.y+3,self.r,(160,160,160))
        pgg.filled_circle(screen,self.x,self.y,self.r,self.color)


'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class RectButton(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0, color=(0,0,0),shadow=False):
        Rectangle.__init__(self, x, y, w, h, color, shadow)
    
    def isMouseOn(self):
        mousePos = pg.mouse.get_pos()
        return (self.x <= mousePos[0] <= self.x + self.w) and (self.y <= mousePos[1] <= self.y + self.h)

    def isMousePressed(self):
        state = pg.mouse.get_pressed()[0]
        return state


'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class CircleButton(Circle):
    def __init__(self,x=0,y=0,r=0,color=(0,0,0),shadow=False):
        Circle.__init__(self, x, y, r, color, shadow)
    
    def isMouseOn(self):
        mousePos = pg.mouse.get_pos()
        return (mousePos[0]-self.x)**2 + (mousePos[1]-self.y)**2 <= self.r**2

    def isMousePressed(self):
        state = pg.mouse.get_pressed()[0]
        return state


'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class Trapezoid:
    def __init__(self,x=0,y=0,t=0,b=0,h=0,color=(0,0,0)):
        self.x = x # Center X 
        self.y = y # Center Y
        self.t = t # Top
        self.b = b # Base
        self.h = h # Height
        self.color = color

    def draw(self,screen):
        x1 = self.x - (self.t / 2)
        x2 = self.x - (self.b / 2)
        x3 = self.x + (self.b / 2)
        x4 = self.x + (self.t / 2)
        y1 = self.y - (self.h / 2)
        y2 = self.y + (self.h / 2)
        pg.draw.polygon(screen, self.color, [(x1,y1),(x2,y2),(x3,y2),(x4,y1)])


'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class Capsule:
    def __init__(self,x=0,y=0,w=0,h=0,color=(0,0,0),shadow=False):
        self.x = x # Center X
        self.y = y # Center Y
        self.w = w # Width
        self.h = h # Height
        self.color = color
        self.shadow = shadow

    def draw(self,screen):
        rad = int(self.h / 2)
        wid = int(self.w - self.h)

        if(self.shadow == True):
            pg.draw.circle(screen,(160,160,160),(self.x - int(wid/2)+3 ,self.y+4),rad)
            pg.draw.circle(screen,(160,160,160),(self.x + int(wid/2)+3 ,self.y+4),rad)
            pg.draw.rect  (screen,(160,160,160),(self.x - int(wid/2)+3 ,self.y+4 - int(self.h/2) ,wid ,self.h))
        
        pg.draw.circle(screen,self.color,(self.x - int(wid/2) ,self.y),rad)
        pg.draw.circle(screen,self.color,(self.x + int(wid/2) ,self.y),rad)
        pg.draw.rect  (screen,self.color,(self.x - int(wid/2) ,self.y - int(self.h/2) ,wid ,self.h))


'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class Image:
    def __init__(self,x=0,y=0,name=''):
        self.x = x # Position X
        self.y = y # Position Y
        self.img = pg.image.load('Desktop/MomotaroSimulation/Image/'+name+'.png')

    def draw(self,screen):
        screen.blit(self.img, (self.x, self.y))

    def rotate(self,angle,screen):
        img_copy = pg.transform.rotate(self.img, angle)
        screen.blit(img_copy, (self.x - int(img_copy.get_width()/2) , self.y - int(img_copy.get_height()/2) ))


'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class GoalTop:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.r = 90
        self.rpm = 0
        self.angle = 0 #Degree
        self.img   = pg.image.load('Desktop/MomotaroSimulation/Image/topSpin.png')  
        self.mode  = 1

    def rotate(self,angle,screen):
        self.angle = angle
        img_copy = pg.transform.rotate(self.img, angle)
        screen.blit(img_copy, (self.x - int(img_copy.get_width()/2) , self.y - int(img_copy.get_height()/2) ))
        x1 = self.x + int( self.r * math.cos(math.radians(self.angle)) )
        y1 = self.y - int( self.r * math.sin(math.radians(self.angle)) )
        x2 = self.x + int( self.r * math.cos(math.radians(self.angle+90)) )
        y2 = self.y - int( self.r * math.sin(math.radians(self.angle+90)) )
        x3 = self.x - int( self.r * math.cos(math.radians(self.angle)) )
        y3 = self.y + int( self.r * math.sin(math.radians(self.angle)) )
        x4 = self.x - int( self.r * math.cos(math.radians(self.angle+90)) )
        y4 = self.y + int( self.r * math.sin(math.radians(self.angle+90)) )
        c1 = (89,89,89)
        c2 = (89,89,89)
        c3 = (89,89,89)
        c4 = (90,150,150)
        if(self.mode == 2):
            c1 = c4
            c4 = c2
        pg.draw.circle(screen,c1,(x1,y1),10)
        pg.draw.circle(screen,c2,(x2,y2),10)
        pg.draw.circle(screen,c3,(x3,y3),10)
        pg.draw.circle(screen,c4,(x4,y4),10)


'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class GoalSide:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.r = 90
        self.rpm = 0
        self.angle = 0 #Degree
        self.img = pg.image.load('Desktop/MomotaroSimulation/Image/sideSpin.png')
        self.mode = 1

    def rotate(self,angle,screen):
        self.angle = angle
        x1 = self.x + int( self.r * math.cos(math.radians(self.angle)) )
        y1 =                      - math.sin(math.radians(self.angle))
        x2 = self.x + int( self.r * math.cos(math.radians(self.angle+90)) )
        y2 =                      - math.sin(math.radians(self.angle+90)) 
        x3 = self.x - int( self.r * math.cos(math.radians(self.angle)) )
        y3 =                        math.sin(math.radians(self.angle)) 
        x4 = self.x - int( self.r * math.cos(math.radians(self.angle+90)) )
        y4 =                        math.sin(math.radians(self.angle+90)) 
        c1 = ( int(155-75*y1), int(155-75*y1) , int(155-75*y1) )
        c2 = ( int(155-75*y2), int(155-75*y2) , int(155-75*y2) )
        c3 = ( int(155-75*y3), int(155-75*y3) , int(155-75*y3) )
        c4 = ( int(145-55*y4), int(205-50*y4) , int(205-50*y4) )

        if(self.mode == 2):
            c1 = ( int(145-55*y1), int(205-50*y1) , int(205-50*y1) )
            c4 = ( int(155-75*y4), int(155-75*y4) , int(155-75*y4) )

        li = []
        if   y1 > 0 and y4 > 0 : li = [ [c3,x3] , [c2,x2] , [c1,x1] , [c4,x4] ]
        elif y4 > 0 and y3 > 0 : li = [ [c2,x2] , [c1,x1] , [c4,x4] , [c3,x3] ]
        elif y3 > 0 and y2 > 0 : li = [ [c1,x1] , [c4,x4] , [c3,x3] , [c2,x2] ]
        elif y2 > 0 and y1 > 0 : li = [ [c4,x4] , [c3,x3] , [c2,x2] , [c1,x1] ]
        elif y1 > 0            : li = [ [c3,x3] , [c2,x2] , [c1,x1] , [c4,x4] ]
        elif y4 > 0            : li = [ [c2,x2] , [c1,x1] , [c4,x4] , [c3,x3] ]
        elif y3 > 0            : li = [ [c1,x1] , [c4,x4] , [c3,x3] , [c2,x2] ]
        else                   : li = [ [c4,x4] , [c3,x3] , [c2,x2] , [c1,x1] ]

        for i in range(0,4):
            top = 20
            bot = 12
            hi  = 28 
            x = li[i][1]
            y = self.y - 13
            x1 = x - (top / 2)
            x2 = x - (bot / 2)
            x3 = x + (bot / 2)
            x4 = x + (top / 2)
            y1 = y - (hi / 2)
            y2 = y + (hi / 2)
            pg.draw.polygon(screen, (li[i][0]), [(x1,y1),(x2,y2),(x3,y2),(x4,y1)])
            if(i == 1):
                screen.blit(self.img, (self.x - int(self.img.get_width()/2) , self.y - int(self.img.get_height()/2) ))

        
'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class Text:
    def __init__(self, x=0, y=0, message='', fontSize=26, fontColor=(0,0,0), shadow=False):
        self.x = x
        self.y = y
        self.message  = message
        self.fontSize = fontSize 
        self.font = pg.font.Font('Library/Fonts/Superspace Bold ver 1.00.ttf', self.fontSize)
        self.fontColor = fontColor
        self.shadow = shadow

    def draw(self,screen):
        if(self.shadow == True):
            self.text = self.font.render(self.message, True, (140,140,140), None)
            self.textRect = self.text.get_rect()
            self.textRect.center = (self.x+2, self.y+2)
            screen.blit(self.text, self.textRect)
        self.text = self.font.render(self.message, True, self.fontColor, None)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x, self.y)
        screen.blit(self.text, self.textRect)


'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class Timer(Text):
    def __init__(self, x=0, y=0, message='', fontSize=26, fontColor=(0,0,0)):
        Text.__init__(self, x, y, message, fontSize, fontColor)
        self.trueStart = 0   #Starting simulation time
        self.start = 0       #Begining of a section time
        self.time = 0        #Last saved time
        self.t = 0           #Running time (Ex. 2.05 s)
    def startTime(self):
        pg.time.delay(100)
        self.trueStart = time.time()
        self.start = self.trueStart
        self.time  = self.trueStart
        pg.time.delay(100)
    def pauseTime(self):
        self.time = self.t + self.trueStart
    def resumeTime(self):
        self.start = time.time()
    def runTime(self, speed):
        self.t = ( ( time.time() - self.start) * speed ) + (self.time-self.trueStart)
        self.message = "0" + str(self.t)[0:4]
    def endTime(self):
        self.message = "00.00"


'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class InputBox:
    def __init__(self,x=0,y=0,fontSize=32,message='',shadow=False):
        self.x = x
        self.y = y
        self.message  = message
        self.fontSize = fontSize 
        self.font = pg.font.Font('Library/Fonts/Superspace Bold ver 1.00.ttf', self.fontSize)
        self.fontColor = (149,238,234)
        self.shadow = shadow
        self.text = self.font.render(self.message, True, self.fontColor, None)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x, self.y)
        self.w = self.textRect.width + 100
        self.h = self.textRect.height
        self.active = False
        self.keyPos = 0
        self.errorState = False
        self.errorMessage  = '' 

    def draw(self,screen):
        if(self.shadow == True):
            self.text = self.font.render(self.message, True, (89,89,89), None)
            self.textRect = self.text.get_rect()
            self.textRect.center = (self.x+2, self.y+2)
            screen.blit(self.text, self.textRect)
        self.text = self.font.render(self.message, True, self.fontColor, None)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x, self.y)
        screen.blit(self.text, self.textRect)

    def isMouseOn(self):
        mousePos = pg.mouse.get_pos()
        return (self.x - self.w/2 <= mousePos[0] <= self.x + self.w/2) and (self.y - self.h/2 <= mousePos[1] <= self.y + self.h/2)

    def isMousePressed(self):
        state = pg.mouse.get_pressed()[0]
        return state
    
    def error(self, errorCode):
        self.errorState = True
        if(errorCode == 'Space'):
            self.fontColor = (255,170,170)
            self.errorMessage = "-- Please Input Every Parameters --"      
        elif(errorCode == 'Alpha'):
            self.fontColor = (255,170,170)
            self.errorMessage = "-- Please Input in Number only --"

    def handle_event(self, event):   

        inuse = False
        if not self.errorState : self.fontColor = (149,238,234)

        if self.isMousePressed():
            if self.isMouseOn():
                inuse = True
                self.active = True
                if(self.message == '-'):
                    self.message = '|'

                elif(self.message == ''):
                    pass

                elif(self.message[-1] != '|'):
                    self.message += '|'
            else:
                self.active = False
                self.message = self.message.replace('|','')
                self.errorState = False
                if(self.message == ''):
                    self.message = '-'
                    self.error('Space')
                self.keyPos  = len(self.message)
            
        if event.type == pg.KEYDOWN:
            if self.active:
                self.message = self.message.replace('|','')
                if event.key == pg.K_RETURN:
                        self.active = False
                        self.errorState = False
                        if(self.message == ''):
                            self.message = '-'
                            self.error('Space')
                        self.keyPos  = len(self.message)

                elif(self.message != ''):
                    if event.key == pg.K_BACKSPACE:
                        oldMessage   = self.message 
                        self.message = oldMessage[:self.keyPos-1]
                        self.keyPos  -= 1
                        self.message += '|' 
                        self.message += oldMessage[self.keyPos+1:]

                    elif event.key == pg.K_LEFT:
                        if(self.keyPos > 0):
                            self.keyPos -= 1
                            self.message = self.message[:self.keyPos] + '|' + self.message[self.keyPos:]
                        elif(self.keyPos == 0):
                            self.message = '|' + self.message

                    elif event.key == pg.K_RIGHT:
                        if(self.keyPos < len(self.message)):
                            self.keyPos += 1
                            self.message = self.message[:self.keyPos] + '|' + self.message[self.keyPos:]
                        elif(self.keyPos == len(self.message)):
                            self.message += '|'

                    else:
                        self.errorState = False
                        if(str(event.unicode).isalpha()):
                            self.error('Alpha')     
                        oldMessage   = self.message 
                        self.message = oldMessage[:self.keyPos]
                        a = 0
                        if str(event.unicode).isnumeric() :
                            self.message += event.unicode
                            self.keyPos  += 1
                            a = 1
                        self.message += '|' 
                        self.message += oldMessage[self.keyPos-a:]
        
                else:
                    self.errorState = False
                    if(str(event.unicode).isalpha()):
                        self.error('Alpha')
                    elif str(event.unicode).isnumeric() :
                        self.message = event.unicode
                        self.keyPos  += 1
                    self.message += '|'

                self.text = self.font.render(self.message, True, self.fontColor, None)
                self.w = self.textRect.width + 100
                inuse = True

        return inuse


'''-----------------------------------------------------------------------------------------------------------------------------------------'''


class Trajectory:   
    def __init__(self,x1=0,y1=0,rpmGoal=0,loss=0):
        self.x1   = x1#px
        self.y1   = y1#px
        self.s    = 0 #m  
        self.h    = 0.405 - 0.3188#m
        self.loss = loss #%
        self.RPM  = 1800
        self.r    = 0.035#m
        self.v       = 0 #m   
        self.real_v  = 0 #m  
        self.rpmGoal = rpmGoal
        self.theta = 45  #Degree
        self.shootTime = 0
        self.spinTime  = 0
        self.spinMode  = 1
        self.waitTime  = 0
        self.table = []

    def calculate(self):
        self.spinMode  = 1
        self.v         = ( (4.9*self.s*self.s) / (self.s*math.tan(math.radians(45)) - 2*self.h) / math.cos(math.radians(45))**2  )**0.5
        self.real_v    = self.v * 100 / (100-self.loss)
        self.RPM       = int( (30*self.real_v) / (math.pi*self.r) )
        self.shootTime = self.s / ( self.v * math.cos(math.radians(45)) )
        self.spinTime  = 15 / self.rpmGoal 
        self.waitTime  = self.spinTime - self.shootTime 
        if(self.waitTime < 0):
            self.waitTime  = 2*self.spinTime - self.shootTime 
            self.spinMode  = 2
        # return self.RPM, self.waitTime, self.spinMode
        return self.v, self.waitTime, self.spinMode


    def generate(self):
        t1 = 0#s
        t2 = self.shootTime #- 0.075#s
        x1 = self.x1#px
        y1 = self.y1#px
        u  = self.v*3/0.02#px/s 
        g  = -1470#px/s^2            #-9.8 m/s^2
        theta = self.theta#degree
        ux = u *math.cos(math.radians(theta))
        uy = u *math.sin(math.radians(theta))
        dt = 0.01#s

        self.table = []
        while(t1 <= t2):
            x = int(x1  +  ux * t1)
            y = int(y1  -  uy * t1  -  0.5 * g * t1**2)
            t1 += dt
            self.table.append([x,y,t1])  

    def draw(self,screen):
        n = 0
        for tab in self.table:
            n+=1
            r = 1
            if n%5 == 0 : r = 3
            x = tab[0]
            y = tab[1]
            pgg.filled_circle(screen,x,y,r,(244,177,131))
            pgg.filled_circle(screen,x,592,r,(244,177,131))


'''-----------------------------------------------------------------------------------------------------------------------------------------'''