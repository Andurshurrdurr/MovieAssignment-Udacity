import media
import fresh_tomatoes

ToyStory = media.Movie("Toy Story",
							"A story of a boy and his boys that can talk", 
							"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
							"https://www.youtube.com/watch?v=KYz2wyBy3kc",
							"Duration: Perfect")



avatar = media.Movie("Avatar",
					"A marine on an alien planet",
					"https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg", 
					"https://www.youtube.com/watch?v=cRdxXPV9GNQ",
					"Duration: Forever")

TAWP = media.Movie("Team America World Police",
					"A movie about how America is a world police",
					"https://upload.wikimedia.org/wikipedia/en/5/53/Team_america_poster_300px.jpg",
					"https://www.youtube.com/watch?v=RPBX47zSktc",
					"1h 38m")



Breaking_bad = media.TvShow("Breaking Bad",
							"A series about how things can go terribly wrong",
							"http://images.amcnetworks.com/amc.com/wp-content/uploads/2010/12/breaking-bad-S5-400x600-compressedV1.jpg",
							"https://www.youtube.com/watch?v=HhesaQXLuRY",
							"1")

Scrubs = media.TvShow("Scrubs",
					"A series about medicine",
					"http://vignette3.wikia.nocookie.net/scrubs/images/b/b4/Season_5_iTunes_Artwork.jpg/revision/latest?cb=20090329210541",
					"https://www.youtube.com/watch?v=QEYcfHoWm2s",
					"5")

Seinfeld = media.TvShow("Seinfeld",
						"A series about NOTHING",
						"http://www.sonypictures.com/tv/seinfeld/assets/images/onesheet.jpg",
						"https://www.youtube.com/watch?v=M2lfZg-apSA",
						"4")
print Seinfeld.season

Movies = [ToyStory,avatar,TAWP]
TvShows = [Breaking_bad, Scrubs, Seinfeld]
print TAWP.gettype()
print Seinfeld.gettype()
print media.Movie.__name__
print media.Movie.__module__

fresh_tomatoes.open_movies_page(Movies, TvShows)