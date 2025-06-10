import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#背景画像のSurface
    bg2_img = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_state = [0,0]
        key_lst = pg.key.get_pressed()#キーの押下状態を取得
        if key_lst[pg.K_UP]:
            key_state[1] -= 1
        if key_lst[pg.K_DOWN]:
            key_state[1] += 1
        if key_lst[pg.K_LEFT]:
            key_state[0] -= 1
        if key_lst[pg.K_RIGHT]:
            key_state[0] += 2
        if key_lst[pg.KEYDOWN] != True :
            key_state[0] -= 1
        print(key_state)
        kk_rct.move_ip(key_state)
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg2_img, [-x+1600,0])
        screen.blit(bg_img, [-x+3200, 0])
        #screen.blit(kk_img, [300, 200])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()