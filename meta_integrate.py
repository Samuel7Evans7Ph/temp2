import os

from integrate import *

from detect import *


def meta_integrate(image):

    #will recieve the pic from from frontend via api
    start_verification(image)
    #after this is run ,a directory image files will be saved with each face detected as a seperate file

    integrate()
    #this will get us all the faces and their corresponding names guessed.
    #this must be further passed via api to the frontend

    #after this the status needs to be updated as finished in the database and perhaps the name could also be stored.






    











