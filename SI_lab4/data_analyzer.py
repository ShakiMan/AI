def count_words(reviews_list):
    counted_words = {}
    for review in reviews_list:
        words = review.split()
        for word in words:
            if word in counted_words:
                counted_words[word] += 1
            elif __is_word(word):
                counted_words[word] = 1

    # counted_words = {k: v for k, v in sorted(counted_words.items(), key=lambda item: item[1])}
    return counted_words


def count_reviews_length(reviews_list):
    reviews_lengths = {}
    review_id = 1
    avg = 0
    for review in reviews_list:
        length = 0
        words = review.split()
        for word in words:
            if __is_word(word):
                length += 1

        reviews_lengths[review_id] = length
        avg += length
        review_id += 1

    avg = avg / review_id
    # reviews_lengths = {k: v for k, v in sorted(reviews_lengths.items(), key=lambda item: item[1])}

    return reviews_lengths, avg


def count_ratings_occurrence_frequency(ratings_list):
    ratings_occurrence = {}
    for rating in ratings_list:
        if rating in ratings_occurrence:
            ratings_occurrence[rating] += 1
        else:
            ratings_occurrence[rating] = 1

    return ratings_occurrence


def __is_word(word):
    for i in range(len(word)):
        if (word[i].lower() < "a" or word[i].lower() > "z") and word[i] != "'":
            return False
    return True
