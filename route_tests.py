from unittest import TestCase
from app import app
from models import db, Playlist, Song, PlaylistSong


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app_test'
app.config['SQLALCHEMY_ECHO'] = False


app.config['TESTING'] = True

db.drop_all()
db.create_all()

class PlaylistTestCase(TestCase):
    """Tests playlist views"""
    def setUp(self):
        """Make test data"""
        Playlist.query.delete()
        db.session.commit()

        playlist = Playlist(name='My Playlist', description='Test description')
        db.session.add(playlist)
        db.session.commit()

        self.playlist_id = playlist.id 

    def tearDown(self):
        """Clean up any leftover transactions"""
        db.session.rollback()

    def test_all_playlists(self):
        with app.test_client() as client:
            resp = client.get("/playlists")
            self.assertEqual(resp.status_code, 200)

    def test_single_playlist(self):
        with app.test_client() as client:
            resp = client.get(f"/playlists/{self.playlist_id}")
            self.assertEqual(resp.status_code, 200)

            self.assertEqual(
                resp.json,
                {'playlist': {
                    'id': self.playlist_id,
                    'name': 'Test Playlist',
                    'description': 'Test Description'
                }})
    
    def test_create_playlist(self):
        with app.test_client() as client:
            resp client.post(
                "/playlists", json={
                    "name": "Test Playlist 2",
                    "description": "Test Description 2"
                })
            self.assertEqual(resp.status_code, 201)

            self.assertIsInstance(resp.jspon['playlist'] ['id', int])
            del resp.json['playlist']['id']

            self.assertEqual(
                resp.json{"playlist": {'name': 'Test Playlist 2', 'description': 'Test Descripiton 2'}})

            self.assertEqual(Playlist.query.count(), 2)

class SongTestCase(TestCase):
    """Tests song views"""
    def setUp(self):
        """Make test data"""
        Song.query.delete()
        db.session.commit()

        song = Song(title='Test Song', artist='Test Artist')
        db.session.add(song)
        db.session.commit()

        self.song_id = song.id 

    def tearDown(self):
        """Clean up any leftover transactions"""
        db.session.rollback()

    def test_all_playlists(self):
        with app.test_client() as client:
            resp = client.get("/songs")
            self.assertEqual(resp.status_code, 200)

    def test_single_playlist(self):
        with app.test_client() as client:
            resp = client.get(f"/songs/{self.song_id}")
            self.assertEqual(resp.status_code, 200)

            self.assertEqual(
                resp.json,
                {'song': {
                    'id': self.song_id,
                    'title': 'Test Song',
                    'artist': 'Test Artist'
                }})
    
    def test_add_song(self):
        with app.test_client() as client:
            resp client.post(
                "/songs", json={
                    "title": "Test Song 2",
                    "aritist": "Test Artist 2"
                })
            self.assertEqual(resp.status_code, 201)

            self.assertIsInstance(resp.jspon['song'] ['id', int])
            del resp.json['song']['id']

            self.assertEqual(
                resp.json{"song": {'title': 'Test Playlist 2', 'artist': 'Test Descripiton 2'}})

            self.assertEqual(Song.query.count(), 2)


        

                



