from preProcess import test
from preProcess import train
from pandas import DataFrame
import subprocess

(allTitle, verifiedTitle, spamTitle), (allComment, verifiedComment, spamComment), (
    allRate, verifiedRate, spamRate) = train()

print('############### Train pre process ###############')

testData = test()

print('############### Test pre process  ###############')

verTitleSum = sum(verifiedTitle.values())
spamTitleSum = sum(spamTitle.values())

verCommentSum = sum(verifiedComment.values())
spamCommentSum = sum(spamComment.values())

verRateSum = sum(verifiedRate.values())
spamRateSum = sum(spamRate.values())

titleLen = len(allTitle)
allCommentLen = len(allComment)
rateLen = len(allRate)

answer_id = []
answer_verification_status = []


def bayes(data, target: dict, _sum, length):
    target_get = target[data] + 3
    return target_get / (_sum + length)


for index, row in testData.iterrows():
    title = row['title']
    comment = row['comment']
    rate = row['rate']
    verified = 1
    spam = 1
    for t in title:
        verified *= bayes(t, verifiedTitle, verTitleSum, titleLen)
        spam *= bayes(t, spamTitle, spamTitleSum, titleLen)

    for c in comment:
        verified *= bayes(c, verifiedComment, verCommentSum, allCommentLen)
        spam *= bayes(c, spamComment, spamCommentSum, allCommentLen)

    verified *= bayes(rate, verifiedRate, verRateSum, rateLen)
    spam *= bayes(rate, spamRate, spamRateSum, rateLen)

    verification_status = 1 if verified > spam else 0

    id = row['id']
    answer_id.append(id)
    answer_verification_status.append(verification_status)

print('############### Answer generated  ###############')

answer = {'id': answer_id, 'verification_status': answer_verification_status}
df = DataFrame(answer, columns=['id', 'verification_status'])
export_csv = df.to_csv('ans.csv', index=False)

print('############### ans.csv generated  ###############')

subprocess.run(["java", "-jar", 'CommentJudge.jar'])
