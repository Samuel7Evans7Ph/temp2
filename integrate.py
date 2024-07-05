import os
#import cv2
import numpy as np
from tensorflow.keras.models import model_from_json
import tensorflow as tf
import pickle

from layers import L1Dist



# Load the model architecture
#mode=tf.keras.models.load_model(model_path,custom_objects={'L1Dist':L1Dist})

#model = tf.keras.models.load_model(model_path, custom_objects={'L1Dist': L1Dist})
#model=tf.keras.models.load_model('c_siamese_model6.keras.zip')
def preprocess(file_path):
    byte_img=tf.io.read_file(file_path)

    img=tf.io.decode_jpeg(byte_img)

    img=tf.image.resize(img,(100,100))

    img=img/255

    return img


def verify(detection_threshold,verification_threshold,input_image,model):
    max_confidence=0

    person_name=""


    for name in os.listdir('Database'):
        count=0

        max_iter=25
        curr_iter=1

        for image_name in os.listdir(os.path.join('Database',name,'Positive')):
            curr_iter+=1
            
            validation_img=preprocess(os.path.join('Database',name,'Positive',image_name))
            
            result=model.predict([np.expand_dims(input_image,axis=0),np.expand_dims(validation_img,axis=0)])
            print(result)
            if result>detection_threshold:
                count+=1
            if curr_iter>=max_iter:
                break

        new_conf=count/min(len(os.listdir(os.path.join('Database',name,'Positive'))),max_iter)
        print(new_conf,"this is the confidence")


        if new_conf>max_confidence:
            max_confidence=new_conf
            person_name=name
        
    if max_confidence<verification_threshold:
        return "Nobody"
    else:
        return person_name


def integrate():

    with open('model_architecture.json','r') as json_file:
        loaded_model_json=json_file.read()
        model=model_from_json(loaded_model_json,custom_objects={'L1Dist':L1Dist})
    
    model.load_weights('model_weights.h5')
    
    
    model_path = '/home/evans_sam/temp/siamese_model.keras'
    
    
    
    for files in os.listdir('Image_Files'):
    
        input_img=preprocess(os.path.join('Image_Files',files))
    
        detection_threshold=0.5
    
        verification_threshold=0.8
        
    
        person_name=verify(detection_threshold,verification_threshold,input_img,model)
    
        print(person_name)
    

if __name__=="__main__":
    main()








   # self.verification.text='verified' if verified ==True else 'Unverified'
