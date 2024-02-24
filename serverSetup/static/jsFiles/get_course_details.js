fetch("http://127.0.0.1:5000/fetchCourseDetails")
    .then(response =>{
        if(!response.ok){
            throw new Error("backend server didnt send course detals")
        }
        return response.json
    })
    .then(data =>{
        console.log(data)
    })
    .catch(Error =>{
        console.log("api failed")
    })