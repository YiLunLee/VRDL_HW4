import os 
import random
HR_path = './vrdl_data/val/HR_x3'
LR_path = './vrdl_data/val/LR_x3'
images = os.listdir(LR_path)
new_HR_path = './vrdl_data/vals_light/HR_x3s'
new_LR_path = './vrdl_data/vals_light/LR_x3s'
os.makedirs(new_HR_path, exist_ok=True)
os.makedirs(new_LR_path, exist_ok=True)

samples = random.sample(images, 30)
for img in samples:
    os.system('cp {} {}'.format(os.path.join(HR_path, img), os.path.join(new_HR_path, img)))
    os.system('cp {} {}'.format(os.path.join(LR_path, img), os.path.join(new_LR_path, img)))    