import sys
from time import sleep
import pygame
from Dimensons import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from Bullets import bullet
from aliens import Alien
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.dimensions = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.dimensions.screen_width = self.screen.get_rect().width
        self.dimensions.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invadors")
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "Play")
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
                
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        self._check_bullet_alien_collision()
    
    def _check_bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.dimensions.alien_score * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.dimensions.increase_speed()
            self.stats.level+=1
            self.sb.prep_level()

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                #Controling the events of the ship based on the key pressed by the user
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                #Quiting the game by esc or q.
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                #Moving right
                   if event.key == pygame.K_RIGHT:
                       self.ship.moving_right = False
                       #Moving left
                   elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False 
    def _check_play_button(self,mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos) 
        if button_clicked and not self.stats.game_active:
             self.dimensions.initialize_dynamic_settings()
             self.stats.reset_stats()
             self.stats.game_active = True
             self.sb.prep_score()
             self.sb.prep_level()
             self.sb.prep_ships()
             self.aliens.empty()
             self.bullets.empty()
             self._create_fleet()
             self.ship.center_ship()
             pygame.mouse.set_visible(False)
    def _fire_bullet(self):
        if len(self.bullets) < self.dimensions.bullets_allowed:
            new_bullet = bullet(self)
            self.bullets.add(new_bullet)
                           
    def _update_screen(self):
        self.screen.fill(self.dimensions.bg)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_image()
        pygame.display.flip()

    def _create_fleet(self):
        alien = Alien(self)
        """About fleet"""
        alien_width,alien_height = alien.rect.size
        available_space_x = self.dimensions.screen_width -  (1 * alien_width)
        number_aliens_x = available_space_x //   (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.dimensions.screen_height - (1 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.dimensions.fleet_drop_speed
        self.dimensions.fleet_direction *= -1
        #Mission passed respect😎😎👆👆✌🤘
        #Very happy 😋😆😋🎂
    def _create_alien(self, alien_number,row_number):
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size 
            alien.x = alien_width + 2* alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 3 * alien.rect.height * row_number
            self.aliens.add(alien)
                                            
if __name__ == '__main__':
     ai = AlienInvasion()
     ai.run_game()
