import fresh_tomatoes
import media

# define variables for instances
fight_club = media.Movie("Fight club",
                         "An insomniac office worker and an underground club",
                         "https://bit.ly/2Q3cYes",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

the_little_rascals = media.Movie("The little rascals",
                                 "Alfalfa' relationshipo being sabotaged.",
                                 "https://bit.ly/2ETgRlc",
                                 "https://www.youtube.com/watch?v=8rwbA5mInW8")
the_ballad_of_buster_scruggs = media.Movie("The ballad of Buster Scruggs",
                                           "An anthology film",
                                           "https://bit.ly/2QRnV85",
                                           "https://bit.ly/2QmAGUl")
#define an array for movies inside the file fresh_tomatoes
movies = [fight_club, the_little_rascals, the_ballad_of_buster_scruggs]
#run the page created on fresh_tomatoes file
fresh_tomatoes. open_movies_page(movies)