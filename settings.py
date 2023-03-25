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

    def speed_up(self):
        self.block_speed *= self.speedup_scale
