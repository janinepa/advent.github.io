# Advent Calendar Web Application - A Christmas Escape Story

This project is an interactive advent calendar web application that tells a christmas story each day of December, where the user can solve small riddles, puzzles, and mindfulness tasks every day. 

https://github.com/user-attachments/assets/f153e6b9-219b-49b1-b31d-3cac6d4be336

Behind each day awaits a short animated scene and a small escape-room-style puzzle. Step into a frozen Christmas village, recover the lost starlight, and help time flow again so Christmas can begin.

The site is live at [https://janinepa.github.io/advent-calender-web-app/](https://janinepa.github.io/advent-calender-web-app/)

## Features

- **Daily Doors**: Each day from December 1st to December 24th has its own door with a unique video and riddle.
- **Responsive Design**: The application is designed to be responsive and user-friendly.

## Tools
- **Animated Scenes**: The animated videos in this project were created using Banana Pro and Flow.
- **Audio and voices**: All narration and character voices were generated with ElevenLabs.
- **Riddle and Puzzles**: Riddle ideas and puzzle concepts were developed with the help of ChatGPT and implemented with the help of Gemini.


## Project Structure
```
advent-calendar-web
├── src
│   ├── index.html          # Main entry point for the web application
│   ├── doors               # Contains HTML files for each day's door
│   │   ├── day-01.html
│   │   ├── day-02.html
│   │   ├── ...
│   │   └── day-24.html
│   ├── components          # Reusable components for the application
│   │   └── door.html
│   ├── styles              # CSS styles for the application
│   │   └── main.css
│   ├── scripts             # JavaScript files for application logic
│   │   ├── app.js
│   │   └── utils.js
│   └── assets  
│       ├── images          # Directory for image files
│       ├── music           # Directory for music files
│       └── videos          # Directory for video files
├── .github
│   └── workflows           # GitHub Actions for deployment
│       └── deploy.yml
├── .gitignore              # Files to ignore in version control
├── package.json            # npm configuration file
└── README.md               # Project documentation
```

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Open `src` and start local server with `python3 -m http.server 8000`.
4. To view the application open http://localhost:8000 in your web browser.
