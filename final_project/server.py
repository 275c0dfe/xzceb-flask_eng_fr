from machinetranslation import translator
from flask import Flask, render_template, request , make_response
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')

    if(textToTranslate == ""):
        return make_response("Error No Input" , 400)

    translated = translator.englishToFrench(textToTranslate)
    
    #if "error" in translated.lower():
    #    return make_response(translated , 500)

    return make_response(translated , 200)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    if(textToTranslate == ""):
        return make_response("Error No Input" , 400)

    translated = translator.frenchToEnglish(textToTranslate)
    
    #if "error" in translated.lower():
    #    return make_response(translated , 500)

    return make_response(translated , 200)

@app.route("/")
def renderIndexPage():
    return make_response(render_template("index.html") , 200)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
