from flask import Flask, request
from flask_cors import CORS, cross_origin
from services.firstLevelService import generateFirstLevelPdf
from services.zeroLevelService import generateZeroLevelPdf
from services.secondLevelService import generateSecondLevelPdf

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

quantity = 0
duration = 0
supplies = 0
assemble = 0
tent_time = 0 
ordering = 0
component = 'component'

@app.route("/quantity", methods=["POST"])
@cross_origin()
def process_quantity():
    data = request.json

    global quantity
    quantity = data.get("quantity")
    
    global duration
    duration = data.get("duration")

    print(f"Received from HTML: {quantity}, {duration}")
    return "received successfully"


@app.route("/producent", methods=["POST"])
@cross_origin()
def producent():
    data = request.json

    global supplies
    supplies = data.get("supplies")

    global assemble
    assemble = data.get("assemble")

    global component
    component = data.get("component")

    # Do something with the quantity here, like store it in a variable
    print(f"Received from HTML: {supplies}, {assemble}, {component}")
    return "received successfully"


@app.route("/tent", methods=["POST"])
@cross_origin()
def add_tent_value():
    data = request.json

    global tent_time
    tent_time = data.get("tent")

    # Do something with the quantity here, like store it in a variable
    print(f"Received from HTML: {supplies}, {assemble}")
    return "received successfully"


#do secondlevel 
@app.route("/producent", methods=["POST"])
@cross_origin()
def producent2():
    data = request.json

    global supplies
    supplies = data.get("supplies")

    global assemble
    assemble = data.get("assemble")

    global component
    component = data.get("component")

    global ordering
    ordering = data.get("order")


    # Do something with the quantity here, like store it in a variable
    print(f"Received from HTML: {supplies}, {assemble}, {component}, {ordering}")
    return "received successfully"

@app.route("/exl", methods=["POST"])
@cross_origin()
def createEXL():
    data = request.json
    level = data.get("level")
    print("Is creating....")

    if level == 0 :
        generateZeroLevelPdf(quantity, duration, supplies, assemble)
    elif level == 1:
        generateFirstLevelPdf(quantity, duration, tent_time, supplies, assemble, component)
    elif level ==2:
        generateSecondLevelPdf(quantity, duration, tent_time, supplies, assemble, component, ordering)
    
    return


if __name__ == "__main__":
    app.run(debug=True)

