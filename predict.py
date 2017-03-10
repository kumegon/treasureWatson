import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3
import csv

data_directory = 'treasure'

f = open('myparams.json', 'r')
jsondata = json.load(f)
f.close()
classifier_id = jsondata.get('classifier_ids')[0]
print(classifier_id)


def main():
    visual_recognition = VisualRecognitionV3('2016-05-20', api_key='dc1f4c8e185cf29ea8002aaf865b47f2b34c6d29')

    print('Start Creating Classifier')
    with open(join(dirname(__file__), sys.argv[1]), 'rb') as img:
        print(json.dumps(visual_recognition.classify(
            images_file=dogs,  threshold=0.1, classifier_ids=[classifier_id, 'default'])))

    print('Finish Creating Classifier')

if __name__ == '__main__':
        main()
