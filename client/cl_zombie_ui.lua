local ply = LocalPlayer()

local function createUI()
    local gameScreen = vgui.Create("DFrame")
    gameScreen:SetSize(ScrW(), ScrH())
    gameScreen:SetTitle("")
    gameScreen:ShowCloseButton(false)
    gameScreen:MakePopup()
    gameScreen.Paint = function(self, w, h)
        draw.RoundedBox(0, 0, 0, w, h, Color(0, 0, 0, 255))
    end

    local exitButton = vgui.Create("DButton", gameScreen)
    exitButton:SetSize(100, 50)
    exitButton:SetPos(ScrW() - 110, 10)
    exitButton:SetText("Exit")
    exitButton.DoClick = function()
        gameScreen:Close()
    end
end

concommand.Add("start_zombie_minigame", function()
    if IsValid(ply) then
        createUI()
    end
end)