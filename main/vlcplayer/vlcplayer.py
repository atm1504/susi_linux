""" VLC Player module """

import vlc
import time


class VlcPlayer():
    def __init__(self):
        self.instance = vlc.Instance("--no-video")
        self.player = self.instance.media_player_new()
        self.list_player =  self.instance.media_list_player_new()
        self.list_player.set_media_player(self.player)

    def play(self, mrl):
        media = self.instance.media_new(mrl)
        media_list = self.instance.media_list_new([mrl])
        self.player.set_media(media)
        self.list_player.set_media_list(media_list)
        self.list_player.play()

    def pause(self):
        self.list_player.pause()

    def resume(self):
        self.list_player.resume()

    def stop(self):
        self.list_player.stop()

    def wait_till_end(self):
        playing = set([vlc.State.Playing, vlc.State.Buffering])
        time_left = True
        while time_left == True:
            pstate = self.list_player.get_state()
            if pstate not in playing:
                time_left = False
            print("Sleeping for audio output")
            time.sleep(1)

    def say(self,mrl):
        # this is tricky!!!
        if self.list_player.is_playing():
            self.list_player.pause()
        # TODO wait for the length of what is said, then restart main player!
        


