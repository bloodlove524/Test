"""This creates 6 movie instances. They would be used to generate a webpage created by fresh_tomatoes.py"""
import media
import fresh_tomatoes

"""This is initializations of 6 movies."""
hell=media.Movie('Hell or High Water','A Dallas Movie','https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4NDA1OTA5NF5BMl5BanBnXkFtZTgwMDQ2MDM5ODE@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
'https://www.youtube.com/watch?v=JQoqsKoJVDw')
redarmy=media.Movie('Red Army','a movie about Soviet Union','https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxMDYwMTg3M15BMl5BanBnXkFtZTgwMDQ1NzQ0MzE@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
'https://www.youtube.com/watch?v=a_euhvZQMaw')
badgenius=media.Movie('Bad Genius','An exam cheating movie','https://images-na.ssl-images-amazon.com/images/M/MV5BMzMxMTFlMDYtNjIyNS00YzQ4LWJlMDAtNGQwY2RlZGJiMmM1XkEyXkFqcGdeQXVyNzEyMTA5MTU@._V1_SY1000_SX700_AL_.jpg',
'https://www.youtube.com/watch?v=CLdhN4oMxCQ')
libertyvalance=media.Movie('The Man Who Shot Liberty Valance','a Classic western movie','https://images-na.ssl-images-amazon.com/images/M/MV5BMGEyNzhkYzktMGMyZS00YzRiLWJlYjktZjJkOTU5ZDY0ZGI4XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg',
'https://www.youtube.com/watch?v=QEpd9Oj3vGw')
birdman=media.Movie('Birdman or (The Unexpected Virtue of Ignorance)','an Inarrito movie','https://images-na.ssl-images-amazon.com/images/M/MV5BODAzNDMxMzAxOV5BMl5BanBnXkFtZTgwMDMxMjA4MjE@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
'https://www.youtube.com/watch?v=uJfLoE6hanc')
beyond=media.Movie('Beyond the Hills','a Romanian movie','https://images-na.ssl-images-amazon.com/images/M/MV5BMjIzOTYwNDc4M15BMl5BanBnXkFtZTcwNjU1NzcwOQ@@._V1_SY1000_CR0,0,660,1000_AL_.jpg',
'https://www.youtube.com/watch?v=o-dQEtJQvyY')
movies=[hell,redarmy,badgenius,libertyvalance,birdman,beyond]

"""This generates a webpage to display movie information"""
fresh_tomatoes.open_movies_page(movies)
