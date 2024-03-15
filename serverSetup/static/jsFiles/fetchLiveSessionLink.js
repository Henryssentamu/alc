async function fetchLiveSessionLink(){
    return await fetch("http://127.0.0.1:5000/handleLiveSessionLinks")
        .then(response =>{
            if(! response.ok){
                throw new Error("handleLiveSessionLinks route (api) didn't send data")
            }
            return response.json()
        })

        .then(data => {
            return data
        })

        .catch(error =>{
            console.log("fetch livesession link api has failed:",error)
        })
}   

async function loadLiveSessionLink(){
    
    var liveSessionLink = await fetchLiveSessionLink();

    let generatedhtml = `
        <div class="session-card">
        <h2> ${ liveSessionLink['Topic']}</h2>
        <p>Date: ${liveSessionLink['DateOfClass']}</p>
        <p>Time: ${liveSessionLink['Time']}</p>
        <p>Tuitor: ${liveSessionLink['instructorName']}</p>
        <button>
            <a href=${liveSessionLink['link']}">
                Join Session
            </a>
        </button>
        </div>
    `

    document.querySelector(".container")
        .innerHTML = generatedhtml

}

loadLiveSessionLink()


