const signInButton = document.querySelector('.sign-in-button');
const signUpButton = document.querySelector('.sign-up-button');
const signUpBox = document.querySelector('.signup-box');
const loginBox = document.querySelector('.login-box');
const popUp = document.querySelector('.pop-up');
// TOGGLE TO LOGIN PAGE 
signInButton.addEventListener('click',()=>{
signUpBox.style.visibility ="hidden";
loginBox.style.visibility="visible";
});

// BLUR EVENT => SIGN UP PAGE POPS FIRST 
// popUp.addEventListener('blur',()=>{
//     signUpBox.style.visibility="visible";
//     loginBox.style.visibility="hidden";
// });

// TOGGLE TO SIGNUP PAGE 
signUpButton.addEventListener('click',()=>{
signUpBox.style.visibility="visible";
loginBox.style.visibility ="hidden";
});
