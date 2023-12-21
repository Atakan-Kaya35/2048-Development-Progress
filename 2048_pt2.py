import random
import pygame
import math
import time

# intialize pygame
pygame.init()


class Values():
    def __init__(self, vvalue):
        self.vvalue = vvalue
        self.not_changedd = True

    def modify(self):
        self.not_changedd = False

    def unmodify(self):
        self.not_changedd = True

    def value_change(self, num):
        self.vvalue = num


class Board():
    def __init__(self, valuess):
        pygame.display.set_caption("Codebasics Snake And Apple Game")
        self.surface = pygame.display.set_mode((500, 500))
        self.valuess = valuess

    def left_shift(self):
        modified = []
        for _ in range(3):
            for i in range(4):
                for j in range(3):
                    if self.valuess[i][j].vvalue == 0:
                        self.valuess[i][j].value_change(self.valuess[i][j + 1].vvalue)
                        self.valuess[i][(j + 1)].value_change(0)
                    elif self.valuess[i][j].vvalue == self.valuess[i][j + 1].vvalue and self.valuess[i][j].not_changedd == True and self.valuess[i][j+1].not_changedd == True:
                        self.valuess[i][j].value_change(self.valuess[i][j + 1].vvalue * 2)
                        self.valuess[i][j + 1].value_change(0)
                        self.valuess[i][j].modify()
                        modified.append([i, j])
        for x, y in modified:
            self.valuess[x][y].unmodify()

    def right_shift(self):
        modified = []
        for _ in range(3):
            for i in range(4):
                for j in range(3, 0, -1):
                    if self.valuess[i][j].vvalue == 0:
                        self.valuess[i][j].value_change(self.valuess[i][j - 1].vvalue)
                        self.valuess[i][(j - 1)].value_change(0)
                    elif self.valuess[i][j].vvalue == self.valuess[i][j - 1].vvalue and self.valuess[i][j].not_changedd == True and self.valuess[i][j-1].not_changedd == True:
                        self.valuess[i][j].value_change(self.valuess[i][j - 1].vvalue * 2)
                        self.valuess[i][j - 1].value_change(0)
                        self.valuess[i][j].modify()
                        modified.append([i, j])
        for x, y in modified:
            self.valuess[x][y].unmodify()

    def down_shift(self):
        modified = []
        for _ in range(3):
            for i in range(3, -1, -1):
                for j in range(3, 0, -1):
                    if self.valuess[j][i].vvalue == 0:
                        self.valuess[j][i].value_change(self.valuess[j - 1][i].vvalue)
                        self.valuess[(j - 1)][i].value_change(0)
                    elif self.valuess[j][i].vvalue == self.valuess[j - 1][i].vvalue and self.valuess[j][i].not_changedd == True and self.valuess[j-1][i].not_changedd == True:
                        self.valuess[j][i].value_change(self.valuess[j - 1][i].vvalue * 2)
                        self.valuess[j - 1][i].value_change(0)
                        self.valuess[j][i].modify()
                        modified.append([j, i])

        for x, y in modified:
            self.valuess[x][y].unmodify()


    def up_shift(self):
        modified = []
        for _ in range(len(self.valuess)):
            for i in range(len(self.valuess)):
                for j in range(len(self.valuess) - 1):
                    if self.valuess[j][i].vvalue == 0:
                        self.valuess[j][i].value_change(self.valuess[j + 1][i].vvalue)
                        self.valuess[j + 1][i].value_change(0)
                    elif self.valuess[j][i].vvalue == self.valuess[j + 1][i].vvalue and self.valuess[j][i].not_changedd == True and self.valuess[j+1][i].not_changedd == True:
                        self.valuess[j][i].value_change(self.valuess[j][i].vvalue * 2)
                        self.valuess[j + 1][i].value_change(0)
                        self.valuess[j][i].modify()
                        modified.append([j, i])
        for x, y in modified:
            self.valuess[x][y].unmodify()


    def display(self):
        print("\n" * 3)
        for x in range(len(self.valuess)):
            res = "\t\t\t"
            for i in range(len(self.valuess)):
                res += str(self.valuess[x][i].vvalue)
                if i < len(self.valuess) - 1: res += "\t,\t"
            print(res)
            if x < len(self.valuess) - 1:
                print("\t", ("\t-\t" * 4))

    def add_num(self):
        not_done = True
        x = 0
        while not_done:
            x += 1
            i = random.randint(0, 3)
            j = random.randint(0, 3)
            if self.valuess[i][j].vvalue == 0:
                self.valuess[i][j].value_change(random.choice([2, 2, 2, 4]))
                not_done = False
            if x > 200:
                self.surface.fill((0,0,0))
                lost = font.render(str("You lost"), True, (255, 155, 60))
                self.surface.blit(lost, (150,400))
                print("here")
                pygame.display.update()

                time.sleep(5)
                exit()
                not_done = False



list = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def show_values(x,y, cordx, cordy):
    score = font.render(str(attemt.valuess[x][y].vvalue), True, (255, 155, 60))
    sccore = font1.render(str(attemt.valuess[x][y].vvalue), True, (255, 155, 60))
    if attemt.valuess[x][y].vvalue == 0:
        zero = font.render(".", True, (255, 155, 60))
        attemt.surface.blit(zero, (cordx, cordy))

    elif attemt.valuess[x][y].vvalue < 100:
        attemt.surface.blit(score, (cordx,cordy))

    else:
        attemt.surface.blit(sccore, (cordx, cordy))

for i in range(4):
    for j in range(4):
        list[i][j] = Values(0)

list[0][0].value_change(4)
list[1][0].value_change(4)
list[2][0].value_change(4)

attemt = Board(list)

cordlist = [0, 150, 300, 450]

font = pygame.font.Font("freesansbold.ttf", 50)
font1 = pygame.font.Font("freesansbold.ttf", 40)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                attemt.left_shift()
                attemt.add_num()
                attemt.display()


            if event.key == pygame.K_RIGHT:
                attemt.right_shift()
                attemt.add_num()
                attemt.display()


            if event.key == pygame.K_UP:
                attemt.up_shift()
                attemt.add_num()
                attemt.display()



            if event.key == pygame.K_DOWN:

                attemt.down_shift()
                attemt.add_num()
                attemt.display()

    for i in range(4):
        for j in range(4):
            show_values(j,i,cordlist[i],cordlist[j])

    pygame.display.update()
    attemt.surface.fill((0, 0, 0))

