# VRDL_HW4: Super Resolution
This is homework 4 in NYCU Selected Topics in Visual Recognition using Deep Learning.


## Installation
build the environment via:
```
$ conda env create -f environment.yml
```
And install following packages:
```
$ pip install imageio
$ pip install opencv-python
$ pip install pandas
$ pip install flags
$ pip install scipy==1.2.2
```

## Prepare Dataset
Unzip the given dataset and put it in vrdl_data folder
The dataset folder should be like:
```
./vrdl_data
  |---training_hr_images/training_hr_images/*.png
  |---testing_lr_images/testing_lr_images/*.png
  
```

(For Training) For preparing training data, run the below code to genearate more training samples.
(Please make sure that the data directory is same as above form)
```
$ python Prepare_TrainData_HR_LR_VRDL.py
$ python Prepare_val_data.py
```

## Training Code
Start training with following command:
```
$ python train.py -opt ./options/train/train_SRFBN_VRDL.json
```

## Evaluation code
1. download the pretrained model bellow and put it at ./submission.pth
2. Run the testing code:
```
$ python test.py -opt ./options/test/test_SRFBN_VRDL.json
```


## Download Pretrained Models
Here is the model weight of my final submission. Please download the weights and run the above evaluation code.
+ [Final_submission_weights](https://drive.google.com/file/d/10v-yK4QhxlcpL8qfjagMWafwa89ZD_Y9/view?usp=sharing)

## Reference
My howework references the codes in the following repos. Thanks for thier works and sharing.
+ [SRFBN](https://github.com/Paper99/SRFBN_CVPR19)

