# VRDL_HW4: Super Resolution
This is homework 4 in NYCU Selected Topics in Visual Recognition using Deep Learning.


## Installation
build the environment via:
```
$ conda env create -f environment.yml
```
And install following packages:
```
$ pip install opencv-python
$ pip install yaml
$ pip install matplotlib
$ pip install tqdm
$ pip install scipy
```

## Prepare Dataset
Split the train data into train_set and validate set
Put the train image in the train folder: ./vrdl_data/images/train_set


The dataset folder should be like:
```
./vrdl_data
  |---train_set.txt
  |---val.txt
  |---test.txt
  |---images
        |---train_set
              |---xxxx.png
              |---xxxx.png
                    .
                    .
        |---val        
              |---xxxx.png
              |---xxxx.png
                    .
                    .
        |---test        
              |---xxxx.png
              |---xxxx.png
                    .
                    .
  |---labels
        |---train_set
              |---xxxx.txt
              |---xxxx.txt
                    .
                    .
        |---val        
              |---xxxx.txt
              |---xxxx.txt
                    .
                    .
```

## Training Code
1. 


## Evaluation code

## Download Pretrained Models
Here is the model weight of my final submission. Please download the weights and run the above evaluation code.
+ [Final_submission_weights](https://drive.google.com/file/d/1g-omXmyRrkKfIlSiu8pBUuowMgy9SBms/view?usp=sharing)

## Reference
My howework references the codes in the following repos. Thanks for thier works and sharing.
+ [SRFBN](https://github.com/Paper99/SRFBN_CVPR19)

