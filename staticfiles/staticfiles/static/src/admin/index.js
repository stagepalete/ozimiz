

const filterBtns = document.querySelectorAll("filterBtns");

filterBtns.forEach(el=> el.addEventListener("click", handleFilterBtn));
function handleFilterBtn(event){
    console.log("hoho")
    event.target.classList.add("filter__btn-active");
}

const loginBtn = document.querySelector("#login");
const modalLogin = document.querySelector(".modal-login");


const siginBtn = document.querySelector("#signin");
const modalSignin = document.querySelector(".modal-signin");

loginBtn.addEventListener('click', handleLogin);
siginBtn.addEventListener('click', handleSignIn);

function handleLogin(){
    modalLogin.style.display = "block";
}

function handleSignIn(){
    modalSignin.style.display = "block";
}

const createAccountBtn = document.querySelector("#create-account");
createAccountBtn.addEventListener('click', handleCreateAccountBtn);

function handleCreateAccountBtn(){
    modalLogin.style.display = "none";
    modalSignin.style.display = "block";
}


const forgotPasswordBtn = document.querySelector("#forgot-password");
const modalTroubleAccount = document.querySelector(".modal-trouble-account");
forgotPasswordBtn.addEventListener('click', handlemodalTroubleAccount);

function handlemodalTroubleAccount(){
    modalLogin.style.display = "none";
    modalTroubleAccount.style.display="block";
}

const goToAccountBtn = document.querySelector(".go-to-account");
goToAccountBtn.addEventListener("click", handlegoToAccountBtn);
function handlegoToAccountBtn(){
    modalLogin.style.display = "block";
    modalSignin.style.display = "none";
}

const backToLoginBtn = document.querySelector("#backToLogin");
backToLoginBtn.addEventListener("click", handleBackToLoginBtn);
function handleBackToLoginBtn(){
    modalTroubleAccount.style.display="none";
    modalLogin.style.display = "block";
}

const modalSendedEmail = document.querySelector(".modal-sended-email");


window.onclick = function(event) {
    if (event.target == modalSendedEmail || event.target == modalLogin || event.target == modalSignin || event.target == modalTroubleAccount) {
        modalLogin.style.display = "none";
        modalSignin.style.display = "none";
        modalTroubleAccount.style.display="none";
        modalSendedEmail.style.display="none";
    }
}

function handleModalSendedEmail(){
    modalSendedEmail.style.display = "block";
    modalTroubleAccount.style.display="none";
}
