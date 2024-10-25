from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
import re
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for flashing messages

# Function to extract video ID from URL
def get_video_id(url):
    video_id = re.sub(r'&t=.*', '', url.replace('https://www.youtube.com/watch?v=', ''))
    return video_id

# Fetch the transcript from the YouTube API
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return transcript
    except NoTranscriptFound:
        return None
    except TranscriptsDisabled:
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Format transcript for display
def format_transcript(transcript):
    output = ''
    if transcript:
        for entry in transcript:
            sentence = entry['text']
            output += f'{sentence}\n'
    return output

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the video URL from form input
        url = request.form['youtube_url']
        video_id = get_video_id(url)

        # Fetch transcript
        transcript = get_transcript(video_id)
        if transcript:
            transcript_text = format_transcript(transcript)
            # Save the transcript to a file
            save_transcript_to_file(transcript_text, video_id)
            flash('Transcript fetched successfully!', 'success')
            return render_template('index.html', transcript=transcript_text, video_id=video_id)
        else:
            flash('No transcript found for this video.', 'danger')
            return render_template('index.html')

    return render_template('index.html')

# Save transcript to a file
def save_transcript_to_file(transcript_text, video_id):
    file_name = f"transcript_{video_id}.txt"
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(transcript_text)
    except Exception as e:
        print(f"Failed to save transcript to file: {e}")

# Route to download the transcript file
@app.route('/download/<video_id>')
def download_file(video_id):
    file_name = f"transcript_{video_id}.txt"
    return send_file(file_name, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
