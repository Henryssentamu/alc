


let courseId = function () {
    return new Promise((resolve, reject) => {
        let course_id;
        document.querySelector('.course-enroll-button')
            .addEventListener("click", function() {
                course_id = this.dataset.productId;
                resolve(course_id);
        });
    });
}

async function send_courseId (){
    let id = await courseId()
    var body = {
        "type": "courseIdDetails",
        "data":id
    }


   return fetch("processDataForEnrolledCourse",{
        method:"POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body:JSON.stringify(body)
    })
        .then(response =>{
            if(!response.ok){
                throw new Error("it is possible that the course id is not sent to the backend server")
            }
            return id
            
        })
        
}

send_courseId()



