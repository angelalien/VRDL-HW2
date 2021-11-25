# VRDL_HW2

Code for Selected Topics in Visual Recognition using Deep Learning(2021 Autumn NYCU) Homework2: Street View House Numbers detection. 
I use [YOLOv5](https://github.com/ultralytics/yolov5) object detection tool to handle this assignment.


## Requirements

To install requirements:

```setup
pip install -r requirements.txt
```
For Windows user to install pycocotools, first download [Microsoft Visual C++ Build Tools 2015](https://go.microsoft.com/fwlink/?LinkId=691126) and run this command:
```
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
```


## Dataset Preparation

To download the training dataset, run this command in the Python compiler:
```
from google_drive_downloader import GoogleDriveDownloader as gdd
gdd.download_file_from_google_drive(file_id='1lrKueI4HrySQDGvpkilQN9BfaMUN7hZi',
                                  dest_path='./train.zip',
                                  unzip=True)
```
After downloading and unzip, the data directory is structured as:
```
train
  +- digitStruct.mat
  +- see_bboxes.m
  +- 1.png
  +- 2.jpg
  ...  
```

Put the training images into 'images' file under the 'data' file in the project. The project structure is:
```
VRDL_HW2
  +- data
    +- images
      +- digitStruct.mat
      +- see_bboxes.m
      +- 1.png
      +- 2.png
      ...
    +- ImageSets
    +- labels
    ...
  make_txt.py
  mat_label.py
  ...
```
Run this command to prepare for data of label and bounding boxes:
```
python mat_label.py
```
> This command will make some text files in 'labels' file.



## Training 

To train the model, run this command:

```train
cd {YOUR_ROOT_PATH}/VRDL_HW2
python train.py
```

After running, you will get some output files in './VRDL_HW2/runs' file

## Pre-trained Models

You can download pretrained models here:

- [YOLOv5m finetuned model](https://drive.google.com/file/d/1rSobTs4LKR3nlNpgxU2ddupZPxLRTm0G/view?usp=sharing) trained and finetuned based on weight YOLOv5m.pt.
- [YOLOv5s finetuned model](https://drive.google.com/file/d/1Wu2p1zkpzu16YI8LIXH-5y7ud3BCAYY2/view?usp=sharing) trained and finetuned based on weight YOLOv5s.pt.
  

Model's hyperparameter setting:

-  batch size = 16
-  epochs = 10
-  initial learning rate=0.01, momentum=0.937, weight_decay=0.0005
-  warmup_epochs=3, warmup_momentum=0.8, warmup_bias_lr=0.1



## Make Submission

To make the submission file, run the [inference.ipynb](https://colab.research.google.com/drive/1FK2XSomj95RBmlysPKwET1IwkDAvdzpA?usp=sharing).
After running, you will get an output file: answer.json for submission


## Result

My model achieves the following performance on CodaLab:
| Model name               | Top 1 mAP  |
| ------------------------ |----------- |
| YOLOv5m finetuned model  |   40.26%   |
| YOLOv5s finetuned model  |   39.63%   |
