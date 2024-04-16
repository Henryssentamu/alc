from databases import Courses,SchoolDatabes
# from databases import SchoolDatabes

coursid = [("prod_PcWpcg8596849j","price_1OnHmBFEzGEPgpDScDoYHd6M","Introduction To Programming with Python"),
           ("prod_PdEzUgIEgT78X5","price_1OnyVTFEzGEPgpDSSuXLUwCT","R programming "),
           ("prod_PdFKztJp8V135N","price_1OnyqKFEzGEPgpDSiizAerA2","Data base Management & SQL "),
           ("prod_PdFc0uIbzgALKI","price_1Onz6yFEzGEPgpDSiORKHVRo","C PROGRAMMING "),
           ("prod_Pve3IFr6iwzyrF","price_1P5ml2FEzGEPgpDSvq5rYDAN","Introduction to machine learning")]


courseId = "prod_Pve3IFr6iwzyrF"
schoolId = "SODS"
courseName = "Introduction to machine learning"
coursePriceId = "price_1P5ml2FEzGEPgpDSvq5rYDAN"
coursePrice = "150.00"
discription = "Introduction to Software development with C"
courseImageLink = "./static/images/facebook.png"
youtubeLink = "https://www.youtube.com/watch?v=6i3EGqOBRiU&list=PLdo5W4Nhv31bZSiqiOL5ta39vSnBxpOPT"
courseObj = {
    "courseId":courseId,
    "schoolId": schoolId,
    "courseName": courseName,
    "coursePriceId":coursePriceId,
    "coursePrice":coursePrice,
    "discription":discription,
    "courseImageLink":courseImageLink,
    "youtubeLink":youtubeLink

}

# db = Courses(courseObject= courseObj)

# create tables
# db.createTables()
# insert into tables
# db.insertIntoTables()


""" note that the url used here referes to the route, and it is the same for all courses"""

availableSchools = [{
    "schoolId":"SODS",
    "SchoolName": "school of Data Science",
    "SchoolCoordinator":" Mr Ssentamu Henry",
    "schoolUrl":"/adminschoolTemplate"


},{
    "schoolId":"SOSE",
    "SchoolName": "school of Software Engineering",
    "SchoolCoordinator":" Mr Bukenya Tom",
    "schoolUrl":"/adminschoolTemplate"
    

}
]

school = SchoolDatabes(availableSchools)
created = school.createTables()
inserted = school.insertIntotables()

print(f"crreate: {created}")
print(f"insert: {inserted}")