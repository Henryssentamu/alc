// // this api get both student data and paid course data, uses the data to generate course section on 
// // student portal then adds event listen which makes api that send the course id to the server on click to the handlerecorded link route

 async  function fetchStudentDetailsData(){
    return await fetch("http://127.0.0.1:5000/getBioDataAndCourseDetails")
    .then(response => {
        if (! response.ok){
            throw new Error("api in getBioDataAndCourseDetails route did return data")
        }
        return response.json()
    })
    .then(data =>{
        // console.log("mboooo uooo",data)
        return data
    })
    .catch(error=>{
        console.log("faced error while fetching student bio data and paid course details:",error)
    })
}

async function generateHtml(){
    var  jsonData = await fetchStudentDetailsData()
    console.log("ssys",jsonData)

    var firstName = jsonData["firstName"]
    var secondName = jsonData["lastName"]
    var courseDetails =  jsonData["courseDetails"]
    var cohort = jsonData["intake"]
    var fullName = firstName + " ." + secondName[0]
    var generatedHtml = " "
    document.querySelector(".logedInstudentName")
        .innerHTML = fullName
    if(courseDetails.length > 0){
        // console.log(courseDetails)
        courseDetails.forEach( (object, index)=> {
            // console.log(object['courseID'])
            generatedHtml += `
                <section class="generated-course">
                    
                    <a id="${index}" data-cohort="${cohort}" onclick="activateEventListner('${index}');" class="portalclass"  data-course-id="${object['courseID']}" href="http://127.0.0.1:5000/loadPaidcourseOnstudentPortal">
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
    }else{
        console.log("empty")
        generatedHtml += `
                <section class="noCourseMessage">
                You are not enrolled into any course yet.
                Access one at your right under 'Navigate To Course'.
                </section>
                
            `

    }
    
    document.querySelector(".student-course-section")
        .innerHTML = generatedHtml


        // after loading the html, it addes event listner on the click on the 
        // course in the student portal which picks the course id and this id is
        // send to handleRecordedLinks route by an api


}

function activateEventListner(id){
    var idElement = document.getElementById(id);
    
    // var i_d = this.getAttribute('data-course-id')
    var i_d = idElement.getAttribute('data-course-id')
    var cohort = idElement.getAttribute('data-cohort')

            
            // console.log(i_d)
            fetch("http://127.0.0.1:5000//loadPaidcourseOnstudentPortal", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "type":"student-paid-course",
                    "data":{ 
                        "courseId": i_d,
                        "cohort":cohort
                    }
                })
            })
            .then(response => response.json())
            .then(data => {
                // return data
                console.log("data courseId sent to the server", data);
                // alert(data)
            })
            .catch(error => {
                console.log("error occurred while sending course id picked from the student portal");
            });
}


generateHtml()


