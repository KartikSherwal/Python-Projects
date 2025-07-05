class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg = (0,0,0)
        self.ship_limit = 3
        #Bullets
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250,0,0)
        self.bullets_allowed = 4
        #Alien and It's FLEET
        
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        #self.width_change = 1.5
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
         self.ship_speed = 1.7
         self.bullet_speed = 1.7
         self.fleet_direction = 1
         self.alien_speed = 0.3
         self.alien_score = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_score = int(self.alien_score * self.score_scale)
        #self.bullet_width = int(self.bullet_width * self.width_change)
        

       