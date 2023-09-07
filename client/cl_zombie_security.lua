-- client/cl_zombie_security.lua

local function exploitCheck()
    -- Check if player is in a valid state
    if not IsValid(ply) then
        return false, "Invalid player state"
    end

    -- Check if player is in the game screen
    if not vgui.IsOnPanel(ply, gameScreen) then
        return false, "Player not in game screen"
    end

    -- Check if player model is correct
    if ply:GetModel() ~= "models/player/zombie_fast.mdl" then
        return false, "Incorrect player model"
    end

    return true
end

-- Continually check for exploits
timer.Create("ExploitCheckTimer", 1, 0, function()
    local isValid, errorMsg = exploitCheck()
    if not isValid then
        debugger(errorMsg)
    end
end)