from mutagen.mp3 import MP3
import datetime
import random
from tabulate import tabulate
import json
from mutagen.easyid3 import EasyID3
from os import listdir
from datetime import timedelta


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
        self.song = ''

    def add_song(self, song):
        if song in self.list_of_songs:
            print("Song already there")
        else:
            self.list_of_songs.append(song)
        print(self.list_of_songs)

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

    def next_song(self, repeat=False, shuffle=True):
        if repeat is True:
            for self.index in range(len(self.list_of_songs)):
                self.song = self.list_of_songs[self.index]
                if self.index is len(self.list_of_songs):
                    self.index = 0
                    continue
                self.index += 1
                print(self.song)

        elif shuffle is True:
            for element in range(len(self.list_of_songs)):
                self.song = random.choice(self.list_of_songs)
                self.list_of_songs.remove(self.song)
                print(self.song)
        else:
            return False

    def pprint_playlist(self):
        headers_name = ["Artist", "Song", "Length"]
        table = []
        for song in self.songs:
            table.append([song.artist, song.title, song.length])
        print(tabulate(table, headers=headers_name))

    def save(self):
        print(self.list_of_songs)
        self.dict_songs = {
            "name": self.name,
            "songs": [song for song in self.list_of_songs]
        }
        with open(self.name + ".json", "w") as f:
            f.write(json.dumps(self.dict_songs, f, indent=True))

    def load(self):
        with open(self.name + '.json', 'r') as f:
            content = json.load(f)
        return content

class Crawler:

    def __init__(self, path):
        self.path = path
        self.mp3_path = []

    def get_playlist(self):
        for element in listdir(self.path):
            if element.endswith(".mp3"):
                self.mp3_path.append(listdir(self.path)[element])
        playlist = Playlist(name="Music_playlist")
        for item in self.mp3_path:
            audio = MP3(self.path + item, ID3=EasyID3)
            artist = audio["artist"][0]
            album = audio["album"][0]
            title = audio["title"][0]
            length = str(timedelta(seconds=int(audio.info.length)))
            song = Song(title, artist, album, length)
            song.name = item
            playlist.add_song(song)
        return playlist



def main():
    s = Song("Odin", "Manowar", "The Sons of Odin", "03:44")
    m = Song("Odin", "Manovar", "The Sons of Odin2", "03:02")

    print (s.get_length(minutes=True))
    print(s.get_length(seconds=True))
    print(s.get_length(hours=False))

    code_songs = Playlist(name="Code")
    print(code_songs.add_song(s))
    print(code_songs.add_song(m))
    code_songs.total_length()
    code_songs.artists()
    code_songs.next_song()
    code_songs.save()
    code_songs.load()
    path = "/home/maria/Desktop/Week4"
    crawler = Crawler(path)
    crawler.get_playlist()


if __name__ == '__main__':
    main()
