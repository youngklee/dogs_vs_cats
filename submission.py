import csv
import glob
from subprocess import Popen, PIPE
import subprocess

def parse_dog_prob(text):
    words =  text.split()
    dog_prob_index = words.index('(0):')
    return words[dog_prob_index+1]

with open('submission.csv', 'wb') as submission_file:
    writer = csv.writer(submission_file)
    writer.writerow(['id', 'label'])

    i = 0
    for img_file in glob.glob('./test/*.jpg'):
        img_id = img_file.split('/')[-1].split('.')[0]
        process = Popen(['/home/ylee/tensorflow/bazel-bin/tensorflow/examples/label_image/label_image',
            '--graph=/tmp/output_graph.pb', '--labels=/tmp/output_labels.txt', '--output_layer=final_result',
            '--image=/home/ylee/dogs_vs_cats/test/' + img_id + '.jpg'], stdout=PIPE, stderr=PIPE)
    #    output = subprocess.check_output(['/home/ylee/tensorflow/bazel-bin/tensorflow/examples/label_image/label_image',
    #        '--graph=/tmp/output_graph.pb', '--labels=/tmp/output_labels.txt', '--output_layer=final_result',
    #        '--image=/home/ylee/dogs_vs_cats/submission/' + img_id + '.jpg'])
        (output, err) = process.communicate()
        dog_prob = parse_dog_prob(err)
        writer.writerow([img_id, dog_prob])
        i += 1
        if i % 100 == 0:
            print '{} images processed'.format(i)
        exit_code = process.wait()

