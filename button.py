import pygame as pg
pg.init()

class button():
    def __init__(self,screen,centerX,centerY,height,colour,text):
        self.screen = screen
        self.centerX = centerX
        self.centerY = centerY
        self.height = height
        self.y = self.centerY - 0.5 * self.height
        self.colour = pg.Color(colour)
        self.colourValue = (self.colour[0],self.colour[1],self.colour[2],self.colour[3])
        self.text = text
        self.textColour = (255,255,255) 
        self.click = 0
        self.active = True
        self.pos = pg.mouse.get_pos()
        self.font = pg.font.SysFont('Calibri', self.height, True, False)

    def drawButton(self):
        self.renderedText = self.font.render(self.text, True, (self.textColour))
        self.textWidth = self.renderedText.get_width()
        self.textHeight = self.renderedText.get_height()
        self.width = self.textWidth + 10
        self.x = self.centerX - 0.5 * self.width
        self.button = pg.rect.Rect([self.x,self.y,self.width,self.height])
        self.textX = self.x + 0.5 * self.width - 0.5 * self.textWidth
        self.textY = self.y + 0.5 * self.height - 0.5 * self.textHeight + 3
        pg.draw.rect(self.screen, self.colourValue, self.button)
        self.screen.blit(self.renderedText,[self.textX,self.textY])
        
    def isPressed(self):
        self.pos = pg.mouse.get_pos()
        self.click = pg.mouse.get_pressed()[0]
        if self.button.collidepoint(self.pos):
            self.colourValue = (self.colour[0]*0.5,self.colour[1]*0.5,self.colour[2]*0.5,self.colour[3]*0.5)
            self.textColour = (255 * 0.5, 255 * 0.5, 255 * 0.5)
        else:
            self.colourValue = self.colour
            self.textColour = (255,255,255) 
        if self.button.collidepoint(self.pos) and self.click == 1 and self.active == True:
            self.active = False
            return(True)
        elif self.click == 0:
            self.active = True
            return(False)
        else:
            return(False)
