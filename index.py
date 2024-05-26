from flask import Flask,render_template,request
from flask_restful import Api, Resource
from youtube_transcript_api import YouTubeTranscriptApi
import json
import subprocess
import time

app= Flask(__name__)
app.use_static = True

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
      video_Id=request.form["video_Id"]
      try:
        x = YouTubeTranscriptApi.get_transcript(video_id=video_Id)
      except:
           return render_template('output.html',text=' Transcript not available for the given youtube ID')
      global text
      text = ' '.join([line['text'] for line in x])  
      return render_template('output.html', text=text)
           


     
     


if __name__== "__main__":
    app.run(debug=True)