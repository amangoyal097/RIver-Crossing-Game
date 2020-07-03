import pygame
pygame.init()


class GlobalThings(object):  # gloabl objects used
    def __init__(self):
        self.sheight = 1000
        self.swidth = 1500
        self.play = True         # variable for game loop
        self.strtscreen = True  # Starting screen
        self.scr = pygame.display.set_mode((self.swidth, self.sheight))
        self.strt = pygame.image.load('./images/start.png')
        self.fin = pygame.image.load('./images/finish.png')
        self.life = pygame.image.load('./images/life.png')
        self.obm = pygame.image.load('./images/mobst.png')
        self.obf = pygame.image.load('./images/fobst.png')
        self.p1img = pygame.image.load('./images/player1.png')
        self.p2img = pygame.image.load('./images/player2.png')
        self.strtbg = pygame.image.load('./images/strtbg.jpg')
        self.fontobj = pygame.font.Font('./font/font.ttf', 40)
        self.fobj = pygame.font.Font('./font/font.ttf', 80)
        self.bgcolor = (100, 100, 255)
        self.pcolor = (16, 49, 107)
        self.scorecolor = (246, 75, 60)
        self.bankcolor = (253, 211, 101)
        self.slabcolor = (25, 41, 101)
        self.wincolor = (254, 152, 1)
        self.govercolor = (33, 191, 115)
        self.endcolor = (0, 0, 0)
        self.p1end = (206, 15, 61)
        self.msgbg = (237, 237, 237)
        self.failcolor = (227, 34, 73)

    def transform(self):  # scaling images to required size
        self.strt = pygame.transform.scale(self.strt, (300, 90))
        self.fin = pygame.transform.scale(self.fin, (300, 90))
        self.life = pygame.transform.scale(self.life, (40, 30))
        self.strtbg = pygame.transform.scale(self.strtbg, (1500, 1000))
    
    def success(self):  # display msg for players
        bankh = 90
        successmsg = self.fobj.render("SUCCESS", 1, self.govercolor)
        pygame.draw.rect(self.scr, self.msgbg,
                         (0, self.sheight - bankh, self.swidth, bankh))
        self.scr.blit(successmsg, (600, self.sheight - bankh))
        pygame.display.update()

    def fail(self):  # display on obstacle hit
        bankh = 90
        failmsg = self.fobj.render("COLLIDED", 1, self.failcolor)
        pygame.draw.rect(self.scr, self.msgbg,
                         (0, self.sheight - bankh, self.swidth, bankh))
        self.scr.blit(failmsg, (600, self.sheight - bankh))
        pygame.display.update()
