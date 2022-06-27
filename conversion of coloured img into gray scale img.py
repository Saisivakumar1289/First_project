import cv2  #here we are importing open cv module
#imread function is used to read the image from the path
#it contains 2 parameters 1 is path and the other is 0,1,-1
# 0 is used to convert coloured img into gray scale image
#1 is used to read original coloured picture
# -1 is used for high constract than the original img
img1=cv2.imread("data\\me.jpg",0)
#resize function is used to resize the img
img1=cv2.resize(img1,(1200,600))
# flip function is used to flip the img
# 1 means it change the image from left to right
# 0 means it change the image upside down in reverse manner
# -1 means it change the image upside down
img1=cv2.flip(img1,0)
# imshow function display img by performing operations
# it has 2 parameters 1.name of the screen i.e.,(title)  2.img (what img we want to display)
cv2.imshow("dav",img1)
# waitkey(0) means it specifies the life time of the inage on the console
# 0 means it waits for sometime otherwise it waits untill we shut
# 1 means it just blink and go
k=cv2.waitKey(0) & 0xFF
# max range of k is 255 i.e.,0 to 256 
# if k== ord(k) means whenever we click q after display the image it shut all the windows
if k==ord('q'):
    cv2.destroyAllWindows()
#if k==ord(s) means whenever we click s after displaying the image it saves the image 
# imwrite function is used to save the image it also has 2 parameters 
# 1 is name of the image and 2 is image
elif k==ord('s'):
    cv2.imwrite('res.jpg',img1)
    cv2.destroyAllWindows()    
cv2.destroyAllWindows()