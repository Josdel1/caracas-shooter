from random import randint
from ezsgame.all import *

screen = Screen(show_fps=True, title="Space Invaders")

player = Rect(pos=["center", 380], size=[20,20], screen=screen)
player_controller = Controller(screen, keys=["left", "right"], speed=[-5,5])

enemy = Rect(pos=["center", 10], size=[20,20], screen=screen, color="Red")
enemy_controller = Controller(screen, keys=["a", "d"], speed=[-5,5])

health = 100
health_text = Text(text=str(health), pos= ["left", "top"], fontsize= 24, color="Green")

e_health = 100
e_health_text = Text(text=str(e_health), pos= ["right", "top"], fontsize= 24, color="Red")

player_bullets = []
enemy_bullets = []

@screen.add_interval(time=650, name="player bullets")
def shoot():
    player_bullets.append(Rect(pos=[player.pos[0] + player.size[0]/2, player.pos[1]], size=[10,10], screen=screen))

@screen.add_interval(time=650, name="enemy bullets")
def enemy_shoot():
    enemy_bullets.append(Rect(pos=[enemy.pos[0] + enemy.size[0]/2, enemy.pos[1]], size=[10,10], screen=screen, color="Red"))

gradient = Gradient(screen, start="black", end="gray", direction="vertical", complexity=50)

while True:
    screen.check_events()
    screen.fill(gradient)
    
    health_text.draw(screen)
    e_health_text.draw(screen)

    player.draw(screen)
    player.move(x = sum(player_controller.get_speed()))

    enemy.draw(screen)
    enemy.move(x = sum(enemy_controller.get_speed()))
    
    # Shoot the bullets.

    for bullet in player_bullets:
        bullet.move(y=7)
        bullet.draw()

        if bullet.is_colliding(enemy, screen):
            if e_health == 0:
                quit()
            else:
                e_health -= 1
                e_health_text.text = str(e_health)

    for e_bullet in enemy_bullets:
        e_bullet.move(y=-7)
        e_bullet.draw()

        if e_bullet.is_colliding(player, screen):
            if health == 0:
                quit()
            else:
                health -= 1
                health_text.text = str(health)
            

    screen.update()
    