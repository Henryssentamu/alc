from databases import Courses


courseId = "prod_PdFc0uIbzgALKI"
courseName = "C PROGRAMMING "
coursePriceId = "price_1Onz6yFEzGEPgpDSiORKHVRo"
coursePrice = "50.00"
discription = "Introduction to programming"
courseImageLink = "./static/images/facebook.png"

db = Courses(courseName= courseName, courseId=courseId,coursePrice=coursePrice,coursePriceId=coursePriceId,courseImageLink=courseImageLink,courseDiscription=discription)

# create tables
db.createTables()
# insert into tables
db.insertIntoTables()