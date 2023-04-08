const signinbtn = document.querySelector(".button");
const wrapperEl = document.querySelector(".wrapper")
// const wrapperEll= document.querySelector(".wrapper-2")
const registerEl = document.querySelector(".register")
const closeEl = document.querySelector(".close")
const createExploreEl= document.querySelector(".create-login")
// const closeEll= document.querySelector(".close2")
const signinbtn2 = document.querySelectorAll(".sign-in");

signinbtn.addEventListener("click",()=>{
    wrapperEl.style.display="flex"
    createExploreEl.style.display="none";
})

// signinbtn2.addEventListener("click",()=>{
//     wrapperEl.style.display="flex"
//     createExploreEl.style.display="none";
// })


closeEl.addEventListener("click",()=>{
    wrapperEl.style.display="none"
    createExploreEl.style.display="flex";
    // wrapperEll.style.display="none"
})

