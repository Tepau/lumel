document.addEventListener('DOMContentLoaded', function() {
    addLozad();
    AOS.init();
    addVHandVWValues();
    addBurgerMenu();
});

// LAZY LOAD
const addLozad = () => {
    const observer = lozad(); 
    observer.observe();
}  

const addVHandVWValues = () => {
    const vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty("--vh", `${vh}px`);

    const vw = window.innerWidth * 0.01;
    document.documentElement.style.setProperty("--vw", `${vw}px`);


    window.addEventListener("resize", () => {
        const vh = window.innerHeight * 0.01;
        document.documentElement.style.setProperty("--vh", `${vh}px`);

        const vw = window.innerWidth * 0.01;
        document.documentElement.style.setProperty("--vw", `${vw}px`);
    });
};

const addBurgerMenu = () => {
    console.log('io')


    function burgerMenu() {
        console.log('aaaaa')

    const burger = document.querySelector(".burger");
    const burgerContainer = document.querySelector(".burger-container");

    burger.addEventListener("click", () => {
        burgerContainer.classList.toggle("active");
    });
}

burgerMenu();
window.addEventListener("resize", burgerMenu);

}

