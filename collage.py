import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


image1=cv2.imread(r"\image_first\bottom_left.jpg")
image2=cv2.imread(r"ani\image_first\bottom_right.jpg")
image3=cv2.imread(r"ani\image_first\top_left.jpg")
image4=cv2.imread(r"ani\image_first\top_right.jpg")

image11=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
image22=cv2.cvtColor(image2,cv2.COLOR_BGR2RGB)
image33=cv2.cvtColor(image3,cv2.COLOR_BGR2RGB)
image44=cv2.cvtColor(image4,cv2.COLOR_BGR2RGB)
plt.imshow(image33)
plt.show()


BLACK=[0,0,0]
image111=cv2.resize(image11,(200,200))
image222=cv2.resize(image22,(200,200))
image333=cv2.resize(image33,(200,200))
image444=cv2.resize(image44,(200,200))

image1111=cv2.copyMakeBorder(image111,5,10,10,5,cv2.BORDER_CONSTANT,value=BLACK)
image2222=cv2.copyMakeBorder(image222,5,10,5,10,cv2.BORDER_CONSTANT,value=BLACK)
image3333=cv2.copyMakeBorder(image333,10,5,10,5,cv2.BORDER_CONSTANT,value=BLACK)
image4444=cv2.copyMakeBorder(image444,10,5,5,10,cv2.BORDER_CONSTANT,value=BLACK)
plt.imshow(image2222)
plt.show()


Horizontal1=np.hstack([image3333,image4444])
Horizontal2=np.hstack([image1111,image2222])
Vertical_attachment=np.vstack([Horizontal1,Horizontal2])


plt.imshow(Vertical_attachment)
plt.show()
print(Vertical_attachment.shape)


image5=cv2.imread(r"ani\image_first\center.jpeg")
image55=cv2.cvtColor(image5,cv2.COLOR_BGR2RGB)
image555=cv2.resize(image55,(200,200))
image5555=cv2.copyMakeBorder(image555,10,10,10,10,cv2.BORDER_CONSTANT,value=BLACK)
plt.imshow(image5555)
plt.show()

image5556 = cv2.resize(image5555, dsize=(200,200))
Vertical_attachment[115:315,115:315] = image5556
plt.imshow(Vertical_attachment)
plt.show()


#image5556.shape

print(Vertical_attachment)
Vertical_attachment.size




nd_arr=np.reshape(Vertical_attachment,(-1,3))#-1 indicates we dont know how many rows will be there in the resized numpy arr
                                             #but we know there should be 3 columns r,g,b
print(nd_arr)

pd.DataFrame(data=nd_arr).to_csv('submission.csv',header=['r','g','b'],index=False)
#pd.DataFrame(data=nd_arr) 




