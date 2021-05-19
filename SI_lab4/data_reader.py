FILE_NAMES = ["Dennis+Schwartz", "James+Berardinelli", "Scott+Renshaw", "Steve+Rhodes"]


def get_all_data():
    rates = []
    reviews = []
    for name in FILE_NAMES:
        temp_rates, temp_reviews = __get_data_from_one_file(name)
        rates += temp_rates
        reviews += temp_reviews

    dataset = []
    if len(rates) != len(reviews):
        raise Exception("Difference in rates and reviews length. Check files.")
    else:
        for i in range(len(rates)):
            dataset.append((reviews[i], rates[i]))
    return dataset


def __get_data_from_one_file(file):
    rates = []
    reviews = []
    with open(f'scaledata/{file}/rating.{file}', 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            rates.append(line)
    with open(f'scaledata/{file}/subj.{file}', 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            reviews.append(line)

    return rates, reviews


def get_data(data_name):
    rates = []
    reviews = []
    with open(f'scaledata/{data_name}/rating.{data_name}', 'r') as f:
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
    reviews =[]
    for name in FILE_NAMES:
        reviews += get_reviews(name)
    return reviews

def get_reviews(data_name):
    reviews = []
    with open(f'scaledata/{data_name}/subj.{data_name}', 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            reviews.append(line)
    return reviews


def get_ratings(data_name):
    ratings = []
    with open(f'scaledata/{data_name}/rating.{data_name}', 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            ratings.append(line)
    return ratings
