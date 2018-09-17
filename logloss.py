import csv
from math import log

def logloss(filename):
    with open(filename, 'rb') as submission_file:
        reader = csv.reader(submission_file)
        next(reader)
        loss = 0
        n = 0
        for row in reader:
            img_id, predicted = row[0], row[1]
            predicted = float(predicted)
            expected = 1.0 if predicted > 0.5 else 0.0
            loss += expected*log(predicted) + (1-expected)*log(1-predicted)
            n += 1
        loss = -loss/n
        print n, loss

def polarize(filename, filename2):
    with open(filename, 'rb') as submission_file, open(filename2, 'wb') as new_submission_file:
        reader = csv.reader(submission_file)
        next(reader)
        writer = csv.writer(new_submission_file)
        writer.writerow(['id', 'label'])
        for row in reader:
            img_id, predicted = row[0], row[1]
            if predicted > 0.9:
                predicted = 1
            elif predicted < 0.1:
                predicted = 0
            writer.writerow([img_id, predicted])
    close(submission_file)
    close(new_submission_file)

if __name__ == __main__:
    polarize('submission.csv', 'submission.csv.2')
