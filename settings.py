class Settings:
    """'Aaaa... things are set here' - Marc Peña"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.gravity = 0.5
        self.block_speed = 1.0

        # Fa més difícil el joc a mesura que passa el temps
        self.speedup_scale = 1.1

        self.background_color = (143, 21, 100)

        self.initialize_player_settings()

    def initialize_player_settings(self):
        self.vertical_speed = 1.0
        self.horizontal_speed = 10.0

        self.player_color = (0, 0, 255)


    def speed_up(self):
        self.block_speed *= self.speedup_scale
