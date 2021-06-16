import time

import sklearn
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

from data_reader import get_all_data
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


def run(type: str, min_df=1, max_df=0.65, ngram_range=(1, 1), max_features=5000, alpha=0.1, feature_class=3,
        test_size=0.2, random_state=15):
    reviews, ratings = get_all_data(feature_class)

    x_train, x_test, y_train, y_test = train_test_split(reviews, ratings, test_size=test_size, random_state=random_state)
    vectorizer = TfidfVectorizer(min_df=min_df, max_df=max_df, ngram_range=ngram_range, max_features=max_features)
    x_train_counts = vectorizer.fit_transform(x_train)

    tfidf_transformer = TfidfTransformer()
    x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)

    x_test_counts = vectorizer.transform(x_test)
    x_test_tfidf = tfidf_transformer.transform(x_test_counts)

    if (type == "MultinomialNB"):
        clf = MultinomialNB(alpha=alpha)
    elif (type == "SVC_rbf"):
        clf = SVC(kernel='rbf')
    else:
        clf = SVC(kernel='linear')
    clf.fit(x_train_tfidf, y_train)

    y_pred = clf.predict(x_test_tfidf)
    print(accuracy_score(y_test, y_pred))
    f1_score = sklearn.metrics.f1_score(y_test, y_pred, average='weighted')
    print(f1_score)

    # test on second file
    text_clf = test_model(clf, ratings, reviews, vectorizer)

    # fine-tuning hyperparameters
    # fine_tuning_hyperparameters(x_train, y_train, clf)


def fine_tuning_hyperparameters(x_train, y_train, clf):
    parameters = {
        'vect__ngram_range': [(1, 1), (1, 2), (1, 3)],
        'vect__min_df': [1, 0.1, 0,2, 0.3],
        'vect__max_df': [0.95, 0.8, 0.65, 0.55],
        'clf__alpha': (1.0, 0.25, 0.1, 0.05),
    }

    text_clf = Pipeline([
        ('vect', TfidfVectorizer()),
        ('clf', clf),
    ])

    start = time.time()
    gs_clf = GridSearchCV(text_clf, parameters, cv=10, n_jobs=-1)
    gs_clf = gs_clf.fit(x_train, y_train)
    end = time.time()
    print(f"Best params: {gs_clf.best_params_}")
    print(f"Best score: {gs_clf.best_score_}")
    print(f"Mean score: {gs_clf.cv_results_['mean_test_score']}")
    print(f"Std score: {gs_clf.cv_results_['std_test_score']}")

    for param_name in sorted(parameters.keys()):
        print("%s: %r" % (param_name, gs_clf.best_params_[param_name]))

    print("\n\n\n", gs_clf)
    print((end - start), "s")


def test_model(clf, ratings, reviews, vectorizer):
    text_clf = Pipeline([
        ('vect', vectorizer),
        ('clf', clf),
    ])
    results = cross_val_score(text_clf, reviews, ratings, cv=10)
    print(results)

    return text_clf
