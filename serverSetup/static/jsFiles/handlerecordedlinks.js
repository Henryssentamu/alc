
async function fetchRecordedSessionLinks(){
    return await fetch("handleRecordedLinks")
        .then(response =>{
            if(!response.ok){
                throw new Error("recordedSessions ROUTE DID NOT SEND RECORDED SESSION LINKS ")
            }
            return response.json()
        })

        .then(data =>{
            console.log("here is the recorded session link:",data)
            return data
        })

}

async function loadhtml(){
    var recorded_links = await fetchRecordedSessionLinks()
    var html_recorded_links = ""
    recorded_links.forEach((items)=>{
        html_recorded_links += `
        <div class="session">
        <h2> Session: ${items["SessionTitle"]}</h2>
        <p>Date:${items["Date"]}</p>
        <p>Topic:${ items["topicCovered"]}</p>
        <a href="${items["Link"]}">Watch Recorded Session</a>
    </div>   
        `
    })
    console.log(html_recorded_links)

    document.querySelector(".container")
        .innerHTML = html_recorded_links

}
loadhtml()

