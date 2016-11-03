import webbrowser
from time import ctime

class Video():
	""" Video is the parent class for the TvShow and Movie class. Dont touch this class, use it for inheritance. """
	def __init__(self, title, storyline, poster, trailer):
		""" Object type Video initiated at """ 
		print (Video.__init__.__doc__ + ctime())
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
	""" TvShow is a class for defining a TvShow. To instantiate this class, pass the following arguments in order:
	title, storyline, poster, trailer, season. You can call the gettype() method on the instance to get the type of the object
	and you can call the show_trailer() function to show a clip from the show. """
	def __init__(self, title, storyline, poster, trailer, season):
		""" Object type TvShow initiated at """
		print (TvShow.__init__.__doc__ + ctime())
		Video.__init__(self, title, storyline, poster, trailer)
		self.kind = 'TV'
		self.season = season

	def gettype(self):
		return self.kind

class Movie(Video):
	""" Movie is a class for defining a Movie. To instantiate this class, pass the following arguments in order:
	title, storyline, poster, trailer, duration. You can call the gettype() function to get the type of the object
	and you can call the show_trailer() function to show the movies trailer."""
	def __init__(self, title, storyline, poster, trailer, duration):
		""" Object type Movie initiated at """
		print (Movie.__init__.__doc__ + ctime())
		Video.__init__(self, title, storyline, poster, trailer)
		self.kind = 'Movie'
		self.duration = duration

	def gettype(self):
		return self.kind
		

	