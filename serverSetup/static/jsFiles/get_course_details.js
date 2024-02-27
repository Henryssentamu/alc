


export let response = async  function courseData() {
    return  await fetch("http://127.0.0.1:5000/fetchCourseDetails")
    .then(response => {
        if (!response.ok) {
            throw new Error("Backend server didn't send course details");
        }
        return response.json();
    })
    .then(data => {
        // console.log(data);
        return data; // Returning the data
    })
    .catch(error => {
        console.log("API failed:", error);
        throw error; // Re-throwing the error to propagate it further
    });
}