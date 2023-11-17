### Describe Problem


# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them


### Design Class Interface

class Playlist():
   def __init__(self):
       self.songs = []

   def add_track(self, track):
        self.songs.append(track)

   def show_tracks(self):
        if not self.songs:
            return "Playlist empty"
        return "\n".join(self.songs)

my_songs = Playlist()

print(my_songs.show_tracks())