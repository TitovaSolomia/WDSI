from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/quantity", methods=["POST"])
@cross_origin()
def process_quantity():
    data = request.json
    quantity = data.get("quantity")
    duration = data.get("duration")
    # Do something with the quantity here, like store it in a variable
    print(f"Received quantity from HTML: {quantity}, {duration}")
    return "Quantity received successfully"

if __name__ == "__main__":
    app.run(debug=True)