from mutagen.mp3 import MP3
import datetime
import random


class Song:

    def __init__(self, artist, title, album, length):
        self.artist = artist
        self.title = title
        self.album = album
        self.length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def _eq__(self, other):
        equal_artists = self.artist == other.artist
        equal_titles = self.title == other.title
        equal_albums = self.album == other.album
        equal_lengths = self.length == other.length
        return equal_artists and equal_titles and equal_albums and equal_lengths

    def __hash__(self):
        return hash(self.artist + self.title + self.album + self.length)

    def get_length(self, seconds=False, minutes=False, hours=False):
        parts = self.length.split(":")
        if seconds is False and minutes is False and hours is False:
            return self.length
        if seconds is True:
            if len(parts) > 2:
                return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
            elif len(parts) == 2:
                return int(parts[0]) * 60 + int(parts[1])
            elif len(parts) == 1:
                return int(parts[0])
        elif minutes is True:
            if len(parts) > 2:
                return int(parts[0]) * 60 + int(parts[1])
            elif len(parts) == 2:
                return int(parts[0])
            else:
                return 0
        elif hours is True:
            if len(parts) > 2:
                return int(parts[0])
            else:
                return 0


class Playlist:

    def __init__(self, name="Code", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.list_of_songs = []
        self.index = 0

    def add_song(self, song):
        if song in self.list_of_songs:
            print("Song already there")
        else:
            self.list_of_songs.append(song)

    def remove_song(self, song):
        if song in self.list_of_songs:
            self.list_of_songs.remove(song)
        else:
            raise ValueError

    def add_songs(self, songs):
        for song in songs:
            if song in self.list_of_songs:
                songs.remove(song)
        self.list_of_songs.append(songs)

    def total_length(self):
        sum_length = 0
        for element in self.list_of_songs:
            sum_length += element.get_length(seconds=True)
        print(str(datetime.timedelta(seconds=sum_length)))

    def artists(self):
        dict_histogram = {}
        i = 0
        for song in self.list_of_songs:
            if song.artist in dict_histogram:
                dict_histogram[song.artist] += 1
            else:
                dict_histogram[song.artist] = 1
        print (dict_histogram)

    #ne vrushta pesen??
    def next_song(self, repeat=False, shuffle=False):
        if self.repeat is True:
            if self.index == len(self.list_of_songs):
                self.index == 0
            self.song = self.list_of_songs[self.index]
            self.index += 1
            return self.song

        elif self.shuffle is True:
            for element in self.list_of_songs:
                self.song = random.choice(self.list_of_songs)
                self.list_of_songs.remove(self.song)
                return self.song

    # def pprint_playlist():



def main():
    s = Song("Odin", "Manowar", "The Sons of Odin", "03:44")
    m = Song("Odin", "Manovar", "The Sons of Odin2", "03:02")

    print (s.get_length(minutes=True))
    print(s.get_length(seconds=True))
    print(s.get_length(hours=False))

    code_songs = Playlist(name="Code")
    code_songs.add_song(s)
    code_songs.add_song(m)
    code_songs.total_length()
    code_songs.artists()
    code_songs.next_song(repeat=True)


if __name__ == '__main__':
    main()
