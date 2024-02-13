from core import translate, load_model
from flask import Flask, Response, render_template, request, current_app

app = Flask(__name__)

MODEL_DIR = '.'

# load our model globally
app.model = load_model(".")


@app.route("/")
def index():
    return render_template('index.html', predict=False)


@app.route("/translate", methods=['POST'])
def translate_api():
    """
    The main API for translation.
    Accepts a prompt in Siswati, then use our trained model to translate it to English.
    """

    if request.method == 'POST':
        _postData: dict = request.json
        prompt = _postData.get('prompt')

        try:
            response = translate(prompt, **current_app.model)
            return {
                'answer': str(response)
            }
        except Exception as error:
            return Response(f"Error: Internal error, failed to translate. Reason: {str(error)}", status=400)

    # if not post, return an error
    return Response(f"Error: Method not allowed. Can only process POST requests.", status=400)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
