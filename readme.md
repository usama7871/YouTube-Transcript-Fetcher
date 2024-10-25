### README for **YouTube Transcript Fetcher**

---

## Project Overview

**YouTube Transcript Fetcher** is a Flask-based web application that allows users to extract and download the transcript of any YouTube video. The application uses the `youtube-transcript-api` Python library to fetch transcripts and provides functionality for both manual and auto-generated transcripts in various languages.

---

## Features

- Fetch transcript of a YouTube video by entering its URL.
- Supports both manual and auto-generated transcripts.
- Display the fetched transcript on the webpage.
- Download the transcript as a `.txt` file.
- Copy transcript text to the clipboard with a single click.
- Simple, modern, and user-friendly UI.

---

## Project Structure

```plaintext
.
├── app.py                # The main Flask application file
├── templates/
│   └── index.html        # HTML template for the frontend
├── static/
│   ├── style.css         # CSS file for styling the webpage
├── requirements.txt      # List of required Python packages
└── README.md             # This README file
```

---

## Requirements

To run this project, you need to have **Python** installed along with the following Python packages:

- Flask
- YouTube Transcript API (`youtube-transcript-api`)

These packages can be installed using `pip` with the following command:

```bash
pip install -r requirements.txt
```

---

## Installation and Setup

1. **Clone the Repository**

   First, clone this repository to your local machine:

   ```bash
   git clone https://github.com/usama7871/YouTube-Transcript-Fetcher.git
   cd Youtube-Transcript-Fetcher
   ```

2. **Create a Virtual Environment** *(Optional but recommended)*

   Create a virtual environment to isolate the dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install all required dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application**

   Start the Flask server by running:

   ```bash
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

---

## How to Use

1. **Enter the YouTube Video URL**: On the homepage, there is an input box where you can enter the URL of the YouTube video.

2. **Fetch the Transcript**: After submitting the URL, the application will attempt to retrieve the transcript. If available, it will display the transcript on the same page.

3. **Copy or Download Transcript**:
    - Click on the "Copy Transcript" button to copy the transcript to your clipboard.
    - Click on the "Download Transcript" link to save the transcript as a `.txt` file.

---

## Error Handling

- If no transcript is found, the application will notify the user that no transcript is available.
- If transcripts are disabled for a video, the user will also be notified.
- The app handles various exceptions and provides feedback for different types of issues (e.g., invalid URLs, transcripts disabled, etc.).

---

## Customization

- **Styling**: You can modify the `static/style.css` file to change the appearance of the app, add more animations, or implement custom themes.
- **Templates**: To adjust the structure of the HTML, edit the `templates/index.html` file.

---

## Future Enhancements

- Add support for more languages and allow users to choose the language of the transcript.
- Implement a search history feature so users can retrieve past transcripts.
- Allow transcript formatting options (e.g., timestamp removal or text-only mode).

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute as needed.

---

## Author

- **Usama-M Abdullah**  
  Feel free to contact me via [kusamakhan1234@@gmail.com] for any questions or suggestions.  
  GitHub: [usama7871](https://github.com/usama7871)

---

### Thank you for using YouTube Transcript Fetcher!
