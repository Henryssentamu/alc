from databases import Courses


courseId = "prod_PcWpcg8596849j"
courseName = "Introduction To Programming with Python"
coursePriceId = "price_1OnHmBFEzGEPgpDScDoYHd6M"
coursePrice = "100"
discription = "This course has all you need to know about computer programming"
courseImageLink = "./static/images/facebook.png"

db = Courses(courseName= courseName, courseId=courseId,coursePrice=coursePrice,coursePriceId=coursePriceId,courseImageLink=courseImageLink,courseDiscription=discription)

# create tables
db.createTables()
# insert into tables
db.insertIntoTables()