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
