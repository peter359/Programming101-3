import datetime
import random
import time
from tabulate import tabulate
import json


class Song:
    def __init__(self, title, artist, album, length):
        self.title = str(title)
        self.artist = str(artist)
        self.album = str(album)
        self.__length = str(length)

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length())

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist

    def __hash__(self):
        return hash(self.title + self.artist)

    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict if not key.startswith("_")}

    def length(self, seconds=False, minutes=False, hours=False):
        times = self.__length.split(":")
        i = 1
        result = 0
        if seconds:
            while i <= len(times):
                result += int(times[len(times) - i]) * 60 ** (i - 1)
                i += 1
            return result
        elif minutes:
            del times[len(times) - 1:]
            while i <= len(times):
                result += int(times[len(times) - i]) * 60 ** (i - 1)
                i += 1
            return result
        elif hours:
            del times[len(times) - 2:]
            while i <= len(times):
                result += int(times[len(times) - i]) * 60 ** (i - 1)
                i += 1
            return result
        return self.__length


class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = []
        self.__current_song_index = 0
        self.__played_songs = set()

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        try:
            self.songs.remove(song)
        except ValueError:
            pass

    def add_songs(self, songs):
        self.songs += songs

    def total_length(self):
        total_seconds = sum([song.get_length(seconds=True) for song in self.songs])
        return str(datetime.timedelta(seconds=total_seconds))

    def artists(self):
        return {self.songs[Song.artist]: self.songs.count(artist) for artist in self.songs}

    def __has_next_song(self):
        return self.__current_song_index < len(self.songs)

    def __shuffle(self):
        song = random.choice(self.songs)

        while song in self.__played_songs:
            song = random.choice(self.songs)

        self.__played_songs.add(song)

        if len(self.__played_songs) == len(self.songs):
            self.__played_songs = set()

        return song

    def next_song(self):
        if self.repeat == "SONG":
            return self.songs[self.__current_song_index]

        if self.shuffle:
            return self.__shuffle()

        if not self.__has_next_song() and self.repeat == "NONE":
            raise Exception("End of playlist")

        if not self.__has_next_song() and self.repeat == "PLAYLIST":
            self.__current_song_index = 0

        song = self.songs[self.__current_song_index]
        self.__current_song_index += 1

        return song

    def pprint_playlist(self):
        headers = ["Artist", "Song", "Length"]
        table = []

        for song in self.songs:
            table.append([song.artist, song.title, song.length()])

        print(tabulate(table, headers=headers))

    def prepare_json(self):
        data = {
            "name": self.__name,
            "songs": [song.prepare_json() for song in self.songs]
        }

        return data

    def save(self, indent=True):
        filename = self.__name.replace(" ", "-") + ".json"

        with open(filename, "w") as f:
            f.write(json.dumps(self.prepare_json(), indent=indent))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            contents = f.read()
            data = json.loads(contents)
            p = Playlist(data["name"])

            for dict_song in data["songs"]:
                song = Song(artist=dict_song["artist"], title=dict_song["title"], album=dict_song["album"], length=dict_song["length"])
                p.add_song(song)

            return p
