import cv2
import matplotlib.pyplot as plt
import os

from database_population import *



face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
def bounding_box(img):
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imwrite(os.path.join("Image_Files","hello.jpg"),img)
    face=face_classifier.detectMultiScale(grey_img,scaleFactor=1.1,minNeighbors=4,minSize=(40,40))

    #os.makedirs("Image_Files")
    count=0
    for (x,y,w,h) in face:
        #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,4),1)
        image=img[y:y+h,x:x+w]
        count+=1
        #print(image)
        return image



    return len(face)
cap = cv2.VideoCapture(0)

count =0

name=input("enter the name of the person")

os.makedirs(os.path.join("Database",name))


os.makedirs(os.path.join("Database",name,"Positive"))
os.makedirs(os.path.join("Database",name,"Negative"))

os.makedirs(os.path.join("Database",name,"Anchor"))

while cap.isOpened():
    ret, frame = cap.read()
    
    #frame=frame[120:250+120,200:200+250,:]
    if not ret:
        break

    # Display the frame in a window
    cv2.imshow("image", frame)

    # Exit the loop when 'q' is pressed
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

    if cv2.waitKey(1) & 0xFF==ord('a'):
        frame=bounding_box(frame)
        if frame:
            if(count>50):
                cv2.imwrite(os.path.join("Database",name,"Anchor",f"image_{count}.jpg"),frame)
                count+=1
            else:
                print("here?")
                cv2.imwrite(os.path.join("Database",name,"Positive",f"image_{count}.jpg"),frame)
                count+=1

    if count==100:
        break


populate_negatives(name)

# Show the last captured frame using matplotlib
plt.imshow(frame)
plt.title("Last Captured Frame")
plt.show()

print(frame.shape)

cap.release()
cv2.destroyAllWindows()
