document.addEventListener('DOMContentLoaded', function() {
    addLozad();
    AOS.init();
    addVHandVWValues();
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

