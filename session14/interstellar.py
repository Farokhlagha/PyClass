# pip install arcade
import random
import arcade
from spaceship import Spaceship
from enemy import Enemy                        


# in site python arcde, API,Built-in resources, find pic for background
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=800, title='Interstellar')
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(':resources:images/backgrounds/stars.png')
        self.me = Spaceship(self.width, 'Farokhlagha')
        self.enemy_list = []


    # display
    def on_draw(self):
        arcade.start_render()
        #arcade.draw_lrtb_rectangle_filled(0, self.width, self.height, self.height * (1 / 3), arcade.color.SKY_BLUE)
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw() 
        for enemy in self.enemy_list:
            enemy.draw()

        for bullet in self.me.bullet_list:
            bullet.draw()

        

    def on_key_press(self, symbol: int, modifiers: int):  
        if symbol == arcade.key.A or symbol == arcade.key.LEFT: 
            self.me.change_x =-1
        elif symbol == arcade.key.D or symbol == arcade.key.RIGHT: # right side
            self.me.change_x =1

        elif symbol == arcade.key.DOWN:
            self.me.center_x = 0
             
        elif symbol == arcade.key.SPACE:
            self.me.fire()

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.center_x = 0


    def on_update(self, delta_time: float):
        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.me, enemy):
                print('Game over ❌')
                exit(0)

        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                self.arcade.check_for_collision(enemy, bullet)
                self.me.bullet_list.remove(bullet)
                self.enemy_list.remove(enemy)

        self.me.move()

        for enemy in self.enemy_list:
            enemy.move()

        for bullet in self.me.bullet_list:
            bullet.move()

        for enemy in self.enemy_list:
            if enemy.center_y < 0:
                self.enemy_list.remove(enemy)
        
        if random.randint(1, 100) == 6:
            self.new_enemy = Enemy(self.width, self.height)
            self.enemy_list.append(self.new_enemy)


window = Game()
arcade.run() #for not close the widow

        