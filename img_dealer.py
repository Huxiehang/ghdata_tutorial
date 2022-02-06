import os
import numpy as np
from PIL import Image

source_path="./data/test/"
target_path="./data/bmps/"
margin=24
for bmp in os.listdir(source_path):
    im = Image.open(os.path.join(source_path,bmp))
    im_np=np.array(im)
    im_np_cap=im_np[margin:480-margin,margin:480-margin]
    im_cap=Image.fromarray(im_np_cap)
    im_cap.resize((256,256),Image.BICUBIC)
    im_cap.save(os.path.join(target_path,bmp))