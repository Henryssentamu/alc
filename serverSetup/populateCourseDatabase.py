from databases import Courses

coursid = [("prod_PcWpcg8596849j","price_1OnHmBFEzGEPgpDScDoYHd6M","Introduction To Programming with Python"),
           ("prod_PdEzUgIEgT78X5","price_1OnyVTFEzGEPgpDSSuXLUwCT","R programming "),
           ("prod_PdFKztJp8V135N","price_1OnyqKFEzGEPgpDSiizAerA2","Data base Management & SQL "),
           ("prod_PdFc0uIbzgALKI","price_1Onz6yFEzGEPgpDSiORKHVRo","C PROGRAMMING ")]


courseId = "prod_PcWpcg8596849j"
courseName = "Introduction To Programming with Python"
coursePriceId = "price_1OnHmBFEzGEPgpDScDoYHd6M"
coursePrice = "66.00"
discription = "Introduction to Programming with Python"
courseImageLink = "./static/images/facebook.png"
youtubeLink = "https://www.youtube.com/watch?v=6i3EGqOBRiU&list=PLdo5W4Nhv31bZSiqiOL5ta39vSnBxpOPT"
courseObj = {
    "courseId":courseId,
    "courseName": courseName,
    "coursePriceId":coursePriceId,
    "coursePrice":coursePrice,
    "discription":discription,
    "courseImageLink":courseImageLink,
    "youtubeLink":youtubeLink

}

db = Courses(courseObject= courseObj)

# create tables
db.createTables()
# insert into tables
db.insertIntoTables()