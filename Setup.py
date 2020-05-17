import time
import sys
import pygame as pg

class Color:
    def __init__(self):
        self.black     = (0,0,0)
        self.lightgray = (191,191,191)
        self.darkgray  = (89,89,89)
        self.red       = (255,0,0)
        self.orange    = (244,177,131)
        self.lightyellow  = (255,235,175)
        self.darkyellow   = (255,192,0)
        self.lightblue = (149,238,234)
        self.lightgreen   = (169,209,142)
        self.darkgreen = (112,173,71)
        self.white     = (255,255,255)
        

class Rectangle:   
    def __init__(self,x=0,y=0,w=0,h=0,color=(0,0,0)):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.color = color
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))


class Circle:
    def __init__(self,x=0,y=0,r=0,color=(0,0,0)):
        self.x = x # Position X
        self.y = y # Position Y
        self.r = r # Radius
        self.color = color
    def draw(self,screen):
        pg.draw.circle(screen,self.color,(self.x,self.y),self.r)


class RectButton(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0, color=(0,0,0)):
        Rectangle.__init__(self, x, y, w, h, color)
    
    def isMouseOn(self):
        mousePos = pg.mouse.get_pos()
        return (self.x <= mousePos[0] <= self.x + self.w) and (self.y <= mousePos[1] <= self.y + self.h)

    def isMousePressed(self):
        state = pg.mouse.get_pressed()[0]
        return state


class CircleButton(Circle):
    def __init__(self,x=0,y=0,r=0,color=(0,0,0)):
        Circle.__init__(self, x, y, r, color)
    
    def isMouseOn(self):
        mousePos = pg.mouse.get_pos()
        return (mousePos[0]-self.x)**2 + (mousePos[1]-self.y)**2 <= self.r**2

    def isMousePressed(self):
        state = pg.mouse.get_pressed()[0]
        return state


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


class Capsule:
    def __init__(self,x=0,y=0,w=0,h=0,color=(0,0,0)):
        self.x = x # Center X
        self.y = y # Center Y
        self.w = w # Width
        self.h = h # Height
        self.color = color
    def draw(self,screen):
        rad = int(self.h / 2)
        wid = int(self.w - self.h)
        pg.draw.circle(screen,self.color,(self.x - int(wid/2) ,self.y),rad)
        pg.draw.circle(screen,self.color,(self.x + int(wid/2) ,self.y),rad)
        pg.draw.rect  (screen,self.color,(self.x - int(wid/2) ,self.y - int(self.h/2) ,wid ,self.h))


class Image:
    def __init__(self,x=0,y=0,name=''):
        self.x = x # Position X
        self.y = y # Position Y
        self.img = pg.image.load('Desktop/Simulation/'+name+'.png')

    def draw(self,screen):
        screen.blit(self.img, (self.x, self.y))
    
    def rotate(self,angle,screen):
        img_copy = pg.transform.rotate(self.img, angle)
        screen.blit(img_copy, (self.x - int(img_copy.get_width()/2) , self.y - int(img_copy.get_height()/2) ))


class Text:
    def __init__(self, x=0, y=0, message='', fontSize=26, fontColor=(0,0,0), backColor=(255,255,255)):
        self.x = x
        self.y = y
        self.message = message
        self.font = pg.font.Font('Library/Fonts/Superspace Light ver 1.00.ttf', fontSize) # fontand fontsize
        self.fontColor = fontColor
        self.backColor = backColor
        

    def draw(self,screen):
        self.text = self.font.render(self.message, True, self.fontColor, self.backColor) # (text,is smooth?,letter color,background color)
        self.textRect = self.text.get_rect() # text size
        self.textRect.center = (self.x, self.y)
        screen.blit(self.text, self.textRect)

class Timer(Text):
    def __init__(self, x=0, y=0, message='', fontSize=26, fontColor=(0,0,0), backColor=(255,255,255)):
        Text.__init__(self, x, y, message, fontSize, fontColor, backColor)

        self.trueStart = 0   #Starting simulation time
        self.start = 0       #Begining of a section time
        self.time = 0        #Last saved time
        self.t = 0           #Running time (Ex. 2.05 s)
    
    # def runTime(self, speed):
    #     self.time = pg.time.get_ticks() * speed
    #     self.message = '0'+str(pg.time.get_ticks()/1000)[0:-1]

    def startTime(self):
        self.trueStart = time.time()
        self.start = self.trueStart
        self.time  = self.trueStart

    def pauseTime(self):
        self.time = self.t + self.trueStart

    def resumeTime(self):
        self.start = time.time()

    def runTime(self, speed):
        self.t = ( ( time.time() - self.start) * speed ) + (self.time-self.trueStart)
        self.message = "0" + str(self.t)[0:4]

    def endTime(self, speed):
        pass









    # def change(self,x=0, y=0, message='', fontSize=26, fontColor=(0,0,0), backColor=(255,255,255) ):
    #     self.font = pg.font.Font('freesansbold.ttf', fontSize) # fontand fontsize
    #     self.text = self.font.render(message, True, fontColor, backColor) # (text,is smooth?,letter color,background color)
    #     self.textRect = self.text.get_rect() # text size
    #     self.textRect.center = (x, y)



class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
        self.COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
        self.FONT = pg.font.Font(None, 32)
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)







