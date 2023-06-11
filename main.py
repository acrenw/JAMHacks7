from flask import Flask, render_template, redirect, request
from image_to_text import image_to_text_main
from bionic import bionic_main
from pdf_to_text import pdf_to_text_main
import assemblyai as aai

app = Flask(__name__)

@app.route("/")
def give_homepage():
	return redirect("/home")


@app.route("/home")
def home():
  return render_template("home.html")


@app.route("/submitted", methods=["POST"])
def the_main_function():
	uploaded_file = request.files["file"]
	path = uploaded_file.filename
	
	extension = path.split(".")[-1]

	if extension == "txt":
		str = open(path, "r").readlines()[0]
	
	elif extension == "jpeg" or extension == "jpg" or extension == "png":
		str = image_to_text_main(path)

	elif extension == "pdf":
		str = pdf_to_text_main(path)

	elif extension == "mp3" or extension == "mp4" or extension == "m4a":
		aai.settings.api_key = "c71f7aa61d274e9dae9c539c43e426f6"
		transcriber = aai.Transcriber()
		transcript = transcriber.transcribe(path)
		str = transcript.text

	else:
		str = "Sorry, your filetype is not supported yet."
	
	bp = bionic_main(str)
	
	return render_template("result.html", value=bp)


if __name__ == "__main__":
  #app.run(host="0.0.0.0",debug=True)
  app.run(debug=True)