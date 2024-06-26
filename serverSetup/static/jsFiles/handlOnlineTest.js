async function fetchTestData() {
    return await fetch("handleOnlinetests")
      .then(response =>{
          if(! response.ok){
            throw new Error("handleOnlinTest api failed")
          }
          return response.json()
      })
      .then(data =>{
        return data
      })

      .catch(error =>{
        console.log("handleonlineExam api has failed")
      })

}




async function loadPage(){
    let data = await fetchTestData()
	// console.log(data)
	// alert(data)
	
	if ("Test Status" in data){	
		// Show no exam message and return
		document.getElementById('timer-container').style.display = "none";
		document.getElementById('submitBtn').style.display = "none"
		document.getElementById('no-exam-message').style.display = 'block';
		
		return;
	}

    // Timer duration in milliseconds (e.g., 5 minutes)
    const timerDuration = 0.30 * 60 * 1000; // 5 minutes
    let timeLeft = timerDuration / 1000; // Convert milliseconds to seconds
    let timerInterval;

   	// function to generate html for all questions

    function generatehtml(){
		let html
		data.forEach((dataObject, index) =>{
			html += `
				<div class="question-container">
					<p>${dataObject.Question}</p>
					<div class="options-container">
			`
			dataObject.Options.forEach((option, optionIndex) => {
				html += `
				<div class="option">
					<input type="radio" name="question-${index}" value="${option}" id="q${index}-option${optionIndex}">
					<label for="q${index}-option${optionIndex}">${option}</label>
				</div>
				`;
			});
			html += `
			</div>
			</div>
		`;
		})
		return html;
      
	}

	 // Function to render trivia questions on the page
    function renderQuestions() {
		document.getElementById('questions-section')
			.innerHTML += generatehtml()
    }

	// Function to update timer display
    function updateTimerDisplay() {
      const timerElement = document.getElementById('timer');
      const minutes = Math.floor(timeLeft / 60);
      const seconds = timeLeft % 60;
      timerElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
    
	// Function to redirect user to the provided page
    function redirectToProvidedPage() {
      window.location.href = 'loadPaidcourseOnstudentPortal';
    }

	// Function to send answers to the server
	function sendeAnswersToServer(answerObject){
		var courseId = data[1]["courseId"]
		var studentId = data[0]["studentId"]
		var TestId = data[0]["TestId"]
		fetch("handleOnlinetests",{
			method: "POST",
			headers:{
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				"studentId":studentId,
				"TestId": TestId,
				"courseId": courseId,
				"answers":answerObject
			})
		}) 
		.then(response => response.json())
		.then(data =>{
			// console.log(data)
		})
		.catch(error =>{
			console.log("failed to send answers to the backend ")
		})

	}

	// Function to submit user answers
    function submitAnswers() {
		clearInterval(timerInterval); // Stop the timer
		const userAnswers = [];
		data.forEach((questionData, index) => {
			const selectedOption = document.querySelector(`input[name="question-${index}"]:checked`);
			if (selectedOption) {
				userAnswers.push(selectedOption.value);
		
			}
			else {
				
				userAnswers.push(null); // Indicate unanswered questions
			}
		});
		// console.log(userAnswers); // You can process or display user answers here
		sendeAnswersToServer(userAnswers)
		
		redirectToProvidedPage();
		      
    }

	// Function to auto-submit answers when the timer elapses
    function autoSubmitAnswers() {
		clearInterval(timerInterval); // Stop the timer
		submitAnswers(); // Call the function to submit answers
    }

	// Call the function to render trivia questions when the page loads
	function loadEverything(){
		window.onload = renderQuestions()

		// Set timer for auto-submit
		timerInterval = setInterval(function() {
			timeLeft -= 1;
			if (timeLeft <= 0) {
			autoSubmitAnswers();
			}
			updateTimerDisplay();
		}, 1000);

		// Initial timer display
		updateTimerDisplay();
		document.getElementById("submitBtn")
			.addEventListener("click",()=>{
				submitAnswers()
			})
    };
	loadEverything()    

}

loadPage()

