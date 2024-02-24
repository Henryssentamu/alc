


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
    // console.log(id)
    // alert(id)


   return fetch("http://127.0.0.1:5000/fetchCourseDetails",{
        method:"POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body:JSON.stringify({"send_courseId":id})
    })
        .then(response =>{
            if(!response.ok){
                throw new Error("it is possible that the course id is not sent to the backend server")
            }
            return id
        })
        
}

send_courseId()