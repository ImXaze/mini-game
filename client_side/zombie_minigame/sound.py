def play_sound(ply, station):
    sound_url = "https://synergyroleplay.com/stream/115.mp3"
    sound_mode = "mono"

    def callback(station):
        if IsValid(station):
            station.SetPos(ply.GetPos())
            station.Play()

    sound.PlayURL(sound_url, sound_mode, callback)