

// function makePayment(paymentRefNo,studentId,studentPhoneNo,studentName, studentEmail) {
//     FlutterwaveCheckout({
//         public_key: "FLWPUBK_TEST-744d44e464c42b31e2ebf4ddb6ff2712-X",
//         tx_ref: `${paymentRefNo}`,
//         amount: 600,
//         currency: "USD",
//         payment_options: "card, mobilemoneyghana, ussd, mobilemoneyuganda, mobilemoneyrwanda, credit",
//         redirect_url: "https://glaciers.titanic.com/handle-flutterwave-payment",
//         meta: {
//             consumer_id: `${studentId}`,
//             consumer_mac: "92a3-912ba-1192a",
//         },
//         customer: {
//         email: `${studentEmail}`,
//         phone_number: `${studentPhoneNo}`,
//         name: `${studentName }`,
//         },
//         customizations: {
//         title: "ARICIA LEARNING CENTER",
//         description: "Payment for Python for Data scientist",
//         logo: "ALC",
//         },
//     });
//     }



// async function fetchPaymentReferenceNUmber(){
//     let reference = await fetch("http://127.0.0.1:5000/fetchPaymentDetails",{method:"GET"})
//         .then(response =>{
//             if (!response.ok){S
//                 throw new Error("api didnt return any results")
//             }
//             return response.json()
//         })
//         .then(data =>{
//             return data
//         })
//     return reference
// }

// document.querySelector(".submit")
//     .addEventListener("click", async ()=>{
//         try{
//             let paymentDetails = await fetchPaymentReferenceNUmber()
//             let name = paymentDetails["fullName"];
//             let ref = paymentDetails["refNo"];
//             let phone = paymentDetails["phoneNo"];
//             let Email = paymentDetails["email"];
//             let studenttId = paymentDetails["studentId"]
//             console.log(Email)

//             makePayment(studentEmail= Email,paymentRefNo=ref,studentPhoneNo=phone,studentName=name,studenttId=studenttId)
//         }
//         catch(Error){
//             console.log(Error)
//         }
//     })