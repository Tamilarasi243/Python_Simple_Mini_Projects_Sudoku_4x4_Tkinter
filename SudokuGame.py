from colorama import init, Fore
import time

init()

List1 = [[0, 2, 4, 0], [1, 0, 3, 0], [0, 1, 2, 0], [2, 0, 1, 0]]
List2 = [[3, 2, 4, 1], [1, 4, 3, 2], [4, 1, 2, 3], [2, 3, 1, 4]]

print("-"*60)
print(Fore.RED+"'4x4 Sudoku'")
for i in List1:
    print(Fore.GREEN + str(i))
print(Fore.RESET+"-"*60)
row=1
start_time=time.time()
for i in range(len(List1)):
    print(Fore.CYAN + "Enter missing numbers from this row...","\nRow...",row,"...",Fore.GREEN+str(List1[i]))
    for j in range(len(List1[i])):
        if List1[i][j] == 0:
            miss = int(input(Fore.MAGENTA + "Enter missing number from 1 to 4 : "))
            while miss<1 or miss>4:
                print(Fore.RED+"Invalid input,Please enter number between 1 to 4...")
                miss = int(input(Fore.MAGENTA + "Enter missing number from 1 to 4 : "))
            if List2[i][j] == miss:
                List1[i][j] = miss
            else:
                print(Fore.RED + "Entered wrong number...")
                miss = int(input(Fore.LIGHTRED_EX + "Enter correct missing number: "))
                while True:
                    if List2[i][j] == miss:
                        List1[i][j] = miss
                        break
                    else:
                        print(Fore.RED + "Entered wrong number...")
                        miss = int(input(Fore.LIGHTRED_EX + "Enter correct missing number: "))
                        
    
    row+=1


    for k in List1:
        print(Fore.YELLOW+str(k))        

end_time=time.time()
total_time=int(end_time-start_time)

import pygame

pygame.init()
width=400
height=400
screen=pygame.display.set_mode((width,height))
black=screen.fill((0,0,0))
colo=(100,234,234)
white=(255,255,255)
font=pygame.font.SysFont(None,40)

pygame.display.set_caption("...4x4 SUDOKU...")

def blocks():
    blockSize=100
    for i in range(0,len(List1)):
        for j in range(0,len(List1[i])):
            a=j*blockSize
            b=i*blockSize
            rect=pygame.Rect(a,b,blockSize,blockSize)
            pygame.draw.rect(screen,colo,rect,1)
            text=font.render(str(List1[i][j]),True,colo)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

running =True
while running:
    blocks()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

pygame.quit()


print(Fore.RESET+"-"*60)
print(Fore.BLUE + "Final display:")
for i in List1:
    print(Fore.LIGHTBLACK_EX+ str(i))
print(Fore.RESET+"-"*60)


print(Fore.LIGHTYELLOW_EX+"Total time..."+Fore.LIGHTRED_EX+str(total_time)+Fore.LIGHTYELLOW_EX+"\nYour IQ Level is "+Fore.LIGHTRED_EX+str(100-total_time))
print(Fore.RESET+"-"*60)
