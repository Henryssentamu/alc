import {response} from './get_course_details.js'


async function sendPurchasedCourseDetails(){
    let data = await response();

    fetch("http://127.0.0.1:5000/studentPaidCourseRecords", {
        method: "POST",
        headers :{
            'Content-Type': 'application/json',
        },
        body:JSON.stringify(data)
    })
    .then(response =>{
        if (!response.ok){
            throw new Error("api failed to send purchased course details")
        }
        return "purchase detailes sent successfuly"
    })
    .then(data => {
        console.log(data)
    })
    .catch(error =>{
        console.log("investigate this error related to send purchased course details".error)
    })
    
}

// async function load_html(){
//     var get_html = sendPurchasedCourseDetails();
//     // localStorage.setItem("html",store_html)
//     // var get_html = localStorage.getItem("html")
//     // console.log(get_html)
//     console.log('can still be accessed here',data.studentId)

//     document.querySelector(".main-body-section")
//         .innerHTML += get_html
// }

// load_html()

sendPurchasedCourseDetails()



