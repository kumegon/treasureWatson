import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3
import csv


f = open('myparams.json', 'r')
jsondata = json.load(f)
f.close()
classifier_id = jsondata.get('classifier_ids')[0]
print(classifier_id)


visual_recognition = VisualRecognitionV3('2016-05-20', api_key='dc1f4c8e185cf29ea8002aaf865b47f2b34c6d29')

print(json.dumps(visual_recognition.delete_classifier(classifier_id=classifier_id), indent=2))
