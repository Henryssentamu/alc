async function FetchYoutubeLink(){
    return await fetch("handleCourseYouTubeLink")
        .then(response =>{
            if(!response.ok){
                throw new Error("api failed to fetch course youtube link ")
            }
            return response.json()
        })
        .then(data =>{
            // console.log("course youtou link:",data)
            return data
        })
        .catch(error =>{
            console.log("api error in fetching course youtube link",error)
        })
}

async function loadCourseYoutubeLink(){
    var link =  await FetchYoutubeLink()
    // console.log("course youtou link:",link["link"])
    document.querySelector(".addYoutubeLink")
        .innerHTML += `<a href="${link["link"]}"> Course Resources</a>`
}

loadCourseYoutubeLink()