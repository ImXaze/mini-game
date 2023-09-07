local ply = LocalPlayer()

local function StartZombieMinigame()
    ply:SetModel("models/player/zombie_fast.mdl")
    sound.PlayURL("https://synergyroleplay.com/stream/115.mp3", "mono", function(station)
        if IsValid(station) then
            station:SetPos(ply:GetPos())
            station:Play()
        end
    end)
end

concommand.Add("start_zombie_minigame", StartZombieMinigame)

local function StopZombieMinigame()
    ply:SetModel("models/player/normal.mdl")
    sound.StopAll()
end

concommand.Add("stop_zombie_minigame", StopZombieMinigame)

hook.Add("Think", "ZombieMinigameThink", function()
    if ply:GetModel() == "models/player/zombie_fast.mdl" then
        include("cl_zombie_controls.lua")
        include("cl_zombie_ui.lua")
    end
end)