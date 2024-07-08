import os

import shutil

def populate_negative(name):

    destination=os.path.join("Database",name,"Negative")

    for person_names in os.listdir("Database"):
        if person_names !=name:
            count=0
            source=os.path.join("Database",person_names,"Positive")

            for files in os.listdir(source):
                source_file=os.path.join(source,files)
                
                shutil.copy(source_file,destination)
                count+=1

                if (count==100):
                    break


