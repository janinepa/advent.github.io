document.addEventListener('DOMContentLoaded', () => {
    const doors = document.querySelectorAll('.door');
    const menu = document.querySelector('.menu');

    // Load door data from data.js
    fetch('./scripts/data.js')
        .then(response => response.text())
        .then(data => {
            eval(data);
            setupDoors();
        });

    function setupDoors() {
        doors.forEach((door, index) => {
            door.addEventListener('click', () => {
                const day = index + 1;
                loadDoorContent(day);
            });
        });
    }

    function loadDoorContent(day) {
        const doorContent = document.querySelector('.door-content');
        doorContent.innerHTML = `
            <h2>Day ${day}</h2>
            <video controls>
                <source src="./assets/videos/day-${day}.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            <p>${riddles[day - 1]}</p>
        `;
    }

    menu.addEventListener('click', () => {
        const doorContent = document.querySelector('.door-content');
        doorContent.innerHTML = '<h2>Select a Day</h2>';
    });
});