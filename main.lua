local ws = WebSocket
local asdasd = ws.connect("ws://127.0.0.1:3000")
local TextChatService = game:GetService("TextChatService")
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

print("Connected to the websocket :3")

asdasd.OnMessage:Connect(function(msg)
    local textToSay = string.match(msg, "^say%s+(.*)")
    if textToSay then
        print("Detected text:", textToSay)
        local localPlayer = Players.LocalPlayer

        if TextChatService.ChatVersion == Enum.ChatVersion.LegacyChatService then
        ReplicatedStorage.DefaultChatSystemChatEvents.SayMessageRequest:FireServer(textToSay, "All")
        else
        local channels = TextChatService.TextChannels
        local general = channels.RBXGeneral

        general:SendAsync(textToSay)
    end
        end

    if msg == "kill" then
        game.Players.LocalPlayer.Character.Humanoid.Health = 0
        print("killed :3")
    end

    if msg == "rejoin" then
        local ts = game:GetService("TeleportService")
        local p = game:GetService("Players").LocalPlayer
        ts:Teleport(game.PlaceId, p)
        print("Rejoining :3")
    end
end)
