// this api get both student data and paid course data, uses the data to generate course section on 
// student portal then adds event listen which makes api that send the course id to the server on click to the handlerecorded link route

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
                
                <a  class="portalclass"  data-course-id="${object['courseID']}" href="http://127.0.0.1:5000/loadPaidcourseOnstudentPortal">
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


        // after loading the html, it addes event listner on the click on the 
        // course in the student portal which picks the course id and this id is
        // send to handleRecordedLinks route by an api


    document.querySelector(".portalclass")
        .addEventListener("click",function(event){
            // event.preventDefault();
            var i_d = this.getAttribute('data-course-id')
            // console.log(i_d)
            fetch("http://127.0.0.1:5000/handleRecordedLinks", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "courseId": i_d
                })
            })
            .then(response => response.json())
            .then(data => {
                // console.log("data courseId sent to the server", data);
                // alert(data)
            })
            .catch(error => {
                console.log("error occurred while sending course id picked from the student portal");
            });
        })


}


generateHtml()

