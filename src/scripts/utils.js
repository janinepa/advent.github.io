/**
 * Triggers a star explosion animation on the screen.
 * Uses CSS animations defined in main.css.
 */
function triggerStarExplosion() {
    const container = document.createElement('div');
    container.className = 'star-explosion-container';
    document.body.appendChild(container);

    // Create multiple stars
    for (let i = 0; i < 60; i++) {
        const star = document.createElement('div');
        star.className = 'star-particle';

        // Randomize direction and distance
        const angle = Math.random() * 360;
        // Bigger explosion: 200px to 600px
        const distance = 200 + Math.random() * 400;
        // Longer duration: 1.5s to 2.5s
        const duration = 1.5 + Math.random() * 1.0;

        // Calculate translation in JS for better compatibility
        const rad = angle * (Math.PI / 180);
        const tx = Math.cos(rad) * distance;
        const ty = Math.sin(rad) * distance;

        star.style.setProperty('--tx', `${tx}px`);
        star.style.setProperty('--ty', `${ty}px`);
        star.style.animationDuration = `${duration}s`;

        // Randomize size slightly
        const size = 10 + Math.random() * 20; // 10px to 30px
        star.style.width = `${size}px`;
        star.style.height = `${size}px`;

        container.appendChild(star);
    }

    // sound effect (optional, maybe later)

    // Cleanup after animation (longer timeout)
    setTimeout(() => {
        container.remove();
    }, 3000);
}
