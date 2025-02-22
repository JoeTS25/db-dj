"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name")
    description = StringField("Playlist Description")


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song Title")
    artist = StringField("Song Artist")


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
