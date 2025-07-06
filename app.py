from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import re

app = Flask(__name__)

def extract_video_id(url):
    """
    Trích xuất video ID từ link YouTube.
    """
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    return match.group(1) if match else None

@app.route('/transcript', methods=['GET'])
def get_transcript():
    youtube_url = request.args.get('url')
    
    if not youtube_url:
        return jsonify({"error": "Thiếu tham số ?url="}), 400

    video_id = extract_video_id(youtube_url)
    if not video_id:
        return jsonify({"error": "Không thể lấy video_id từ URL"}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # Chỉ lấy phần text và thời gian
        result = [
            {
                "start": round(entry['start'], 2),
                "duration": round(entry['duration'], 2),
                "text": entry['text']
            } for entry in transcript
        ]
        return jsonify({"video_id": video_id, "transcript": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
