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

fetch("http://127.0.0.1:5000/getBioDataAndCourseDetails")
    .then(response => {
        if (! response.ok){
            throw new Error("api in getBioDataAndCourseDetails route did return data")
        }
        return response.json()
    })
    .then(data =>{
        console.log(data)
        return data
    })
    .catch(error=>{
        console.log("faced error while fetching student bio data and paid course details:",error)
    })