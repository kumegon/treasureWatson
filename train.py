import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3
import csv

data_directory = 'treasure'

f = open('./data/' + data_directory + '/list.csv','r')
items = [item[0] for item in csv.reader(f)]
f.close()

def main():
    visual_recognition = VisualRecognitionV3('2016-05-20', api_key='dc1f4c8e185cf29ea8002aaf865b47f2b34c6d29')

    print('Start Creating Classifier')
    with open(join(dirname(__file__), 'data/' + data_directory + '/train/0.zip'), 'rb') as item0, \
            open(join(dirname(__file__), 'data/' + data_directory + '/train/1.zip'), 'rb') as item1, \
            open(join(dirname(__file__), 'data/' + data_directory + '/train/2.zip'), 'rb') as item2, \
            open(join(dirname(__file__), 'data/' + data_directory + '/train/3.zip'), 'rb') as item3, \
            open(join(dirname(__file__), 'data/' + data_directory + '/train/4.zip'), 'rb') as item4, \
            open(join(dirname(__file__), 'data/' + data_directory + '/train/5.zip'), 'rb') as item5, \
            open(join(dirname(__file__), 'data/' + data_directory + '/train/6.zip'), 'rb') as item6, \
            open(join(dirname(__file__), 'data/' + data_directory + '/train/7.zip'), 'rb') as item7, \
            open(join(dirname(__file__), 'data/' + data_directory + '/train/8.zip'), 'rb') as item8:
        jsondata = visual_recognition.create_classifier('treasure',
                                                 item0_positive_examples=item0,
                                                 item1_positive_examples=item1,
                                                 item2_positive_examples=item2,
                                                 item3_positive_examples=item3,
                                                 item4_positive_examples=item4,
                                                 item5_positive_examples=item5,
                                                 item6_positive_examples=item6,
                                                 item7_positive_examples=item7,
                                                 item8_positive_examples=item8)
        print(json.dumps(jsondata, indent=2))
        classifier_id = jsondata.get('classifier_id')
        f = open('myparams.json', 'w')
        f.write('{ "classifier_ids": ["' + classifier_id + '", "default"] }')
        f.close()
    print('Finish Creating Classifier')

if __name__ == '__main__':
        main()
