from pygame import *
perso = image.load('sonic.png')

scr = display.set_mode((500,500))

class Luffy:
    image = dict([(direction,[perso.subsurface(x,y,44,62)for x in range(0,200,44)]) for direction,y in zip((K_s,K_a,K_d,K_w),range(0,200,62))])
    x,y = 202,202

direction = K_s
index_img = 0

scr.blit(Luffy.image[direction][index_img],(202,202))
display.flip()

while True:
    ev = event.poll()
    if ev.type == QUIT: break
    k = key.get_pressed()
    for i in (K_s,K_a,K_d,K_w):
        if k[i]:
            direction = i if direction != i else direction
            index_img = (index_img+1)%4
            Luffy.x += (-k[K_a]+k[K_d])*8
            Luffy.y += (-k[K_w]+k[K_s])*8
            break
    else: index_img = 0
    scr.fill(0)
    scr.blit(Luffy.image[direction][index_img],(Luffy.x,Luffy.y))
    display.flip()
    time.wait(50)

quit()