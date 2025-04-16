document.addEventListener('DOMContentLoaded', function() {
    const introText = document.getElementById('intro-text');
    
    // Simple animation effect: Fade in the intro text
    introText.style.opacity = 0;
    let opacity = 0;
    const fadeInInterval = setInterval(function() {
        if (opacity < 1) {
            opacity += 0.05;
            introText.style.opacity = opacity;
        } else {
            clearInterval(fadeInInterval);
        }
    }, 50);

    // Log to console
    console.log("Welcome to my portfolio! Check out my projects below.");
});
