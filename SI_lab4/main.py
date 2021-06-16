from dataset_analysis import analyse
from data_reader import get_all_data
from ml_system import run


def test_multinomial():
    print("MultinomialNB:\nAlpha changes\n")
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=1")
    run("MultinomialNB", 1, 0.65, (1, 1), 5000, 1)
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.25")
    run("MultinomialNB", 1, 0.65, (1, 1), 5000, 0.25)
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1")
    run("MultinomialNB", 1, 0.65, (1, 1), 5000, 0.1)

    print("MultinomialNB:\nngram_range changes\n")
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1")
    run("MultinomialNB", 1, 0.65, (1, 1), 5000, 0.1)
    print("min_df=1, max_df=0.65, ngram_range=(1, 2), max_features=5000, alpha=0.1")
    run("MultinomialNB", 1, 0.65, (1, 2), 5000, 0.1)
    print("min_df=1, max_df=0.65, ngram_range=(1, 3), max_features=5000, alpha=0.1")
    run("MultinomialNB", 1, 0.65, (1, 3), 5000, 0.1)

    print("MultinomialNB:\nmin_df changes\n")
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1")
    run("MultinomialNB", 1, 0.65, (1, 1), 5000, 0.1)
    print("min_df=0.1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1")
    run("MultinomialNB", 0.1, 0.65, (1, 1), 5000, 0.1)
    print("min_df=0.2, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1")
    run("MultinomialNB", 0.2, 0.65, (1, 1), 5000, 0.1)

    print("MultinomialNB:\nmax_df changes\n")
    print("min_df=1, max_df=0.95, ngram_range=(1, 1), max_features=5000, alpha=0.1")
    run("MultinomialNB", 1, 0.95, (1, 1), 5000, 0.1)
    print("min_df=1, max_df=0.8, ngram_range=(1, 1), max_features=5000, alpha=0.1")
    run("MultinomialNB", 1, 0.8, (1, 1), 5000, 0.1)
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1")
    run("MultinomialNB", 1, 0.65, (1, 1), 5000, 0.1)

    print("MultinomialNB:\nmax_features changes\n")
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=1000, alpha=0.1")
    run("MultinomialNB", 1, 0.65, (1, 1), 1000, 0.1)
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=2000, alpha=0.1")
    run("MultinomialNB", 1, 0.65, (1, 1), 2000, 0.1)
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1")
    run("MultinomialNB", 1, 0.65, (1, 1), 5000, 0.1)


def test_various_classifiers():
    print("MultinomialNB:\n")
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1")
    run("MultinomialNB", 1, 0.65, (1, 1), 5000, 0.1)

    print("SVC_rbf:\n")
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1")
    run("SVC_rbf", 1, 0.65, (1, 1), 5000, 0.1)

    print("SVC_linear:\n")
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1")
    run("SVC_linear", 1, 0.65, (1, 1), 5000, 0.1)


def test_various_classes():
    print("MultinomialNB:\n")
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1, label3.class")
    run("MultinomialNB", 1, 0.65, (1, 1), 5000, 0.1, 3)

    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1, label4.class")
    run("MultinomialNB", 1, 0.65, (1, 1), 5000, 0.1, 4)

    print("SVC_rbf:\n")
    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1, label3.class")
    run("SVC_rbf", 1, 0.65, (1, 1), 5000, 0.1, 3)

    print("min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1, label4.class")
    run("SVC_rbf", 1, 0.65, (1, 1), 5000, 0.1, 4)


def test_size_and_random_state():
    print("test_size = 0.1")
    run("MultinomialNB", test_size=0.1)

    print("test_size = 0.2")
    run("MultinomialNB", test_size=0.2)

    print("test_size = 0.3")
    run("MultinomialNB", test_size=0.3)

    print("random_state = 10")
    run("MultinomialNB", random_state=10)

    print("random_state = 15")
    run("MultinomialNB", random_state=15)

    print("random_state = 20")
    run("MultinomialNB", random_state=20)


if __name__ == '__main__':
    # print("Dennis+Schwartz\n\n")
    # analyse("Dennis+Schwartz")
    # print("\n\nJames+Berardinelli\n\n")
    # analyse("James+Berardinelli")
    # print("\n\nScott+Renshaw\n\n")
    # analyse("Scott+Renshaw")
    # print("\n\nSteve+Rhodes\n\n")
    # analyse("Steve+Rhodes")
    # dataset = get_all_data()
    # for data in dataset:
    #     print(data)
    # test_multinomial()
    # test_various_classifiers()
    # test_various_classes()
    # run("MultinomialNB")
    test_size_and_random_state()
