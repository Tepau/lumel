document.addEventListener('DOMContentLoaded', function() {
    addLozad();
    AOS.init();
});

// LAZY LOAD
const addLozad = () => {
    const observer = lozad(); 
    observer.observe();
}  

