
// RESP NAVBAR 
const hamburger=document.querySelector('.hamburger');
const navlinks=document.querySelector('.responsive-navlinks');
const nav=document.querySelectorAll('.responsive-navlinks li');
hamburger.addEventListener('click',()=>{
    //Toggle nav
navlinks.classList.toggle('nav-active');
//Animate list items
nav.forEach((link,index)=>{
    if(link.style.animation)
    {
        link.style.animation=``;
    }
    else{
        link.style.animation= `navLinkFade 0.5s ease forwards ${index/3+0.3}s`;
    }
});
hamburger.classList.toggle('toggle');
});
