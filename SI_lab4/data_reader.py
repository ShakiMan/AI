from gensim.parsing.preprocessing import remove_stopwords

FILE_NAMES = ["Dennis+Schwartz", "James+Berardinelli", "Scott+Renshaw", "Steve+Rhodes"]


def get_all_data(feature_class=3):
    rates = []
    reviews = []
    for name in FILE_NAMES:
        temp_rates, temp_reviews = __get_data_from_one_folder(name, feature_class)
        rates += temp_rates
        reviews += temp_reviews

    reviews = __delete_not_words(reviews)
    dataset = []
    if len(rates) != len(reviews):
        raise Exception("Difference in rates and reviews length. Check files.")
    else:
        for i in range(len(rates)):
            dataset.append((reviews[i], rates[i]))
    return reviews, rates


def __get_data_from_one_folder(file, feature_class=3):
    rates = []
    reviews = []
    with open(f'scaledata/{file}/label.{feature_class}class.{file}', 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            rates.append(line)
    with open(f'scaledata/{file}/subj.{file}', 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            line = remove_stopwords(line)
            reviews.append(line)

    return rates, reviews


def __delete_not_words(reviews):
    new_reviews = []
    for review in reviews:
        new_review = ""
        for word in review.split():
            if __is_word(word) and new_reviews == "":
                new_review += word
            elif __is_word(word):
                new_review += " " + word

        new_reviews.append(new_review)
    return new_reviews


def __is_word(word):
    for i in range(len(word)):
        if (word[i].lower() < "a" or word[i].lower() > "z") and word[i] != "'":
            return False
    return True


def get_data(data_name):
    rates = []
    reviews = []
    with open(f'scaledata/{data_name}/label.3class.{data_name}', 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            rates.append(line)
    with open(f'scaledata/{data_name}/subj.{data_name}', 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            reviews.append(line)

    dataset = []
    for i in range(len(rates)):
        dataset.append((reviews[i], rates[i]))

    return dataset


def get_all_reviews():
    reviews = []
    for name in FILE_NAMES:
        reviews += get_reviews(name)
    return reviews


def get_reviews(data_name):
    reviews = []
    with open(f'scaledata/{data_name}/subj.{data_name}', 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            line = remove_stopwords(line)
            reviews.append(line)

    reviews = __delete_not_words(reviews)
    return reviews


def get_ratings(data_name):
    ratings = []
    with open(f'scaledata/{data_name}/label.3class.{data_name}', 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            ratings.append(line)
    return ratings
