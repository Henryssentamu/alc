


// var socket = io.connect('http://127.0.0.1:5000');

// async function getSocketAlert(){
//     const response = await fetch("payments")
//     .then(response =>{
//         if(!response.ok){
//             throw new Error("socketio event was not sent to the client server")
//         }
//         return response
//     })
//     .then(data =>{
//         return data
//     })
//     .catch(error=>{
//         console.log(error)
//     })
//     return response

// }


// async function getStudentPaymentDetails(){
//     const dataResponse = await fetch(my_endpoint)
//         .then(response =>{
//             if(! response.ok){
//                 throw new Error("get resquest did not fetch data from the backend")
//             }
//             return response.json()
//         })
//         .then(data =>{
//             // console.log("we recieved this:",data)
//             // alert("DATA HERE",data)
//             return data
//         })
//         .catch(error =>{
//             console.log("faced this error while fetching data from the backend")
//         })
//         return dataResponse


// }

// function threadOfOperations(){
//     document.querySelector(".paymentButton")
//         .addEventListener("click", async ()=>{
//             try{
//                 await getSocketAlert()
//                 const recieved_dta = getStudentPaymentDetails()
//                 alert(`here: ${recieved_dta}`)
//                 console.log(`data recevied is here: ${recieved_dta}`)
//             }
//             catch(Error){
//                 console.log("if failed")
//             }
//         })

// }


// threadOfOperations()



// async function getStudentPaymentDetails() {
//     try {
//         const dataResponse = await fetch(my_endpoint);
//         if (!dataResponse.ok) {
//             throw new Error("get request did not fetch data from the backend");
//         }
//         const data = await dataResponse.json();
        
//     } catch (error) {
//         console.error("Error occurred while fetching data from the backend:", error);
//     }
// }

// async function getSocketAlert() {
//     try {
//         const response = await fetch("payments");
//         if (!response.ok) {
//             throw new Error("socketio event was not sent to the client server");
//         }
//         const data = await response.json();
//         return data;
//     } catch (error) {
//         console.error(error);
//         throw error;
//     }
// }

// let my_endpoint = "fetchPaymentDetails";

// var socket = io.connect('http://127.0.0.1:5000');

// function threadOfOperations() {
//     document.querySelector(".paymentButton").addEventListener("click", async () => { // Make the event listener async
//         try {
//             await getSocketAlert(); // Wait for getSocketAlert() to complete
//             await getStudentPaymentDetails(); // Wait for getStudentPaymentDetails() to complete
//         } catch (error) {
//             console.error("Error occurred", error);
//         }
//     });
// }

// threadOfOperations();






// function trigerGetPaymentDetails(){
//     socket.on("paymentDetailsAddedToDataBase", ()=>{
//         // when the socketio even is sent from the server side , the sendgetrequest function will get triggerd
//         sendGetRequest()
//     })
// }

// function sendGetRequest(){
//     // on click the payment button , this function will triger get reques to the server
//     document.querySelector(".paymentButton")
//         .addEventListener("click",()=>{
//             fetch(my_endpoint)
//                 .then(response =>{
//                     if (!response.ok){
//                         throw new Error("api did not return anything")
//                     }
//                     return response.json()
//                 })
//                 .then(Date =>{
//                     console.log(`data printed here ${data}`)
//                     alert("eeeeeee")
//                 })
//                 .catch(error => {
//                     console.error('Error fetching data:', error);
//                 });
//         })
// }










// function makePayment() {
//     FlutterwaveCheckout({
//         public_key: "FLWPUBK_TEST-SANDBOXDEMOKEY-X",
//         tx_ref: "titanic-48981487343MDI0NzMx",
//         amount: 54600,
//         currency: "NGN",
//         payment_options: "card, mobilemoneyghana, ussd",
//         redirect_url: "https://glaciers.titanic.com/handle-flutterwave-payment",
//         meta: {
//         consumer_id: 23,
//             consumer_mac: "92a3-912ba-1192a",
//         },
//         customer: {
//         email: "rose@unsinkableship.com",
//         phone_number: "08102909304",
//         name: "Rose DeWitt Bukater",
//         },
//         customizations: {
//         title: "The Titanic Store",
//         description: "Payment for an awesome cruise",
//         logo: "https://www.logolynx.com/images/logolynx/22/2239ca38f5505fbfce7e55bbc0604386.jpeg",
//         },
//     });
//     }
