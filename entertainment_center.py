import fresh_tomatoes
import media

la_haine = media.Movie("La Haine",
                        "24 hours in the lives of three young men in the French suburbs the day after a violent riot.",
                        "https://upload.wikimedia.org/wikipedia/en/3/30/Haine.jpg",
                        "https://www.youtube.com/watch?v=yk77VrkxL88",
                        "Budget: 2 590 000 euro", "Genres: Crime | Drama",
                        "Release dates: May 31 1995 (France), November 17 1995 (UK), February 9 1996 (US)",
                        "Directed by:	Mathieu Kassovitz", "Written by:	Mathieu Kassovitz",
                        "Starring:	Vincent Cassel, Hubert Kounde, Said Taghmaoui")

zift = media.Movie("Zift",
                    "'Zift' is a genre mixture of neo-noir and sots-art."
                    "The story unfolds in one night.Moth is freed on parole after spending time in prison on wrongful"
                    " conviction of murder. Jailed shortly before the Bulgarian communist coup of 1944, "
                    "he now finds himself in a new and alien world - the totalitarian Sofia of the 60s. ",
                    "http://www.altcine.com/posters/photo/zift-poster-2.jpg",
                    "https://www.youtube.com/watch?v=3mimnhbz2Qk",
                    "Budget: BGL 1 200 000",
                    "Genres: Crime | Drama | Mystery",
                    "Release date: 25 September 2008 (Bulgaria)",
                    "Director: Javor Gardev", "Writers: Vladislav Todorov ",
                    "Starring: Zachary Baharov, Tanya Ilieva, Vladimir Penev")

the_lives_of_others = media.Movie("The Lives of Others / Das Leben der Anderen (original title)",
                                   "In 1984 East Berlin, an agent of the secret police, conducting surveillance on a"
                                   " writer and his lover, finds himself becoming increasingly absorbed by their lives."
                                   "(Based on a true story)",
                                   "https://upload.wikimedia.org/wikipedia/en/9/9f/Leben_der_anderen.jpg",
                                   "https://www.youtube.com/watch?v=FppW5ml4vdw",
                                   "Budget: $2 000 000", "Genres: Drama | Thriller",
                                   " 23 March 2006 (Germany)", "Director: Florian Henckel von Donnersmarck",
                                   "Writer: Florian Henckel von Donnersmarck",
                                   "Starring: Ulrich Muhe, Martina Gedeck, Sebastian Koch")

carlos = media.Movie("Carlos",
                      "The story of Venezuelan revolutionary Ilich Ramirez Sanchez, who founded a worldwide terrorist"
                      " organization and raided the 1975 OPEC meeting.(Based on a true story)",
                      "https://upload.wikimedia.org/wikipedia/en/f/f6/CarlosPoster.jpg",
                      "https://www.youtube.com/watch?v=H3QkM7uyF10",
                      "Budget: $18 000 000", "Genres: Biography | Crime | Drama | Thriller",
                      "Release date: May 19 2010 (France-Germany)",
                      "Directed by:	Olivier Assayas", "Written by:	Olivier Assayas, Dan Franck, Daniel Leconte",
                      "Starring: Edgar Ramirez, Alexander Scheer, Nora von Waldstatten, Ahmad Kaabour,"
                      " Christoph Bach, Susanne Wuest, Anna Thalbach, Julia Hummer")

the_intouchables = media.Movie("The Intouchables / Intouchables (original title)",
                                "After he becomes a quadriplegic from a paragliding accident, an aristocrat hires a"
                                " young man from the projects to be his caregiver.(Based on a true story)",
                                "https://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg",
                                "https://www.youtube.com/watch?v=R8wUIez--WE",
                                "Budget	$10 800 000", "Genres: Biography | Comedy | Drama",
                                "Release dates: 23 September 2011 (San Sebastian),2 November 2011 (France)",
                                "Directed by:	Olivier Nakache & Eric Toledano",
                                "Written by	Olivier Nakache & Eric Toledano",
                                "Starring: Francois Cluzet, Omar Sy, Anne Le Ny")

happy_thank_you_more_please = media.Movie("Happythankyoumoreplease",
                                           "Captures a generational moment - young people on the cusp of truly "
                                           "growing up, tiring of their reflexive cynicism, each in their own ways"
                                           " struggling to connect and define what it means to love and be loved.",
                                           "https://upload.wikimedia.org/wikipedia/en/c/c2/Happythankyoumoreplease.jpg",
                                           "https://www.youtube.com/watch?v=Ls_SKFeJxEg",
                                           "Budget: N/A", "Genres: Comedy | Drama | Romance",
                                           "Release dates: January 20, 2010",
                                           "Directed by	Josh Radnor", "Written by	Josh Radnor",
                                           "Starring:	Malin Akerman, Tony Hale, Zoe Kazan, Kate Mara,"
                                           " Josh Radnor, Pablo Schreiber")

movies = [la_haine, zift, the_lives_of_others, carlos, the_intouchables, happy_thank_you_more_please]

# fresh_tomatoes module has this function open_movies_page
# that takes in argument, which is a list of movies and
# creates a HTML file which visualize them in a browser
fresh_tomatoes.open_movies_page(
    movies)

