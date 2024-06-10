async function fetchAvailableCourses(){
    return    await fetch("schoolDataScience?type=availableCourses")
            .then(response =>{
                if(!response.ok){
                    throw new Error("fetch availabe courses failed")
                }
                return response.json()
            })
            .then(data =>{
                return data
            })
            .catch(error=>{
                console.log(error)
            })
}


async function generateHtml(){
    var data = await fetchAvailableCourses();
    var dataArray = data["data"]
    var html = "";
    
    
    dataArray.forEach(obj => {
        var route = obj["routeFunction"]
        html += `
            <div class="program-container">
                <div class="program-image-section">
                    <img class="program-thumbnail" src="${obj["courseImage"]}">
                </div>
                <div class="program-detail-section">
                    <div class="program-course-name">
                        ${obj["coursName"]}
                    </div>
                    <div>
                        ${obj["courseDiscription"]} 
                    </div>
                    <div class="program-duration">
                        ${obj["courseDuration"]}
                    </div>
                    <div class="program-enrrole-section">
                        <a href="${route}">
                            <button class="programe-enrrole-button">
                                Read More
                            </button>
                        </a>
                    </div>
                </div>
            </div>`;
    });

    return html
}


async function loadHtml(){
    var htmlData = await generateHtml()
    document.querySelector(".courses-under-school")
        .innerHTML += htmlData

}

loadHtml()

