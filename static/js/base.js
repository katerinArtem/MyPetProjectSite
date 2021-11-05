
function menuSetup(){
    let hideDelay = 300;
    let menuLeaveTimer;
    let allDropDowns = document.querySelectorAll('._dropdown');
    for (let i = 0; i < allDropDowns.length; i++) {
        allDropDowns[i].addEventListener('mouseenter', function() {
            let thisItem = this;
            clearTimeout(menuLeaveTimer);
            for (let j = 0; j < allDropDowns.length; j++) {
                allDropDowns[j].classList.remove('active');
            }
            thisItem.classList.add('active');
        });
        allDropDowns[i].addEventListener('mouseleave', function() {
            let thisItem = this;
            menuLeaveTimer = setTimeout(function() {
                thisItem.classList.remove('active');
            }, hideDelay);
        });
    }
}
document.addEventListener('DOMContentLoaded', menuSetup);

    

var nav =  document.getElementById('navMenu')
var content = document.getElementById("godown")
content.style.paddingTop = (nav.clientHeight + 20) + 'px'

