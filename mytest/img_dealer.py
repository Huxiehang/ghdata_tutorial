import os
import numpy as np
from PIL import Image

def deal_img(source_path,target_path,margin):
    for bmp in os.listdir(source_path):
        im = Image.open(os.path.join(source_path,bmp))
        im_np=np.array(im)
        im_np_cap=im_np[margin:480-margin,margin:480-margin]
        im_cap=Image.fromarray(im_np_cap)
        im_cap.resize((256,256),Image.BICUBIC)
        im_cap.save(os.path.join(target_path,bmp))

class Dealer:
    def __init__(self,source_path,target_path) -> None:
        self.source=source_path
        self.target=target_path
        self.margin=24

    def deal_imgs(self):
        for bmp in os.listdir(self.source):
            self.deal_img(bmp).save(os.path.join(self.target,bmp))

    def deal_img(self,bmp):
        im = Image.open(os.path.join(self.source,bmp))
        im_np=np.array(im)
        im_np_cap=im_np[self.margin:480-self.margin,self.margin:480-self.margin]
        im_cap=Image.fromarray(im_np_cap)
        im_cap.resize((256,256),Image.BICUBIC)
        return im_cap
    