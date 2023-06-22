$(document).ready(function () {
    $(".owl-carousel").owlCarousel({
      items: 2,
      loop: true,
      autoplay: true,
      autoplayTimeout: 3000,     
    //   nav,
    });
  });

  // let tabsBtn = document.querySelectorAll("#tabsBtn");
  // let tabsItems = document.querySelectorAll(".audio__first");
  // tabsBtn.forEach((item) => {
  //   item.addEventListener("click", () => {
  //     let currentBtn = item;
  //     let tabId = currentBtn.getAttribute("data-tab");
  //     let currentTab = document.querySelector(tabId);
  //     if (!currentBtn.classList.contains("active")) {
  //       tabsBtn.forEach((item) => {
  //         item.classList.remove("active");
  //       });
  //       tabsItems.forEach((item) => {
  //         item.classList.remove("active");
  //       });
  //       currentBtn.classList.add("active");
  //       currentTab.classList.add("active");
  //     }
  //   });
  // });
  // document.querySelector("#tabsBtn").click();

// let navbarItems = document.querySelectorAll('.nav-link');

// navbarItems.forEach((item)=>{
//   console.log('fwae');
//   item.addEventListener('click', ()=>{
//     let nav = item;
//     nav.classList.add('active')
//   })
// })



function inc(com, id) {
  if (com=='+'){
    let num = document.getElementById('count'+id)
    let count = parseInt(num.textContent)
    let b = count +1
    num.innerHTML=String(b)
    
  }
  else {
    let num = document.getElementById('count'+id)
    let count = parseInt(num.textContent)
    if (count == 0){
      return
    }
    let b = count -1
    num.innerHTML=String(b)
  }
}