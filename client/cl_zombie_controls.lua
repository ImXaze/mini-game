-- client/cl_zombie_controls.lua

local ply = LocalPlayer()

-- Function to handle player controls
function HandlePlayerControls()
    if input.IsKeyDown(KEY_W) then
        ply:SetVelocity(Vector(0, 0, 100)) -- Move player forward
    elseif input.IsKeyDown(KEY_S) then
        ply:SetVelocity(Vector(0, 0, -100)) -- Move player backward
    elseif input.IsKeyDown(KEY_A) then
        ply:SetVelocity(Vector(-100, 0, 0)) -- Move player left
    elseif input.IsKeyDown(KEY_D) then
        ply:SetVelocity(Vector(100, 0, 0)) -- Move player right
    end
end

-- Function to handle game controls
function HandleGameControls()
    if input.IsKeyDown(KEY_ESCAPE) then
        RunConsoleCommand("exit") -- Exit the game
    end
end

-- Function to handle zombie controls
function HandleZombieControls()
    if input.IsKeyDown(KEY_SPACE) then
        ply:SetModel("models/player/zombie_fast.mdl") -- Change player model to zombie
        sound.PlayURL("https://synergyroleplay.com/stream/115.mp3", "mono", function(station)
            if IsValid(station) then
                station:SetPos(ply:GetPos())
                station:Play()
            end
        end)
    end
end

-- Hook the functions to the appropriate events
hook.Add("Think", "PlayerControls", HandlePlayerControls)
hook.Add("Think", "GameControls", HandleGameControls)
hook.Add("Think", "ZombieControls", HandleZombieControls)