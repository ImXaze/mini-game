import pygame
from ui import UI
from controls import Controls
from game_logic import GameLogic
from player_model import PlayerModel
from sound import Sound
from exit_button import ExitButton
from bug_checker import BugChecker
from exploit_prevention import ExploitPrevention

class Main:
    def __init__(self):
        pygame.init()
        self.ply = PlayerModel("models/player/zombie_fast.mdl")
        self.station = Sound("https://synergyroleplay.com/stream/115.mp3", "mono")
        self.ui = UI(self.ply, self.station)
        self.controls = Controls(self.ply, self.station)
        self.game_logic = GameLogic(self.ply, self.station)
        self.exit_button = ExitButton(self.ui)
        self.bug_checker = BugChecker(self.ply, self.station)
        self.exploit_prevention = ExploitPrevention(self.ply, self.station)

    def run(self):
        while True:
            self.controls.handle_input()
            self.game_logic.update()
            self.ui.draw()
            self.bug_checker.check()
            self.exploit_prevention.prevent()
            if self.exit_button.is_clicked():
                break

if __name__ == "__main__":
    main = Main()
    main.run()