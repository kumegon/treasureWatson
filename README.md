Treasure Learning using Watson API
====

## Overview
We can train treasures' images using Watson API.

##

## <a name ="req"> Requirement</a>
* Python 2.7.10
* [watson_developer_cloud](https://github.com/watson-developer-cloud/python-sdk)

## Usage
1. Please download [the data](https://drive.google.com/open?id=0BwGWkWRitjNiRXF5bndMaVlNNEU), unzip, and move to the this script's directory.

2. Learn images using Watson.(You can skip this step, because I had finished learn them. We can have only one classfier per an account, so if you want to learn, you have to delete a previous classifier.)
      ```
      $python train.py
      ```

3. If you want to know the state of this classifier, start 'getState.py'.
      ```
      $python getState.py
      ```

4. If you want to classify your image, start 'predict.py'.
      ```
      $python predict.py <your image>
      ```

5. If you want to delete the classifier, start 'deleteClassfier.py'.
      ```
      $python deleteClassfier.py
      ```

## Install
Please read [Requirement](#req) section, and install packages you haven't installed.


## Author

[kumegon](https://github.com/kumegon)
