from flask import Flask, Response

app = Flask(__name__)

# هنا يمكنك وضع روابط البث الخاصة بك (مثلاً روابط M3U8 أو روابط قنوات مجانية)
# يمكنك تعديل أسماء القنوات والروابط بالشيء الذي تحبه
playlist_content = """#EXTM3U
#EXTINF:-1 tvg-name="Channel 1",قناتي الأولى
https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4
#EXTINF:-1 tvg-name="Channel 2",قناتي الثانية
https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4
"""

@app.route('/')
def home():
    return "IPTV Server is Running! Use /playlist.m3u to get your list."

@app.route('/playlist.m3u')
def playlist():
    # إرجاع ملف M3U للأجهزة والتطبيقات
    return Response(playlist_content, mimetype='audio/x-mpegurl')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
