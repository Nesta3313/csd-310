#Richard Akindele
#Feb 8 2022
#Module 6.2


import pymongo

from pymongo import MongoClient

# MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.vzaco.mongodb.net/pytech?retryWrites=true&w=majority"

cluster = MongoClient(url, tls=True, tlsAllowInvalidCertificates=True)

# connect to pytech database
db = cluster.pytech


# get the student collection
students = db.students

# find all students in the collection 
student_list = students.find({})


# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")


# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Nesta"}})

# find the updated student document 
richard = students.find_one({"student_id": "1007"})


# display message
print("\n  -- DISPLAYING UPDATED STUDENT DOCUMENT 1007 --")

# output the updated document to the terminal window
print("  Student ID: " + richard["student_id"] + "\n  First Name: " + richard["first_name"] + "\n  Last Name: " + richard["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")

    
