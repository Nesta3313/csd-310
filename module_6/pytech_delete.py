#Richard Akindele
#Feb 8 2022
#Module 6.3


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

# data for new insert

data = {
    "student_id": "1010",
    "first_name": "Joe",
    "last_name": "Byron"
}

# insert the test document into database 
data_id = students.insert_one(data).inserted_id


# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(data_id))

# call the find_one() method by student_id 1010
joe = students.find_one({"student_id": "1010"})



# display the results 
print("\n  -- DISPLAYING THE INSERTED DOCUMENT -- ")
print("  Student ID: " + joe["student_id"] + "\n  First Name: " + joe["first_name"] + "\n  Last Name: " + joe["last_name"] + "\n")



# call the delete_one method to remove Joe document
deleted_joe = students.delete_one({"student_id": "1010"})

# find all students in the collection 
updated_student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in updated_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")

