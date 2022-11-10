from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
# base app for the api
api = Api(app)

# restful enpoint implementation
class HelloWorld(Resource):
    def get(self, name, number):
        return jsonify({"data":"Hello World!", "name": name, "number": number})

    def post(self):
        return jsonify({"data": "Hello World!"})

    
"""
    /helloworld => endpoint
    <string:name> => type: string, param name: name
    <int:number> => type: int, param name: number
"""
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:number>")


if __name__=="__main__":
    app.run(debug=True)