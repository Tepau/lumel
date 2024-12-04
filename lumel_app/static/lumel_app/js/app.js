// Document ready, start functions
document.addEventListener('DOMContentLoaded', function() {

    // Initialize AOS / Animation library
    addAOS();

    addLozad();
    addVHandVWValues();
});

const addAOS = () => {

    // Initialize AOS / Animation library
    // Init only for desktop
    AOS.init({
        disable: 'mobile'
      });
}

// LAZY LOAD
const addLozad = () => {
    const observer = lozad(); 
    observer.observe();
}  

/* 
Add --vh and --vw values to the root element
to fix the vh and vw units on mobile devices

*/
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



