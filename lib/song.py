class Song:
      count = 0
      genres = []
      artists = []
      genre_count = {}
      artist_count = {}

      def __init__(self, name, artist, genre):
        # Initialize instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment count for each new song created
        Song.add_song_to_count()

        # Add the genre to the genres list
        Song.add_to_genres(self.genre)

        # Add the artist to the artists list
        Song.add_to_artists(self.artist)

        # Update the genre count
        Song.add_to_genre_count(self.genre)

        # Update the artist count
        Song.add_to_artist_count(self.artist)

      @classmethod
      def add_song_to_count(cls):
        """Increments the song count."""
        cls.count += 1

      @classmethod
      def add_to_genres(cls, genre):
        """Adds genre to genres list, ensuring no duplicates."""
        if genre not in cls.genres:
            cls.genres.append(genre)

      @classmethod
      def add_to_artists(cls, artist):
        """Adds artist to artists list, ensuring no duplicates."""
        if artist not in cls.artists:
            cls.artists.append(artist)

      @classmethod
      def add_to_genre_count(cls, genre):
        """Increments the count of the given genre in genre_count."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

      @classmethod
      def add_to_artist_count(cls, artist):
        """Increments the count of the given artist in artist_count."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
      pass
