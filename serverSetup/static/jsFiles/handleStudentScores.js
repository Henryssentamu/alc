async function fetchScores(){
    return await fetch("http://127.0.0.1:5000/handleStudentscores")
        .then(response =>{
            if(!response.ok){
                throw new Error("fetch score api failed")
            }
            return response.json()
        })
        .then(data =>{
            console.log(data)
            return data
        })
        .catch(error =>{
            console.log("fetch score api failed to fetch data from the server",error)
        })
}

async function loadScores(){
    var score = await fetchScores()
    console.log(score)
    var html = ""
    score.forEach((object)=>{
        for(var key in object){
            if (key == "testId"){
                html += `<div class="section">
                    
                    <div class="subsection">
                        <h2> Test </h2>
                        <p>Score: ${object["scores"]}%</p> <!-- Calculate the overall total score and display here -->
                    </div>
                </div>
                `
            }
            else if(key == "examId"){
                html += `<div class="section">
                    
                    <div class="subsection">
                        <h2> Exam </h2>
                        <p>Score: ${object["scores"]}%</p> <!-- Calculate the overall total score and display here -->
                    </div>
                </div>
                `
            }
        }
            
     

    })
    document.querySelector(".container")
        .innerHTML = html


    console.log("here are scores:",score)
}

loadScores()