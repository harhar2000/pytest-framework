from lib.music_list import Playlist

def test_empty_list_returns_empty():
    playlist = Playlist()
    result = playlist.show_tracks()
    assert result == "Playlist empty"
    

def test_list_of_one_returns_one():
    playlist = Playlist()
    playlist.add_track("Song 1")
    result = playlist.show_tracks()
    assert result == "Song 1"

def test_list_of_three_returns_three():
    playlist = Playlist()
    playlist.add_track("Song 1")
    playlist.add_track("Song 2")
    playlist.add_track("Song 3")
    result = playlist.show_tracks()
    assert result == "Song 1\nSong 2\nSong 3"





