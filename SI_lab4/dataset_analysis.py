from data_analyzer import count_words, count_reviews_length, count_ratings_occurrence_frequency
from data_reader import get_reviews, get_ratings


def print_dict(dict):
    for key in dict.keys():
        print(f'{key} - {dict[key]}')


def analyse(dataset_name):
    reviews = get_reviews(dataset_name)
    counted = count_words(reviews)
    counted = {k: v for k, v in sorted(counted.items(), key=lambda item: item[1])}
    print_dict(counted)
    reviews_length, avg = count_reviews_length(reviews)
    reviews_length = {k: v for k, v in sorted(reviews_length.items(), key=lambda item: item[1])}
    print_dict(reviews_length)
    print(f'\n{avg}')
    ratings = get_ratings(dataset_name)
    ratings_occurrence = count_ratings_occurrence_frequency(ratings)
    print_dict(ratings_occurrence)
