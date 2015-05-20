from music_library import Song, Playlist, Crawler
import unittest


class TestMusicLibrary(unittest.TestCase):

    def setUp(self):
        self.info = Song("Pink", "Perfect", "Perfect", "3:44")


    def test_init(self):
        self.assertEqual(self.info.artist, "Pink")
        self.assertEqual(self.info.title, "Perfect")
        self.assertEqual(self.info.album, "Perfect")
        self.assertEqual(self.info.length, "3:44")

    def test_str(self):
        result = "Pink - Perfect from Perfect - 3:44"
        self.assertEqual(str(self.info), result)

    def test_eq(self):
        s = Song("Odin", "Manowar", "The Sons of Odin", "3:44")
        self.assertTrue(self.info == self.info)
        self.assertFalse(self.info == s)

    def test_hash(self):
        result = self.info.__hash__()
        self.assertTrue(isinstance(result, int))

    def test_get_length(self):
        self.assertEqual(self.info.get_length(seconds=True), 224)
        self.assertEqual(self.info.get_length(minutes=True), 3)
        self.assertEqual(self.info.get_length(hours=True), 0)


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.code_songs = Playlist("Code", True, True)
        self.info = Song("Pink", "Perfect", "Perfect", "3:44")

    def test_init(self):
        self.assertEqual(self.code_songs.name, "Code")
        self.assertEqual(self.code_songs.repeat, True)
        self.assertEqual(self.code_songs.shuffle, True)
        self.assertEqual(self.code_songs.list_of_songs, [])
        self.assertEqual(self.code_songs.index, 0)
        self.assertEqual(self.code_songs.song, '')

    def test_add_song(self):
        self.code_songs.add_song(self.info)
        self.assertTrue(self.info in self.code_songs.list_of_songs)

    def test_remove_song(self):
        self.code_songs.add_song(self.info)
        self.code_songs.remove_song(self.info)
        self.assertFalse(self.info in self.code_songs.list_of_songs)

class TestCrawler(unittest.TestCase):

    def setUp(self):
        self.path = "/home/maria/Desktop/Week4"
        self.crawler = Crawler(self.path)


    def test_init(self):
        self.assertEqual(self.crawler.path, self.path)
        self.assertEqual(self.crawler.mp3_path, [])


if __name__ == '__main__':
    unittest.main()
