# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:08:53 2018

@author: Administrator
"""
# score tem code
resized_image = tf.image.resize_images(img, [size, size])
sess = tf.Session()
result = sess.run(resized_image)

test1 = pd.concat([testset,pd.DataFrame(shapelist),pd.DataFrame(shapecol)],axis=1)
test1.to_csv(r"E:\fashion ai\train\Annotations\abc.csv")
shapecol = []
shapelist = []
for i in range(len(idd)):
    img=cv2.imread(idd.iloc[i,0])
    shapecol.append(img.shape[0])
    imgnew = img.reshape((1,-1))
    diffnum = size*size*3 - imgnew.shape[1]
    if diffnum>0:
        imgpad = np.zeros((1,diffnum))
        diff = np.concatenate([imgnew,imgpad],axis=1)
    elif not diffnum:
        diff = img
    else:
        print ("warning:diffnum<0 ")
        shapelist.append(diff)
    if i>20:
        break

testset = dataset.iloc[:102,:]
colname = dataset.columns

imgplot = plt.imshow(img)
    
