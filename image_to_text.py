import easyocr
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def image_to_text_main(filename):
  reader = easyocr.Reader(['en'], gpu=False)
  results = reader.readtext(filename)
  text = ""

  for result in results:
      text += result[1] + " "

  return text