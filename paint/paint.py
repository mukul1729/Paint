from tkinter import filedialog
from tkinter import ttk
import sys
import time
from tkinter import *
import pygame
import numpy
sys.setrecursionlimit(10**5)
class paint:                
    def __init__(self):
        self.run = True
        self.x = 1080
        self.y = 720
        self.selected = None
        self.sel_color = (0,0,0)
        self.col1 = (26,82,89)
        self.col2 = (26,82,89)
        self.col3 = (26,82,89)
        self.win = 0
        self.sett = 0
        self.scx1 = 31
        self.scx2 = 31
        self.scx3 = 31
        self.scx4 = 30
        self.scx5 = 30
        self.scx6 = 30
        self.size = 1
        self.gx = 878
        self.gy = 590
        self.tab = 1
        self.tabseq = [1,2,3,4,5]
        self.xx = {}
        self.tabarr = {1:194,2:347,3:500,4:653,5:806}
        self.projectDir = \
                '/run/media/mukul/D/Programming/SH/Python/Projects/paint/'
        self.val = 1
        self.var = None
        self.r = 0
        self.g = 0
        self.b = 0

    def showval(self,setting_Surf,var,pos,s):
        fontObj = \
                pygame.font.Font('/usr/share/fonts/TTF/OpenSans-Regular.ttf',18)
        val = fontObj.render(s+str(int(var)),True,(120,120,120))
        setting_Surf.blit(val,pos)

    def ruler(self,scr,position,mouse,mouseButton):
        pass



    def floodfill_upper(self,arr,x,y,val,preval):
        try:
            if x<0 or y<0 or x>currx-1 or y>curry-1 or arr[x][y]!=list(preval[0:-1]):
                return
            arr[x][y] = val
            self.floodfill_upper(arr,x,y-1,val,preval)
            self.floodfill_upper(arr,x+1,y,val,preval)
            self.floodfill_upper(arr,x,y+1,val,preval)
        except IndexError:
            pass

    def floodfill_lower(self,arr,x,y,val,preval):
        try:
            if x<0 or y<0 or x>currx-1 or y>curry-1 or arr[x][y]!=list(preval[0:-1]):
                return
            arr[x][y] = val
            self.floodfill_lower(arr,x-1,y,val,preval)
            self.floodfill_lower(arr,x,y-1,val,preval)
            self.floodfill_lower(arr,x,y+1,val,preval)
        except IndexError:
            pass

    def tabar(self,scr,x,y,position,mouse,mouseButton,projectDir,var):
        tab = pygame.image.load(projectDir + '/images/tab.png')
        scr.blit(tab,(x,y))
        if var == 1:
            tab = pygame.image.load(projectDir + '/images/tab_sel.png')
            scr.blit(tab,(x,y))
        cross = pygame.image.load(projectDir + '/images/cross.png')
        scr.blit(cross,(x+128,y))
        if position[0] > x+128 and position[0]<x+153 and position[1]>y and\
                position[1]<y+25:
            cross = pygame.image.load(projectDir + '/images/cross_h.png')
            scr.blit(cross,(x+128,y))
            if mouseButton == 'left':
                time.sleep(.10)
                if self.tab in range(1,6):
                    self.tab -= 1
                cross = pygame.image.load(projectDir + '/images/cross.png')
                scr.blit(cross,(x+128,y))
                for a in range(len(self.tabseq)):
                    if self.tabseq[a] == self.val:
                        self.val = self.tabseq[a-1]
                        break

                for a in self.tabarr.keys():
                    if self.tabarr[a] == x:
                        for i in range(len(self.tabseq)):
                            if self.tabseq[i] == a:
                                del self.tabseq[i]
                                self.tabseq.append(a)
                        x = [194,347,500,653,806]
                        self.xx = {}
                        for i in range(len(self.tabseq)):
                            self.xx[self.tabseq[i]] = x[i]
                        self.tabarr = self.xx
                if self.val not in self.tabseq[0:self.tab]:
                    self.val = 1
                if self.tab == 1:
                    self.val = self.tabseq[0]
        elif position[0]>x and position[0]<x+128 and position[1]>y and \
                position[1]<y+25:
            if var == 1:
                tab = pygame.image.load(projectDir + '/images/tab_sel_h.png')
            else:
                tab = pygame.image.load(projectDir + '/images/tab_h.png')
            scr.blit(tab,(x,y))
            if mouseButton == 'left':
                if var == 1:
                    tab = pygame.image.load(projectDir + '/images/tab_sel.png')
                else:
                    tab = pygame.image.load(projectDir + '/images/tab.png')
                scr.blit(tab,(x,y))
                for i in self.tabarr.keys():
                    if self.tabarr[i] == x:
                        self.val = i


    def plus(self,scr,x,y,position,mouse,mouseButton,projectDir):
        add = pygame.image.load(projectDir + '/images/add.png')
        scr.blit(add,(x,y))
        if position[0] > x and position[0]<x+25 and position[1]>y and\
                position[1]<y+25:
            add = pygame.image.load(projectDir + '/images/add_h.png')
            scr.blit(add,(x,y))
            if mouseButton == 'left':
                time.sleep(0.10)
                if self.tab in range(0,5):
                    self.tab += 1
                add = pygame.image.load(projectDir + '/images/add.png')
                scr.blit(add,(x,y))
                self.val = self.tabseq[self.tab-1]


    def scrollbar(self,scr,x,y,position,mouse,mouseButton,var,color):
        fontObj = \
                pygame.font.Font('/usr/share/fonts/TTF/OpenSans-Regular.ttf',20)
        text1 = fontObj.render('-',True,(123,199,50))
        text2 = fontObj.render('+',True,(123,199,50))
        p0 = position[0]+2
        p1 = position[1]-433
        pygame.draw.rect(scr,(60,60,60),(x,y,120,15))
        scr.blit(text1,(x-15,y-9))
        scr.blit(text2,(x+125,y-7))
        if var:
            pygame.draw.rect(scr,(30,30,30),(var-5,y-5,10,26))
        else:
            pygame.draw.rect(scr,(30,30,30),(x,y-5,10,26))
        if mouseButton == 'left':
            if p0>x+55 and p0<x+65 and p1>y-5 and p1<y+21:
                pygame.draw.rect(scr,(0,255,255),(x+55,y-5,10,26))
            if p0>x and p0<x+120 and p1>y-5 and p1<y+21:
                var = p0
                pygame.draw.rect(scr,color,(x-10,y-5,135,26))
                pygame.draw.rect(scr,(60,60,60),(x,y,120,15))
                pygame.draw.rect(scr,(30,30,30),(p0-5,y-5,10,26))
        if p0 <var+9 and p0>var-2 and p1>y-5 and p1<y+21:
            pygame.draw.rect(scr,(90,90,90),(var-5,y-5,10,26))

        if p0 <x+145 and p0>x+125 and p1>y-3 and p1<y+15:
            text2 = fontObj.render('+',True,(172,50,50))
            scr.blit(text2,(x+125,y-7))
            if mouseButton == 'left':
                text2 = fontObj.render('+',True,(0,0,0))
                scr.blit(text2,(x+125,y-7))
                if var-30>=1 and var-30<118:
                    var += 1
                time.sleep(0.10)
        if p0 <x+5 and p0>x-15 and p1>y+1 and p1<y+19:
            text1 = fontObj.render('-',True,(172,50,50))
            scr.blit(text1,(x-15,y-9))
            if mouseButton == 'left':
                text1 = fontObj.render('-',True,(0,0,0))
                scr.blit(text1,(x-15,y-9))
                if var-30>=2 and var-30<118:
                    var -= 1
                time.sleep(0.10)
        pygame.draw.rect(scr,color,(x+29,y+25,83,23))
        mouseButton = None
        return var

    def pallete(self,scr,x,y,col):
        pygame.draw.line(scr,(80,80,80),(x,y-2),(x+80,y-2),3)
        pygame.draw.line(scr,(80,80,80),(x-2,y-3),(x-2,y+30),3)
        pygame.draw.line(scr,(80,80,80),(x-3,y+31),(x+80,y+31),3)
        pygame.draw.line(scr,(80,80,80),(x+80,y+31),(x+80,y-3),3)
        pygame.draw.rect(scr,col,(x,y,80,30))

    def button(self,scr,x,y,col):
        pygame.draw.line(scr,(20,20,20),(x,y-2),(x+50,y-2),3)
        pygame.draw.line(scr,(20,20,20),(x-2,y-3),(x-2,y+30),3)
        pygame.draw.line(scr,(20,20,20),(x-3,y+31),(x+50,y+31),3)
        pygame.draw.line(scr,(20,20,20),(x+50,y+31),(x+50,y-3),3)
        pygame.draw.rect(scr,col,(x,y,50,30))

    def whichcolor_selected(self,scr,x,y,mouse,mouseButton):
        if x>10 and x<100 and y>105 and y<135:
            self.pallete(scr,10,105,(55,175,188))
            if mouse == 'down':
                self.pallete(scr,10,105,self.color('blu'))
                self.sel_color = self.color('blu')
        elif x>100 and x<180 and y>105 and y<135:
            self.pallete(scr,100,105,(103,179,30))
            if mouse == 'down':
                self.pallete(scr,100,105,self.color('gr'))
                self.sel_color = self.color('gr')
        elif x>10 and x<80 and y>145 and y<175:
            self.pallete(scr,10,145,(132,20,20))
            if mouse == 'down':
                self.pallete(scr,10,145,self.color('re'))
                self.sel_color = self.color('re')
        elif x>100 and x<180 and y>145 and y<175:
            self.pallete(scr,100,145,(78,26,98))
            if mouse == 'down':
                self.pallete(scr,100,145,self.color('pu'))
                self.sel_color = self.color('pu')
        elif x>10 and x<80 and y>185 and y<215:
            self.pallete(scr,10,185,(199,89,14))
            if mouse == 'down':
                self.pallete(scr,10,185,self.color('or'))
                self.sel_color = self.color('or')
        elif x>100 and x<180 and y>185 and y<215:
            self.pallete(scr,100,185,(225,225,225))
            if mouse == 'down':
                self.sel_color = self.color('wh')
                self.pallete(scr,100,185,self.color('wh'))
        elif x>10 and x<80 and y>225 and y<255:
            self.pallete(scr,10,225,(207,208,10))
            if mouse == 'down':
                self.sel_color = self.color('ye')
                self.pallete(scr,10,225,self.color('ye'))
        elif x>100 and x<180 and y>225 and y<255:
            self.pallete(scr,100,225,(115,58,31))
            if mouse == 'down':
                self.sel_color = self.color('br')
                self.pallete(scr,100,225,self.color('br'))
        elif x>10 and x<80 and y>265 and y<295:
            self.pallete(scr,10,265,(30,30,30))
            if mouse == 'down':
                self.sel_color = self.color('bl')
                self.pallete(scr,10,265,self.color('bl'))
        elif x>100 and x<180 and y>265 and y<295:
            self.pallete(scr,100,265,(175,83,146))
            if mouse == 'down':
                self.sel_color = self.color('pi')
                self.pallete(scr,100,265,self.color('pi'))

    def color(self,c):
        if c == 'wh':
            col = (255,255,255)
            return col
        elif c == 'bl':
            col = (0,0,0)
            return col
        elif c == 'gr':
            col = (123,199,50)
            return col
        elif c == 're':
            col = (152,30,30)
            return col
        elif c == 'ye':
            col = (231,232,34)
            return col
        elif c == 'pu':
            col = (88,36,108)
            return col
        elif c == 'or':
            col = (213,103,28)
            return col
        elif c == 'br':
            col = (123,66,39)
            return col
        elif c == 'pi':
            col = (185,93,156)
            return col
        elif c == 'blu':
            col = (85,195,218)
            return col

    def whichtool(self,position,mouse,mouseButton):
        x = position[0]
        y = position[1]
        if x<148 and x>20 and y>10 and y<64:
            if mouse == 'down':
                self.selected = 'rectangle'
            return 'rectangle'
        elif x<288 and x>160 and y>10 and y<64:
            if mouse == 'down':
                self.selected = 'line'
            return 'line'
        elif x<428 and x>300 and y>10 and y<64:
            if mouse == 'down':
                self.selected = 'ellipse'
            return 'ellipse' 
        elif x<568 and x>440 and y>10 and y<64:
            if mouse == 'down':
                self.selected = 'circle'
            return 'circle' 
        elif x<708 and x>580 and y>10 and y<64:
            if mouse == 'down':
                self.selected = 'freehand'
            return 'freehand' 
        elif x<848 and x>720 and y>10 and y<64:
            if mouse == 'down':
                self.selected = 'bucket'
            return 'bucket' 
        elif x<988 and x>860 and y>10 and y<64:
            if mouse == 'down':
                self.selected = 'clear'
            return 'clear' 
        elif x<1075 and x>1000 and y>10 and y<34:
            if mouse == 'down':
                self.selected = 'save'
            return 'save' 
        elif x<1075 and x>1000 and y>44 and y<70:
            if mouse == 'down':
                self.selected = 'open'
            return 'open' 

    def settings_ui(self,setting_Surf,position,mouse,mouseButton,scr):
        fontObj = \
                pygame.font.Font('/usr/share/fonts/TTF/OpenSans-Regular.ttf',18)
        pygame.draw.line(setting_Surf,(0,0,0),(0,2),(195,2),6)
        pygame.draw.line(setting_Surf,(0,0,0),(2,2),(2,287),6)
        pygame.draw.line(setting_Surf,(0,0,0),(0,287),(195,287),6)
        pygame.draw.line(setting_Surf,(0,0,0),(182,0),(182,287),6)
        text1 = fontObj.render('Brush Size',True,(10,10,10))
        text2 = fontObj.render('Decrease Width',True,(10,10,10))
        text3 = fontObj.render('Decrease Height',True,(10,10,10))
        text4 = fontObj.render('Copy',True,(10,10,10))
        text5 = fontObj.render('Red',True,(10,10,10))
        text6 = fontObj.render('Green',True,(10,10,10))
        text7 = fontObj.render('Blue',True,(10,10,10))
        if self.sett == 0:
            color = (40,40,40)
            pygame.draw.rect(setting_Surf,color,(6,6,178,279))
            pygame.draw.rect(setting_Surf,color,(51,9,90,23))
            setting_Surf.blit(text1,(53,10))
            pygame.draw.rect(setting_Surf,color,(26,90,135,23))
            setting_Surf.blit(text2,(28,90))
            pygame.draw.rect(setting_Surf,color,(26,178,139,23))
            setting_Surf.blit(text3,(28,178))
            pygame.draw.line(setting_Surf,(0,0,0),(182,0),(182,287),6)
            a1 =\
                    self.scrollbar(setting_Surf,30,40,position,mouse,mouseButton,self.scx1,color)
            self.size = a1 - 30
            self.scx1 = a1
            self.showval(setting_Surf,a1-30,(60,60),'Value: ')
            b1 =\
                    self.scrollbar(setting_Surf,30,120,position,mouse,mouseButton,self.scx2,color)
            self.gx = 879 - (5*(b1-31)) 
            self.scx2 = b1
            self.showval(setting_Surf,self.gx,(50,140),'Value: ')
            c1 =\
                    self.scrollbar(setting_Surf,30,210,position,mouse,mouseButton,self.scx3,color)
            self.gy = 590 - (3*(c1-31)) 
            self.scx3 = c1
            self.showval(setting_Surf,self.gy,(50,230),'Value: ')

        elif self.sett == 1:
            color = (40,40,40)
            pygame.draw.rect(setting_Surf,color,(6,6,178,279))
            pygame.draw.rect(setting_Surf,color,(51,9,90,23))
            pygame.draw.rect(setting_Surf,color,(26,90,135,23))
            pygame.draw.rect(setting_Surf,color,(26,178,139,23))
            pygame.draw.line(setting_Surf,(0,0,0),(182,0),(182,287),6)
            self.pallete(setting_Surf,10,15,(80,80,80))
            self.pallete(setting_Surf,97,15,(80,80,80))
            setting_Surf.blit(text4,(30,17))
            if position[0]>10 and position[0]<90 and position[1]>445\
                    and position[1]<480:
                self.pallete(setting_Surf,10,15,(100,100,100))
                setting_Surf.blit(text4,(30,17))
                if mouseButton == 'left':
                    self.selected = 'copy'
                    self.pallete(setting_Surf,10,15,(80,80,80))
                    setting_Surf.blit(text4,(30,17))
                
        elif self.sett == 2:
            self.r,self.g,self.b = self.sel_color
            color = (40,40,40)
            pygame.draw.rect(setting_Surf,color,(6,6,178,279))
            pygame.draw.rect(setting_Surf,color,(51,9,90,23))
            setting_Surf.blit(text5,(28,10))
            pygame.draw.rect(setting_Surf,color,(26,90,135,23))
            setting_Surf.blit(text6,(28,90))
            pygame.draw.rect(setting_Surf,color,(26,178,139,23))
            setting_Surf.blit(text7,(28,178))
            pygame.draw.line(setting_Surf,(0,0,0),(182,0),(182,287),6)
            a =\
                    self.scrollbar(setting_Surf,30,40,position,mouse,mouseButton,self.scx4,color)
            self.r = 2.15*(a - 30)
            self.scx4 = a
            b =\
                    self.scrollbar(setting_Surf,30,120,position,mouse,mouseButton,self.scx5,color)
            self.g = 2.15*(b - 30)
            self.scx5 = b
            c =\
                    self.scrollbar(setting_Surf,30,210,position,mouse,mouseButton,self.scx6,color)
            self.b = 2.15*(c - 30)
            self.scx6 = c
            self.sel_color = self.r,self.g,self.b
            self.showval(setting_Surf,self.r,(60,60),'Value: ')
            self.showval(setting_Surf,self.g,(60,140),'Value: ')
            self.showval(setting_Surf,self.b,(60,230),'Value: ')

    def ui(self,scr,position,mouse,mouseButton):
        # replace it with your project dir 
        projectDir = self.projectDir

        fontObj = \
                pygame.font.Font('/usr/share/fonts/TTF/OpenSans-Regular.ttf',18)
        fontObj2 = \
                pygame.font.Font('/usr/share/fonts/TTF/OpenSans-Regular.ttf',15)
        text1 = fontObj.render('Rectangle',True,(90,90,90))
        text2 = fontObj.render('Line',True,(90,90,90))
        text3 = fontObj.render('Ellipse',True,(90,90,90))
        text4 = fontObj.render('Circle',True,(90,90,90))
        text5 = fontObj.render('Freehand',True,(90,90,90))
        text6 = fontObj.render('Bucket',True,(90,90,90))
        text7 = fontObj.render('Clear',True,(90,90,90))
        text8 = fontObj2.render('SAVE',True,(20,20,20))
        text9 = fontObj2.render('OPEN',True,(20,20,20))

        box = pygame.image.load(projectDir + '/images/box.png')
        save = pygame.image.load(projectDir+ '/images/save.png')
        tabular = pygame.image.load(projectDir + '/images/tabular.png')

        pygame.draw.rect(scr,(30,30,30),(0,0,1080,90))
        pygame.draw.rect(scr,(30,30,30),(0,0,190,720))
        pygame.draw.line(scr,(0,0,0),(0,90),(1080,90),6)
        pygame.draw.line(scr,(0,0,0),(190,90),(190,720),6)
        pygame.draw.line(scr,(0,0,0),(190,716),(1080,716),6)
        pygame.draw.line(scr,(0,0,0),(1076,90),(1076,716),6)
        pygame.draw.line(scr,(0,0,0),(190,120),(1076,120),6)

        scr.blit(box,(20,10))
        scr.blit(text1,(44,25))
        scr.blit(box,(160,10))
        scr.blit(text2,(205,25))
        scr.blit(box,(300,10))
        scr.blit(text3,(335,25))
        scr.blit(box,(440,10))
        scr.blit(text4,(480,25))
        scr.blit(box,(580,10))
        scr.blit(text5,(604,25))
        scr.blit(box,(720,10))
        scr.blit(text6,(749,25))
        scr.blit(box,(860,10))
        scr.blit(text7,(899,25))
        scr.blit(save,(1000,10))
        scr.blit(text8,(1020,13))
        scr.blit(save,(1000,45))
        scr.blit(text9,(1018,49))

        scr.blit(tabular,(194,93))

        tool = self.whichtool(position,mouse,mouseButton)
        for a in range(0,self.tab):
            if self.tabarr[self.val] == self.tabarr[self.tabseq[a]]:
                self.var = 1
            else:
                self.var = 0
            self.tabar(scr,self.tabarr[self.tabseq[a]],93,position,mouse,mouseButton,projectDir,self.var)
        if self.tab <=0:
            self.val = self.tabseq[0]
                    

        self.plus(scr,1050,93,position,mouse,mouseButton,projectDir)

        if mouse == 'motion':
            if tool == 'rectangle':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(20,10))
                scr.blit(text1,(44,25))
            elif tool == 'line':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(160,10))
                scr.blit(text2,(205,25))
            elif tool == 'ellipse':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(300,10))
                scr.blit(text3,(335,25))
            elif tool == 'circle':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(440,10))
                scr.blit(text4,(480,25))
            elif tool == 'freehand':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(580,10))
                scr.blit(text5,(604,25))
            elif tool == 'bucket':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(720,10))
                scr.blit(text6,(749,25))
            elif tool == 'clear':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(860,10))
                scr.blit(text7,(899,25))
            elif tool == 'save':
                save = pygame.image.load(projectDir + '/images/save_h.png')
                scr.blit(save,(1000,10))
                scr.blit(text8,(1020,13))
            elif tool == 'open':
                save = pygame.image.load(projectDir + '/images/save_h.png')
                scr.blit(save,(1000,45))
                scr.blit(text9,(1018,49))

        elif mouse == 'down':
            if tool == 'rectangle':
                box = pygame.image.load(projectDir + '/images/box_click.png')
                scr.blit(box,(20,10))
                scr.blit(text1,(44,25))
            elif tool == 'line':
                box = pygame.image.load(projectDir + '/images/box_click.png')
                scr.blit(box,(160,10))
                scr.blit(text2,(205,25))
            elif tool == 'ellipse':
                box = pygame.image.load(projectDir + '/images/box_click.png')
                scr.blit(box,(300,10))
                scr.blit(text3,(335,25))
            elif tool == 'circle':
                box = pygame.image.load(projectDir + '/images/box_click.png')
                scr.blit(box,(440,10))
                scr.blit(text4,(480,25))
            elif tool == 'freehand':
                box = pygame.image.load(projectDir + '/images/box_click.png')
                scr.blit(box,(580,10))
                scr.blit(text5,(604,25))
            elif tool == 'bucket':
                box = pygame.image.load(projectDir + '/images/box_click.png')
                scr.blit(box,(720,10))
                scr.blit(text6,(749,25))
            elif tool == 'clear':
                box = pygame.image.load(projectDir + '/images/box_click.png')
                scr.blit(box,(860,10))
                scr.blit(text7,(899,25))
            elif tool == 'save':
                save = pygame.image.load(projectDir + '/images/save.png')
                scr.blit(save,(1000,10))
                scr.blit(text8,(1020,13))
            elif tool == 'open':
                save = pygame.image.load(projectDir + '/images/save.png')
                scr.blit(save,(1000,45))
                scr.blit(text9,(1018,49))

        elif mouse == 'up':
            if tool == 'rectangle':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(20,10))
                scr.blit(text1,(44,25))
            elif tool == 'line':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(160,10))
                scr.blit(text2,(205,25))
            elif tool == 'ellipse':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(300,10))
                scr.blit(text3,(335,25))
            elif tool == 'circle':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(440,10))
                scr.blit(text4,(480,25))
            elif tool == 'freehand':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(580,10))
                scr.blit(text5,(604,25))
            elif tool == 'bucket':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(720,10))
                scr.blit(text6,(749,25))
            elif tool == 'clear':
                box = pygame.image.load(projectDir + '/images/box_hover.png')
                scr.blit(box,(860,10))
                scr.blit(text7,(899,25))
            elif tool == 'save':
                save = pygame.image.load(projectDir + '/images/save_h.png')
                scr.blit(save,(1000,10))
                scr.blit(text8,(1020,13))
            elif tool == 'open':
                save = pygame.image.load(projectDir + '/images/save_h.png')
                scr.blit(save,(1000,45))
                scr.blit(text9,(1018,49))

        self.pallete(scr,10,105,self.color('blu'))
        self.pallete(scr,100,105,self.color('gr'))
        self.pallete(scr,10,145,self.color('re'))
        self.pallete(scr,100,145,self.color('pu'))
        self.pallete(scr,10,185,self.color('or'))
        self.pallete(scr,100,185,self.color('wh'))
        self.pallete(scr,10,225,self.color('ye'))
        self.pallete(scr,100,225,self.color('br'))
        self.pallete(scr,10,265,self.color('bl'))
        self.pallete(scr,100,265,self.color('pi'))
        self.pallete(scr,10,319,self.sel_color)
        cor = fontObj.render('X         Y',True,(100,100,100))
        corx = fontObj.render(str(position[0]),True,(200,200,200))
        cory = fontObj.render(str(position[1]),True,(200,200,200))
        selected = fontObj.render('Tool: '+str(self.selected),True,(200,200,200))
        scr.blit(cor,(100,310))
        scr.blit(corx,(100,332))
        scr.blit(cory,(150,332))
        scr.blit(selected,(10,353))
        self.whichcolor_selected(scr,position[0],position[1],mouse,mouseButton)

        if position[0] >15 and position[0] <65 and position[1]>388 and\
                position[1]<418:
                    self.col1 = (56,112,119)
                    self.col2 = (26,82,89)
                    self.col3 = (26,82,89)
                    if mouse == 'down':
                        self.col1 = (16,72,79)
                        self.sett = 0
        elif position[0] >65 and position[0] <115 and position[1]>388 and\
                position[1]<418:
                    self.col1 = (26,82,89)
                    self.col2 = (56,112,119)
                    self.col3 = (26,82,89)
                    if mouse == 'down':
                        self.col2 = (16,72,79)
                        self.sett = 1
        elif position[0] >115 and position[0] <165 and position[1]>388 and\
                position[1]<418:
                    self.col1 = (26,82,89)
                    self.col2 = (26,82,89)
                    self.col3 = (56,112,119)
                    if mouse == 'down':
                        self.col3 = (16,72,79)
                        self.sett = 2
        else:
            self.col1 = (26,82,89)
            self.col2 = (26,82,89)
            self.col3 = (26,82,89)
        self.button(scr,15,392,self.col1)
        self.button(scr,68,392,self.col2)
        self.button(scr,121,392,self.col3)

obj_paint = paint()
pygame.init()
screen = pygame.display.set_mode((obj_paint.x,obj_paint.y))

game_Surf1 = pygame.surface.Surface((obj_paint.gx,obj_paint.gy))
game_Surf2 = pygame.surface.Surface((obj_paint.gx,obj_paint.gy))
game_Surf3 = pygame.surface.Surface((obj_paint.gx,obj_paint.gy))
game_Surf4 = pygame.surface.Surface((obj_paint.gx,obj_paint.gy))
game_Surf5 = pygame.surface.Surface((obj_paint.gx,obj_paint.gy))

game_Surf = game_Surf1

setting_Surf = pygame.surface.Surface((186,290))
setting_Surf.fill((255,255,255))
clock = pygame.time.Clock()
screen.fill(obj_paint.color('wh'))
game_Surf.fill((255,255,255))
position = (0,0)
cpy = None
mouseButton = None
mouse = None
currx = obj_paint.gx
curry = obj_paint.gy
c=0
pre = None
tab_sel = 1

arr1,arr2,arr3,arr4,arr5 = 0,0,0,0,0

while obj_paint.run == True:
    if tab_sel != obj_paint.val:
        tab_sel = obj_paint.val
        if tab_sel == 1:
            game_Surf = game_Surf1
            if arr1 == 0:
                game_Surf.fill((255,255,255))
                arr1 = 1
        elif tab_sel == 2:
            game_Surf = game_Surf2
            if arr2 == 0:
                game_Surf.fill((255,255,255))
                arr2 = 1
        elif tab_sel == 3:
            game_Surf = game_Surf3
            if arr3 == 0:
                game_Surf.fill((255,255,255))
                arr3 = 1
        elif tab_sel == 4:
            game_Surf = game_Surf4
            if arr4 == 0:
                game_Surf.fill((255,255,255))
                arr4 = 1
        elif tab_sel == 5:
            game_Surf = game_Surf5
            if arr5 == 0:
                game_Surf.fill((255,255,255))
                arr5 = 1
        if 1 not in obj_paint.tabseq[0:obj_paint.tab]:
            game_Surf1 = pygame.surface.Surface((obj_paint.gx,obj_paint.gy))
            game_Surf1.fill((255,255,255))
        if 2 not in obj_paint.tabseq[0:obj_paint.tab]:
            game_Surf2 = pygame.surface.Surface((obj_paint.gx,obj_paint.gy))
            game_Surf2.fill((255,255,255))
        if 3 not in obj_paint.tabseq[0:obj_paint.tab]:
            game_Surf3 = pygame.surface.Surface((obj_paint.gx,obj_paint.gy))
            game_Surf3.fill((255,255,255))
        if 4 not in obj_paint.tabseq[0:obj_paint.tab]:
            game_Surf4 = pygame.surface.Surface((obj_paint.gx,obj_paint.gy))
            game_Surf4.fill((255,255,255))
        if 5 not in obj_paint.tabseq[0:obj_paint.tab]:
            game_Surf5 = pygame.surface.Surface((obj_paint.gx,obj_paint.gy))
            game_Surf5.fill((255,255,255))


    if obj_paint.gx !=currx or obj_paint.gy!=curry:
        game_Surf = pygame.surface.Surface((obj_paint.gx,obj_paint.gy))
        game_Surf.fill((255,255,255))
        if cpy:
            game_Surf.blit(cpy,(0,0))
        currx = obj_paint.gx
        curry = obj_paint.gy
        pygame.draw.rect(screen,(30,30,30),(currx,124,currx,595),0)
        pygame.draw.rect(screen,(30,30,30),(194,curry,884,curry))

    screen.blit(game_Surf,(194,124))
    obj_paint.ui(screen,position,mouse,mouseButton)
    obj_paint.settings_ui(setting_Surf,position,mouse,mouseButton,screen)
    screen.blit(setting_Surf,(0,430))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            obj_paint.run = False

        elif obj_paint.selected == 'clear':
            game_Surf = pygame.surface.Surface((currx,curry))
            game_Surf.fill((255,255,255))
            obj_paint.selected = None
            cpy = None
            mouseButton = None

        elif obj_paint.selected == 'save':
            obj_paint.selected = None
            root = Tk()
            root.filename =  filedialog.asksaveasfilename(initialdir =\
                    obj_paint.projectDir,title = "Select file",filetypes = \
                    (("jpeg files","*.jpg"),("all files","*.*")))
            pygame.image.save(game_Surf,root.filename)
            print(root.filename)
            f = open(str(root.filename+".bat"),'w')
            f.write(str(currx)+" ")
            f.write(str(curry))
            f.close()
            root.destroy()

        elif obj_paint.selected == 'open':
            obj_paint.selected = None
            root = Tk()
            root.filename =  filedialog.askopenfilename(initialdir =\
                    obj_paint.projectDir,title = "Select file",filetypes = \
                    (("jpeg files","*.jpg"),("all files","*.*")))
            if root.filename:
                img = pygame.image.load(root.filename)
                f = open(str(root.filename),'r')
            else:
                pass
            game_Surf = img
            screen.blit(game_Surf,(194,124))
            root.destroy()

        elif event.type == pygame.MOUSEMOTION:
            mouse = 'motion'
            pos_motion = event.pos
            position = pos_motion
            if obj_paint.selected == 'freehand':
                if mouseButton == 'left':
                    if c==0:
                        x1,y1 = pos_down[0],pos_down[1]
                        x2,y2 = pos_motion[0],pos_motion[1]
                        c=1
                    pygame.draw.line(game_Surf,obj_paint.sel_color,(x1-194,y1-124),\
                            (x2-194,y2-124))
                    x1,y1 = x2,y2
                    x2,y2 = pos_motion[0],pos_motion[1]
                    screen.blit(game_Surf,(194,124))
            elif obj_paint.selected == 'line':
                if mouseButton == 'left':
                    x1,y1 = pos_down[0],pos_down[1]
                    x2,y2 = pos_motion[0],pos_motion[1]
                    game_Surf.fill((255,255,255))
                    if cpy:
                        game_Surf.blit(cpy,(0,0))
                    pygame.draw.line(game_Surf,obj_paint.sel_color,(x1-194,y1-124),\
                            (x2-194,y2-124),obj_paint.size)
                    screen.blit(game_Surf,(194,124))

            elif obj_paint.selected == 'rectangle':
                if mouseButton == 'left':
                    x1,y1 = pos_down[0],pos_down[1]
                    x2,y2 = pos_motion[0],pos_motion[1]
                    game_Surf.fill((255,255,255))
                    if cpy:
                        game_Surf.blit(cpy,(0,0))
                    try:
                        pygame.draw.rect(game_Surf,obj_paint.sel_color,(x1-194,y1-124,\
                                x2-x1,y2-y1),1)
                    except ValueError:
                        pass
                    screen.blit(game_Surf,(194,124))

            elif obj_paint.selected == 'copy':
                if mouseButton == 'left':
                    x1,y1 = pos_down[0],pos_down[1]
                    x2,y2 = pos_motion[0],pos_motion[1]
                    game_Surf.fill((255,255,255))
                    if cpy:
                        game_Surf.blit(cpy,(0,0))
                    try:
                        pygame.draw.rect(game_Surf,(0,0,0),(x1-194,y1-124,\
                                x2-x1,y2-y1),1)
                        if x1<x2:
                            for i in range(x1,x2,3):
                                pygame.draw.line(game_Surf,(255,255,255),(i-194,y1-124),\
                                        ((i-194)+1,y1-124),3)
                                pygame.draw.line(game_Surf,(255,255,255),(i-194,y2-124),\
                                        ((i-194)+1,y2-124),3)
                        else:
                            for i in range(x2,x1,3):
                                pygame.draw.line(game_Surf,(255,255,255),(i-194,y1-124),\
                                        ((i-194)+1,y1-124),3)
                                pygame.draw.line(game_Surf,(255,255,255),(i-194,y2-124),\
                                        ((i-194)+1,y2-124),3)
                         
                        if y1<y2:
                            for i in range(y1,y2,3):
                                pygame.draw.line(game_Surf,(255,255,255),(x1-194,i-124),\
                                        (x1-194,i-124+1),3)
                                pygame.draw.line(game_Surf,(255,255,255),(x2-194,i-124),\
                                        (x2-194,i-124+1),3)
                        else:
                            for i in range(y2,y1,3):
                                pygame.draw.line(game_Surf,(255,255,255),(x1-194,i-124),\
                                        (x1-194,i-124+1),3)
                                pygame.draw.line(game_Surf,(255,255,255),(x2-194,i-124),\
                                        (x2-194,i-124+1),3)


                    except ValueError:
                        pass
                    screen.blit(game_Surf,(194,124))

            elif obj_paint.selected == 'copy_movin':
                screen.blit(copy_surf,(pos_motion[0]-(x2-x1)//2,pos_motion[1]-(y2-y1)//2))

            elif obj_paint.selected == 'ellipse':
                if mouseButton == 'left':
                    x1,y1 = pos_down[0],pos_down[1]
                    x2,y2 = pos_motion[0],pos_motion[1]
                    game_Surf.fill((255,255,255))
                    if cpy:
                        game_Surf.blit(cpy,(0,0))
                    radx = max(x2-x1,1)
                    rady = max(y2-y1,1)
                    sz2 = 10
                    pygame.draw.ellipse(screen,obj_paint.sel_color,(x1,y1,radx,rady), sz2 if sz2 < max(radx, rady) else 0)
                    screen.blit(game_Surf,(194,100))


        elif event.type == pygame.MOUSEBUTTONDOWN:
            copy = game_Surf.copy()
            mouse = 'down'
            pos_down = event.pos
            position = pos_down
            if event.button == 1:
                mouseButton = 'left'
            elif event.button == 3:
                mouseButton = 'right'
            if obj_paint.selected == 'bucket' and pos_down[0]>192 and\
                    pos_down[1] > 124:
                x = pos_down[0]-194
                y = pos_down[1]-124
                arr3d = pygame.surfarray.array3d(game_Surf)
                arr3d = arr3d.tolist()
                obj_paint.floodfill_lower(arr3d,x,y,obj_paint.sel_color,\
                        game_Surf.get_at((x,y)))
                obj_paint.floodfill_upper(arr3d,x+1,y,obj_paint.sel_color,\
                        game_Surf.get_at((x,y)))
                pygame.surfarray.blit_array(game_Surf,numpy.array(arr3d))
                screen.blit(game_Surf,(194,124))

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse = 'up'
            mouseButton = None
            pos_up = event.pos
            position = pos_up
            cpy = game_Surf.copy()
            if obj_paint.selected == 'copy':
                x1,y1 = pos_down[0],pos_down[1]
                x2,y2 = pos_up[0],pos_up[1]
                if x2<x1:
                    x2,x1 = x1,x2
                if y2<y1:
                    y2,y1 = y1,y2
                if x1 in range(194,1081) and x2 in\
                range(194,1081) and y1 in range(124,721) and \
                y2 in range(124,721):
                    game_Surf.fill((255,255,255))
                    copy_surf = pygame.surface.Surface((x2-x1,y2-y1))
                    copy_surf.blit(copy,(0,0),pygame.Rect(x1-194,y1-124,x2-194,y2-124))
                    game_Surf.blit(copy,(0,0))
                    screen.blit(game_Surf,(194,124))
                    cpy = copy
                    copy = None
                    obj_paint.selected = 'copy_movin'
            c = 0
    if obj_paint.selected == 'copy_movin':
        screen.blit(copy_surf,(pos_motion[0]-(x2-x1)//2,pos_motion[1]-(y2-y1)//2))
        if mouse == 'down':
            game_Surf.blit(copy_surf,(pos_motion[0]-(x2-x1)//2-194,\
                pos_motion[1]-(y2-y1)//2-124))
            screen.blit(game_Surf,(194,124))
            obj_paint.selected = None
            copy = None
            copy_surf = None

    pygame.display.update()
    clock.tick(60)
