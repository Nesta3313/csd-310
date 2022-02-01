#Richard Akindele
#Feb 1 2022
#Module 5.3

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.vzaco.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
cluster = MongoClient(url, tls=True, tlsAllowInvalidCertificates=True)

# connect pytech database
db = cluster.pytech

""" three student documents"""
# Richard Akindele data document
richard = {
    "student_id": "1007",
    "first_name": "Richard",
    "last_name": "Akindele",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "4.0",
            "start_date": "June 5, 2022",
            "end_date": "August 4, 2022",
            "courses": [
                {
                    "course_id": "MTH210",
                    "description": "Time series analysis",
                    "instructor": "Kunal Patel",
                    "grade": "A"
                },
                {
                    "course_id": "BIO201",
                    "description": "Biology",
                    "instructor": "John Robert",
                    "grade": "C"
                }
            ]
        }
    ]

}

# Brandon Dooley data document
brandon = {
    "student_id": "1008",
    "first_name": "Brandon",
    "last_name": "Dooley",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "3.98",
            "start_date": "June 5, 2022",
            "end_date": "August 4, 2022",
            "courses": [
                {
                    "course_id": "CHE201",
                    "description": "Organic chemistry",
                    "instructor": "James Wheeler",
                    "grade": "A"
                },
                {
                    "course_id": "CSD201",
                    "description": "Programming with Python",
                    "instructor": "Matt Turner",
                    "grade": "A-"
                }
            ]
        }
    ]
}

# Sydney data document
sydney = {
    "student_id": "1009",
    "first_name": "Sydney",
    "last_name": "Aruta",
    "enrollments": [
        {
            "term": "Fall",
            "gpa": "3.53",
            "start_date": "September 6, 2022",
            "end_date": "December 14, 2022",
            "courses": [
                {
                    "course_id": "COM310",
                    "description": "Data structure and Algorithm",
                    "instructor": "Matt Turner",
                    "grade": "A"
                },
                {
                    "course_id": "MTH 310",
                    "description": "Linear Algebra",
                    "instructor": "Kunal Patel",
                    "grade": "B+"
                }
            ]
        }
    ]
}

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
richard_student_id = students.insert_one(richard).inserted_id
print("  Inserted student record Richard Akindele into the students collection with document_id " + str(richard_student_id))

brandon_student_id = students.insert_one(brandon).inserted_id
print("  Inserted student record Brandon Dooley into the students collection with document_id " + str(brandon_student_id))

sydney_student_id = students.insert_one(sydney).inserted_id
print("  Inserted student record Sydney Aruta into the students collection with document_id " + str(sydney_student_id))

input("\n\n  End of program, press any key to exit... ")
