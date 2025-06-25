import pygame as pg

pg.init()

# data temporary storage ----
SIZE = (750 * 0.68, 1334 * 0.68)
# -----

screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()

background = pg.image.load("assets/background.jpg").convert()
background = pg.transform.scale(background, SIZE)

class DragCard():
    def __init__(self, rect):
        self.rect = rect
        self.image = None

        self.pos = None
        self.clickPos = None
        self.offset = None

    def updateMouse(self):
        self.pos = pg.mouse.get_pos()
        pressed = pg.mouse.get_pressed()[0]

        if self.rect.collidepoint(self.pos) and pressed: # initial click
            if self.clickPos == None:
                self.image = background.subsurface(self.rect) # subsurface card
                self.clickPos = self.pos # initial condition

        if pressed:
            if self.clickPos == None:
                self.clickPos = self.pos # prevents collision (picking up card) if already clicked elsewhere

        if not(pressed): # image disappears if not clicking
            self.image = None 
            self.clickPos = None

    def update(self):
        if self.clickPos != None: # update offset
            self.offset = (self.pos[0] - self.clickPos[0], self.pos[1] - self.clickPos[1])
    
    def draw(self, screen): # draw image
        if self.image != None:
            screen.blit(self.image, (self.rect.x + self.offset[0], self.rect.y + self.offset[1]))
        
    


    def keys(self, events): # debug to screenshot screen
        for ev in events:
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_s:
                    pg.image.save(screen, "screenshot1.png")


#TEST
IWrect = pg.Rect((116, 753), (205-116, 863-753)) # ice wizard
#TEST

card = DragCard(IWrect)
running = True
while running:
    events = pg.event.get()
    for ev in events:
        if ev.type == pg.QUIT:
            running = False
    screen.blit(background, (0, 0))

    # input
    card.updateMouse()
    card.update()
    card.draw(screen)

    # debug
    card.keys(events)


    pg.display.flip()
    clock.tick()

