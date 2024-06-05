import {response} from './get_course_details.js'
// import {SendNeededCouseId} from "./get_courseId_from_studentPortal.js"



async function sendPurchasedCourseDetails(){
    let data = await response();
    // this api sends student id and paid course id to the studentPaidCourseRecords
    //  route so that course padid 
    // data base is updated
 
    // fetch("studentPaidCourseRecords", {
    fetch("studentPaidCourseRecords", {
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
        // console.log(data)
    })
    .catch(error =>{
        console.log("investigate this error related to send purchased course details".error)
    })
    
}


// async function call_activator(){
//     await sendPurchasedCourseDetails();
//     SendNeededCouseId()
// }

sendPurchasedCourseDetails()


// call_activator()



