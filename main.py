import vlc

# Create an instance of the VLC player
instance = vlc.Instance("--no-xlib")
player = instance.media_player_new()

# Set the video as the media to play
media = instance.media_new("yaai.mp4")
player.set_media(media)

# Set the video to loop
player.set_fullscreen(True)
player.play()

# Run the event loop
while True:
    pass
