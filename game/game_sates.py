class GameStates():
    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        self.reset_states()
        self.game_active=False
    def reset_states(self):
        self.ship_left=self.ai_settings.ship_limit