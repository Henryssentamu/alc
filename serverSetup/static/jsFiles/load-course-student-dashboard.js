import {response} from './get_course_details.js'

async function generate_html(){
    var data = await response()
    var generated_html = `
        <div class="course-cards">
            <a href="#">
                <div class="course-backgroud-image-section">
                    <!-- <img class="course-image" src="../static/images/newimages/istockphoto-1075599562-2048x2048.jpg"> -->
                </div>
                <div class="course-details-section">
                    <div class="course-name">
                        ${data.courseName}
                    </div>
                </div>
            </a>
        
        </div>
    `
    // return generated_html
    localStorage.setItem("html",generated_html)

}

async function load_html(){
    await generate_html();
    // localStorage.setItem("html",store_html)
    var get_html = localStorage.getItem("html")
    console.log(get_html)

    document.querySelector(".main-body-section")
        .innerHTML += get_html
}

load_html()



