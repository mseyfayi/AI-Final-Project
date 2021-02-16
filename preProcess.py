import collections
import pandas as pd
from removeExtraWords import remove_extra_words


def train():
    trainData = pd.read_csv('train.csv')
    print("*************** read csv ***************")

    trainData['title'] = trainData['title'].apply(remove_extra_words)
    print("*************** remove extra title *****")

    trainData['comment'] = trainData['comment'].apply(remove_extra_words)
    print("*************** remove extra comment ***")

    verifiedTitle = []
    spamTitle = []

    verifiedComment = []
    spamComment = []

    verifiedRate = []
    spamRate = []

    for index, row in trainData.iterrows():
        title = row['title']
        comment = row['comment']
        rate = int(row['rate'])

        if row['verification_status'] == 1:
            verifiedTitle.extend(title)
            verifiedComment.extend(comment)
            verifiedRate.append(rate)
        else:
            spamTitle.extend(title)
            spamComment.extend(comment)
            spamRate.append(rate)
    print("*************** spam and ver appended **")

    allTitle = verifiedTitle + spamTitle
    allComment = verifiedComment + spamComment
    allRate = verifiedRate + spamRate
    print("*************** all appended ***********")

    verifiedTitle = collections.Counter(verifiedTitle)
    verifiedComment = collections.Counter(verifiedComment)
    verifiedRate = collections.Counter(verifiedRate)
    print("*************** verified count *********")

    spamTitle = collections.Counter(spamTitle)
    spamComment = collections.Counter(spamComment)
    spamRate = collections.Counter(spamRate)
    print("*************** spam count *************")

    allTitle = collections.Counter(allTitle)
    allComment = collections.Counter(allComment)
    allRate = collections.Counter(allRate)
    print("*************** all count **************")

    return (allTitle, verifiedTitle, spamTitle), (allComment, verifiedComment, spamComment), (
        allRate, verifiedRate, spamRate)


def test():
    testData = pd.read_csv('test.csv')
    print("*************** read csv ***************")

    testData['title'] = testData['title'].apply(remove_extra_words)
    print("*************** remove extra title *****")

    testData['comment'] = testData['comment'].apply(remove_extra_words)
    print("*************** remove extra comment ***")

    return testData
