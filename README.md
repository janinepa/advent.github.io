# Advent Calendar Web Application

This project is an Advent calendar web application that features a door for each day of December, displaying a video and a riddle. Users can navigate through the calendar using a menu that provides access to all the doors.

## Project Structure
cd /Users/macjanine/Uni/Advent/advent-calendar-web/src
python3 -m http.server 8000

```
advent-calendar-web
├── src
│   ├── index.html          # Main entry point for the web application
│   ├── doors               # Contains HTML files for each day's door
│   │   ├── day-01.html
│   │   ├── day-02.html
│   │   ├── day-03.html
│   │   ├── day-04.html
│   │   ├── day-05.html
│   │   ├── day-06.html
│   │   ├── day-07.html
│   │   ├── day-08.html
│   │   ├── day-09.html
│   │   ├── day-10.html
│   │   ├── day-11.html
│   │   ├── day-12.html
│   │   ├── day-13.html
│   │   ├── day-14.html
│   │   ├── day-15.html
│   │   ├── day-16.html
│   │   ├── day-17.html
│   │   ├── day-18.html
│   │   ├── day-19.html
│   │   ├── day-20.html
│   │   ├── day-21.html
│   │   ├── day-22.html
│   │   ├── day-23.html
│   │   └── day-24.html
│   ├── components          # Reusable components for the application
│   │   ├── door.html
│   │   └── menu.html
│   ├── styles              # CSS styles for the application
│   │   └── main.css
│   ├── scripts             # JavaScript files for application logic
│   │   ├── app.js
│   │   └── data.js
│   └── assets              # Directory for video files
│       └── videos
├── .github
│   └── workflows           # GitHub Actions for deployment
│       └── gh-pages.yml
├── .gitignore              # Files to ignore in version control
├── package.json            # npm configuration file
└── README.md               # Project documentation
```

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Open `src/index.html` in your web browser to view the application.
4. Ensure you have a local server running if you want to test the application with JavaScript functionality.

## Features

- **Daily Doors**: Each day from December 1st to December 24th has its own door with a unique video and riddle.
- **Menu Navigation**: A menu component allows users to easily access any day's door.
- **Responsive Design**: The application is designed to be responsive and user-friendly.

## Deployment

This application is hosted on GitHub Pages. Changes pushed to the main branch will automatically deploy the latest version of the application.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.