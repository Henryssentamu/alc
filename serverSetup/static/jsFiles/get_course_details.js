


export let response = async  function courseData() {
    // this api get student id and the course id of the purchased course from fetchCourseDetails route
    return  await fetch("http://127.0.0.1:5000/fetchCourseDetails")
    .then(response => {
        if (!response.ok) {
            throw new Error("Backend server didn't send course details");
        }
        return response.json();
    })
    .then(data => {
        // console.log('mbo da ',data);
        return data; // Returning the data
    })
    .catch(error => {
        console.log("API failed:", error);
        throw error; // Re-throwing the error to propagate it further
    });
}