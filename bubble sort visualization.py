import sys
import pygame
import time
from pygame.locals import *
def main():
    print("--------------Bubble Sort Visualization-------------\n-----------------By Rahul choudhary-----------------")
    inarray = inarray=list(map(int,input("Enter the Array\n\n-> ").split()))
    print("\nArray Before Sorting:\n")
    print(inarray)
    pygame.init()
    screen = pygame.display.set_mode((960, 540))
    pygame.display.set_caption('Bubble Sort')
    screen.fill([255, 255, 255])
    pygame.font.init()
    font = pygame.font.SysFont('Inconsolata-Regular', int(pygame.display.get_surface().get_size()[0]/(len(inarray)+10)))
    bubble_sort(screen, font, inarray)
    print("Array After Sorting:\n")
    print(inarray)
    time.sleep(5)
    pygame.quit()
def bubble_sort(screen, font, inarray):
    check = False
    l = len(inarray)
    m = max(inarray)
    w, h = pygame.display.get_surface().get_size()
    scale = m/(h-(h*0.2))
    p = l
    change = 0
    screen.fill([255,255,255])
    crbox(screen, font, inarray, -1)
    while not check:
        temp = 0

        if p == 0:
            check = chorder(inarray)

        for i in range(0, p):
            if change == 1:
                screen.fill([255,255,255])
                crbox(screen, font, inarray, p)
                pygame.display.update()
                change = 0
            time.sleep(1/len(inarray))
            if i + 1 < p and inarray[i] > inarray[i+1]:
                temp = inarray[i]
                inarray[i] = inarray[i+1]
                inarray[i+1] = temp
                pygame.draw.rect(screen, [255,0,0], ((w/(l+2))*(i+1), h-(h*0.1), w/(l+2), -inarray[i+1]/scale), 0)
                pygame.draw.rect(screen, [0,0,0], ((w/(l+2))*(i+1), h-(h*0.1), w/(l+2), -inarray[i+1]/scale), 1)
                pygame.display.update();
                change = 1
            else:
                pygame.draw.rect(screen, [0,255,0], ((w/(l+2))*(i), h-(h*0.1), w/(l+2), -inarray[i]/scale), 0)
                pygame.draw.rect(screen, [0,0,0], ((w/(l+2))*(i), h-(h*0.1), w/(l+2), -inarray[i]/scale), 1)
                change = 1
        p -= 1

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    print("\n-----------------Completed Sorting!----------------\n")
    screen.fill([255,255,255])
    crbox(screen, font, inarray, -1)
    pygame.display.update()
def crbox(screen, font, inarray, p):
    l = len(inarray)
    m = max(inarray)
    w, h = pygame.display.get_surface().get_size()
    scale = m/(h-(h*0.2))
    for i, val in enumerate(inarray):
        if i == p:
            pygame.draw.rect(screen, [0,255,255], ((w/(l+2))*(i+1), h-(h*0.1), w/(l+2), -val/scale), 0)
            pygame.draw.rect(screen, [0,0,0], ((w/(l+2))*(i+1), h-(h*0.1), w/(l+2), -val/scale), 1)
        else:
            pygame.draw.rect(screen, [0,0,255], ((w/(l+2))*(i+1), h-(h*0.1), w/(l+2), -val/scale), 0)
            pygame.draw.rect(screen, [0,0,0], ((w/(l+2))*(i+1), h-(h*0.1), w/(l+2), -val/scale), 1)
        text = font.render(str(val), False, (0, 0, 0))
        screen.blit(text, ((w/(l+2))*(i+1), h-(h*0.075)))
def chorder(inarray):
    for i in range(0, len(inarray)-1):
        if (inarray[i] > inarray[i+1]):
            return False
    return True
if __name__ == "__main__":
    main()
