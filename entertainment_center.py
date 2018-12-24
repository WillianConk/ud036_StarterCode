import fresh_tomatoes
import media



fight_club = media.Movie("Fight club",
                        "An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.",
                        "https://m.media-amazon.com/images/M/MV5BMjJmYTNkNmItYjYyZC00MGUxLWJhNWMtZDY4Nzc1MDAwMzU5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")

the_little_rascals = media.Movie("The little rascals",
                     "Alfalfa is wooing Darla and his he man woman hatingM friends attempt to sabotage the relationship.",
                     "https://upload.wikimedia.org/wikipedia/pt/thumb/7/70/The_Little_Rascals.jpg/200px-The_Little_Rascals.jpg",
                     "https://www.youtube.com/watch?v=8rwbA5mInW8")

the_ballad_of_buster_scruggs = media.Movie("The ballad of Buster Scruggs",
                                            "An anthology film comprising six stories, each dealing with a different aspect of life in the Old West",
                                            "http://br.web.img2.acsta.net/c_215_290/pictures/18/09/10/11/40/4457327.jpg",
                                            "https://www.youtube.com/watch?v=_2PyxzSH1HM")

movies =[fight_club, the_little_rascals, the_ballad_of_buster_scruggs]
fresh_tomatoes.open_movies_page(movies)
