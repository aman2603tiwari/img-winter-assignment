// import React from "react";
const arrows=document.querySelectorAll(".arrow");
const movieLists=document.querySelectorAll(".movie-list");
arrows.forEach((arrow,i)=> {
    
    const itemNumber=movieLists[i].querySelectorAll("img").length;
    let clickCounter=0;
    arrow.addEventListener("click",()=>{
        const ratio=Math.floor(window.innerWidth/300);
        clickCounter++;
        if (itemNumber-(4+ clickCounter)+(4-ratio)>=0){
            movieLists[i].style.transform=`translateX(${movieLists[i].computedStyleMap().get("transform")[0].x.value -307}px)`
        }else{
            movieLists[i].style.transform="translateX(0)";
            clickCounter=0;
        }
    });
    console.log(Math.floor(window.innerWidth / 275));
    
});

const ball=document.querySelector(".toggle-ball");
const items=document.querySelectorAll(".container,.movie-list-title,.navbar-container,.sidebar,.toggle,.left-menu-icon");
ball.addEventListener("click",()=>{
    items.forEach(item=>{
        item.classList.toggle("active");
    });
    ball.classList.toggle("active");
});
// const search1 = document.querySelector(".sidebar .left-menu-icon fa-solid fa-magnifying-glass");
// const search2= document.querySelector(".searchBox");
// search1.addEventListener("onclick",()=>{
//     search2.classList.searchBox("searching");
//     // search2.style.display=inline-block;
// });
function func(){
    console.log("working");
    let obj = document.getElementById("searchBox");
    if(obj.style.display == "none"){
        obj.style.display = "inline-block"
    }else{
        obj.style.display = "none"
    }
}

$(document).ready(function(){
  $('.dropdown-submenu a.test').on("click", function(e){
    $(this).next('ul').toggle();
    e.stopPropagation();
    e.preventDefault();
  });
});
$(window).on("load",function(){
    $(".loader-wrapper").fadeOut("slow");
  });
var availablekeywords=[];
const searchlist=document.getElementsByClassName("searchlist-item");
var i=0;
while(i<searchlist.length){
    availablekeywords[i]=searchlist[i].innerHTML;
    i++;
}
// var j=0;
// while(j<availablekeywords.length){
//     availablekeywords[j].style.color = "black";
//     j++;

// }
 
// export const availablekeywords = () => {
//     return{
//         searchlist.map
//     }
// }
// ['Salaar','Animal','Dhoom','Harry Potter','Dunki','fast and Furious','Action-jackson'];

const resultsBsox= document.querySelector(".result-box");
const inputBox=  document.getElementById("input-box");
inputBox.onkeyup=function(){
    let result=[];
    let input=inputBox.value;
    if(input.length){
        result=availablekeywords.filter((keyword)=>{
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
        console.log(result);
    }
    display(result);

    if(!result.length){
        resultsBsox.innerHTML='';
    }
}
function selectInput(list){
    inputBox.value=list.innerHTML;
    resultBox.innerHTML='';
}
function display(result){
    const content=result.map((list)=>{
        return "<li onclick=selectInput(this)>"+list+"</li>";

    });
    resultsBsox.innerHTML = "<ul>" +content.join('')+"</ul>";

}
var searchlist1=document.getElementsByClassName("searchlist-item");

console.log(searchlist1[0].innerHTML);


function signIn(){
    let oauth2Endpoint = "https://accounts.google.com/o/oauth2/v2/auth"

    let form = document.createElement('form')
    form.setAttribute('method','GET')
    form.setAttribute('action',oauth2Endpoint)

    let params = {
        "client_id":"926296752162-iu3agq72vfcq91dsn243bqeo6s35faru.apps.googleusercontent.com",
        "redirect_uri":"http://127.0.0.1:5500/profile.html",
        "response_type":"token",
        "scope":"https://www.googleapis.com/auth/userinfo.profile",
        "include_granted_scopes":'true',
        "state":"pass-through-value"

    }
    for(var p in params){
        let input = document.createElement('input')
        input.setAttribute('type','hidden')
        input.setAttribute('name',p)
        input.setAttribute('value',params[p])
        form.appendChild(input)

    }
    document.body.appendChild(form)
    form.submit()
}