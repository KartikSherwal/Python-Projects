import pygame.font
from pygame.sprite import Group
from ship import Ship
class Scoreboard:
    def __init__(self,ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.dimensions
        self.stats = ai_game.stats
       #Text and font color and size
        self.text_color = (0,0,250)
        self.level_color = (250,0,0)
        self.font = pygame.font.SysFont(None,48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "Score:{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 20
    
    def prep_high_score(self):
        high_score = round(self.stats.high_score,-1)
        high_score_str = "High Score: {:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str,True,self.text_color,self.settings.bg
        )
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(
            self.level_image,self.level_rect
        )
        self.ships.draw(self.screen)
    
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def prep_level(self):
        level_str = "Level: "+ str(self.stats.level)
        #Mission Completed respect👆✌🤘✌✌🤘😎😎🤘
        self.level_image = self.font.render(level_str,True,self.level_color, self.settings.bg)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)