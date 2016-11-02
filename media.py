import webbrowser

class Video():

	def __init__(self, title, storyline, poster, trailer):
		print "Video constructor called"
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
	
	def __init__(self, title, storyline, poster, trailer, season):
		self.kind = 'TV'
		print "Video constructor called"
		Video.__init__(self, title, storyline, poster, trailer)
		self.season = season

	def gettype(self):
		return self.kind

class Movie(Video):
	
	def __init__(self, title, storyline, poster, trailer, duration):
		print "Movie constructor called"
		self.kind = 'Movie'
		Video.__init__(self, title, storyline, poster, trailer)
		self.duration = duration

	def gettype(self):
		return self.kind
		

	