-- client/cl_zombie_debugger.lua

local function debugger()
    local ply = LocalPlayer()
    if not IsValid(ply) then
        print("Player object is not valid.")
        return
    end

    if not ply:GetModel() == "models/player/zombie_fast.mdl" then
        print("Player model is not set to zombie.")
        return
    end

    if not ply:Alive() then
        print("Player is not alive.")
        return
    end

    print("No issues found.")
end

local function exploitCheck()
    local ply = LocalPlayer()
    if ply:GetMoveType() ~= MOVETYPE_WALK and ply:GetMoveType() ~= MOVETYPE_NOCLIP then
        print("Potential exploit detected: abnormal player movement.")
        return
    end

    if ply:GetPos():Distance(gameScreen:GetPos()) > 1000 then
        print("Potential exploit detected: player is too far from the game screen.")
        return
    end

    print("No exploits detected.")
end

concommand.Add("debug", debugger)
concommand.Add("exploitCheck", exploitCheck)