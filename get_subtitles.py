from youtube_transcript_api import YouTubeTranscriptApi

video_id = '7zC8-06198g'  # ← Thay bằng ID video YouTube bạn muốn

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    with open("subtitles.txt", "w", encoding="utf-8") as f:
        for entry in transcript:
            start = entry['start']
            duration = entry['duration']
            text = entry['text']
            f.write(f"{start:.2f} --> {start+duration:.2f}\n{text}\n\n")

    print("✅ Đã lưu phụ đề vào file subtitles.txt")

except Exception as e:
    print("❌ Lỗi:", str(e))
