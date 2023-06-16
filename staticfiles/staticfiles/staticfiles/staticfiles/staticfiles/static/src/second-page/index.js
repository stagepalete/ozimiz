

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
    if (event.target == modalEnroll || event.target == modalSendedEmail || event.target == modalLogin || event.target == modalSignin || event.target == modalTroubleAccount) {
        modalLogin.style.display = "none";
        modalSignin.style.display = "none";
        modalTroubleAccount.style.display="none";
        modalSendedEmail.style.display="none";
        modalEnroll.style.display="none";
    }
}

function handleModalSendedEmail(){
    modalSendedEmail.style.display = "block";
    modalTroubleAccount.style.display="none";
}


const acc = document.getElementsByClassName("accordion");
var i;
for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}



function countdown(days, hours, minutes, seconds) {
            var countdownElement = document.getElementById("countdown");
            var totalSeconds = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds;
            var interval = setInterval(function() {
                var daysRemaining = Math.floor(totalSeconds / (24 * 60 * 60));
                var hoursRemaining = Math.floor((totalSeconds / (60 * 60)) % 24);
                var minutesRemaining = Math.floor((totalSeconds / 60) % 60);
                var secondsRemaining = Math.floor(totalSeconds % 60);
                countdownElement.innerText = daysRemaining + " дней, " + hoursRemaining + " часов, " + minutesRemaining + " минут, " + secondsRemaining + " секунд";
                if (totalSeconds <= 0) {
                    clearInterval(interval);
                    countdownElement.innerText = "Время истекло!";
                }
                totalSeconds--;
            }, 1000);
        }

        countdown(2, 5, 30, 10);


const modalEnroll = document.querySelector(".modal-enroll");
const sendBtn = document.querySelector("#sendBtn");

sendBtn.addEventListener("click", handlemodalEnroll);
function handlemodalEnroll(){
    modalEnroll.style.display = "block";
}