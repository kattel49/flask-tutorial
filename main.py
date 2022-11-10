from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
# base app for the api
api = Api(app)

# names = {"shubhushan": {"age": 22, "gender": "male"},
#          "miller": {"age": 25, "gender": "male"}}

# # restful enpoint implementation
# class HelloWorld(Resource):
#     # def get(self, name, number):
#     #     return jsonify({"data":"Hello World!", "name": name, "number": number})

#     def get(self, name):
#         return names[name]

#     def post(self):
#         return jsonify({"data": "Hello World!"})

    
# """
#     /helloworld => endpoint
#     <string:name> => type: string, param name: name
#     <int:number> => type: int, param name: number
# """
# #api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:number>")
# api.add_resource(HelloWorld, "/helloworld/<string:name>")

videos = {}

# validates request with required fields
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Number of likes on the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Number of views on the video is required", required=True)

class Video(Resource):
    def get(self, video_id):
        if video_id not in videos:
            abort(404, message="Video id is not valid")
        return videos[video_id], 200

    def put(self, video_id):
        if video_id in videos:
            abort(408, message="Video already exists with that id")
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
    def delete(self, video_id):
        if video_id not in videos:
            abort(404, message="Video id is not valid")
        del videos[video_id]
        return "", 204
        

api.add_resource(Video,"/video/<int:video_id>")


if __name__=="__main__":
    app.run(debug=True)