import time
from game_logic import ply, IsValid
from player_model import SetPos, GetPos
from main import LocalPlayer

def check_for_bugs():
    while True:
        # Check if player object is valid
        if not IsValid(ply):
            print("Error: Player object is not valid.")
            break

        # Check if player position is valid
        player_pos = GetPos(LocalPlayer())
        if not IsValid(player_pos):
            print("Error: Player position is not valid.")
            break

        # Check if player model is set correctly
        if ply.GetModel() != "models/player/zombie_fast.mdl":
            print("Error: Player model is not set correctly.")
            break

        # Sleep for a while before next check
        time.sleep(1)

if __name__ == "__main__":
    check_for_bugs()