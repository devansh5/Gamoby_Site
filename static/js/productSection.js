const card1 =document.querySelector('.card1');
let image1 = document.querySelector('.image1');
let image2 = document.querySelector('.image2');
card1.addEventListener('mouseover', ()=>{
        image1.style.display ="none";
        image2.style.display ="block";
});
card1.addEventListener('mouseout', ()=>{
        image2.style.display ="none";
        image1.style.display ="block";
});


const card2 =document.querySelector('.card2');
let image3 = document.querySelector('.image3');
let image4 = document.querySelector('.image4');
card2.addEventListener('mouseover', ()=>{
        image3.style.display ="none";
        image4.style.display ="block";
});
card2.addEventListener('mouseout', ()=>{
        image4.style.display ="none";
        image3.style.display ="block";
});


const card3 =document.querySelector('.card3');
let image5 = document.querySelector('.image5');
let image6 = document.querySelector('.image6');
card3.addEventListener('mouseover', ()=>{
        image5.style.display ="none";
        image6.style.display ="block";
});
card3.addEventListener('mouseout', ()=>{
        image6.style.display ="none";
        image5.style.display ="block";
});


const card4 =document.querySelector('.card4');
let image7 = document.querySelector('.image7');
let image8 = document.querySelector('.image8');
card4.addEventListener('mouseover', ()=>{
        image7.style.display ="none";
        image8.style.display ="block";
});
card4.addEventListener('mouseout', ()=>{
        image8.style.display ="none";
        image7.style.display ="block";
});