def set_player_model(ply):
    if IsValid(ply):
        ply:SetModel("models/player/zombie_fast.mdl")
        ply:SetPos(LocalPlayer():GetPos())

def get_player_position(ply):
    if IsValid(ply):
        return ply:GetPos()

def update_player_position(ply, new_pos):
    if IsValid(ply):
        ply:SetPos(new_pos)