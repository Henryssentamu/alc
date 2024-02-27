
// function add_margic(){
//     var scrolosition = window.scrollY || document.documentElement.scrollTop;
//     var element = document.getElementById("header");
//     if (scrolosition >= 80){
//         element.classList.add("smaller")
//         console.log("it worked")
//     }
//     else{
//         element.classList.remove("smaller")
//     }
// }

window.addEventListener('scroll',()=>{
    var scrolosition = window.scrollY || document.documentElement.scrollTop;


    var element = document.getElementById("header");
    if (scrolosition >= 90){
        element.classList.add("smaller")
        // console.log("it worked")
        // alert("ittttt");
    }
    else{
        element.classList.remove("smaller")
    }

})




// window.onscroll = function(){
//     add_margic()
// }