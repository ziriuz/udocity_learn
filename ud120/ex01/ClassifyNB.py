# import the sklearn module for GaussianNB
from sklearn.naive_bayes import GaussianNB


def classify(features_train, labels_train):
    # create classifier
    gnb = GaussianNB()
    # fit the classifier on the training features and labels
    cls = gnb.fit(features_train, labels_train)
    # return the fit classifier
    return cls
