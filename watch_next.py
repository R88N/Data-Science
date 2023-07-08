import spacy

# I am loading the _md language model

nlp = spacy.load('en_core_web_md')

# here is the movie description i will be using to compare with other movie descriptions
# this is so that i can build a model to recommend the next best alternative
def calc():
    planet_hulk = """Will he save their world or destroy it? When   the Hulk becomes too dangerous for the Earth, 
                    the Illuminati trick Hulk into a shuttle and launch him into space to a planet where Hulk can live in peace. 
                    Unfortunately, hulk lands on the planet Sakaar where he is sold into slavert and trained as a gladiator."""

    # i'll first need to nlp-ify the description
    model_movie = nlp(planet_hulk)

    # i am calling on the txt file to read the descriptions to be able to compare it to Planet Hulk
    with open('movies.txt') as f:
        lines = f.readlines()

    # I am listing out the available movie titles to be able to use it in the next set of loops

    movie_options = ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E', 'Movie F', 'Movie G', 'Movie H', 'Movie I', 'Movie J']

    # I would like to create a dictionary where the keys are the movie titles and the values are corresponding similarity scores
    # Lines is a list where each element represents a separate line from the file
    # I am then applying the similarity function and comparing each line to our Planet Hulk description

    movie_dict = {}
    for line in lines:
        similarity = round(nlp(line).similarity(model_movie), 4)

        movie_name = line[:7]     # this is to isolate the movie name from each line

        if movie_name in movie_options:
            movie_dict[movie_name] = similarity

    #print(movie_dict)

    # Here i am establishing what the highest value is from the dictionary using the max function

    dict_values = movie_dict.values()
    best_option = max(dict_values)

    #print(best_option)

    # I then want to find the corresponding key so i iterate over all items in the dictionary find the matching key to best_option

    best_movie_option = None
    for key, value in movie_dict.items():
        if value == best_option:
            best_movie_option = key
            break

    #print(best_movie_option)

    # I will then print the recommendation - movie with the highest similarity score
    print(f"\nYou might like to watch {best_movie_option} since you watched Planet Hulk with a similarity score of {best_option}")

calc()  