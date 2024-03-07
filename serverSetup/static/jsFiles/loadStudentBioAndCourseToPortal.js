//  async function getStudentBioAndCourseDetails(){
//     return await fetch("http://127.0.0.1:5000/getBioDataAndCourseDetails")
//     .then(response => {
//         if (! response.ok){
//             throw new Error("api in login did return data")
//         }
//         return response.json()
//     })
//     .then(data =>{
//         console.log(`data here:${data}`)
//         return data
//     })
//     .catch(error=>{
//         console.log("faced error while fetching student bio data and paid course details:",error)
//     })
// }

// console.log(getStudentBioAndCourseDetails())
//  console.log(data)

 async  function fetchStudentDetailsData(){
    return await fetch("http://127.0.0.1:5000/getBioDataAndCourseDetails")
    .then(response => {
        if (! response.ok){
            throw new Error("api in getBioDataAndCourseDetails route did return data")
        }
        return response.json()
    })
    .then(data =>{
        // console.log(data)
        return data
    })
    .catch(error=>{
        console.log("faced error while fetching student bio data and paid course details:",error)
    })
}

async function generateHtml(){
    var  jsonData = await fetchStudentDetailsData()
    var firstName = jsonData["firstName"]
    var secondName = jsonData["lastName"]
    var courseDetails =  jsonData["courseDetails"]
    var fullName = firstName + " ." + secondName[0]
    var generatedHtml = " "
    document.querySelector(".logedInstudentName")
        .innerHTML = fullName

    courseDetails.forEach(object => {
        generatedHtml += `
            <section class="generated-course">
                
                <a href="#">
                    <div class="course-image-section">
                    <img class="course-image" src="${object['imageLink']}">
                    </div>
                    <div class="course-titles">
                        ${object["courseName"]}
                    </div>
                </a>
                
            </section>
            
            
        `
    });
    document.querySelector(".student-course-section")
        .innerHTML = generatedHtml
    console.log(courseDetails)
}

generateHtml()