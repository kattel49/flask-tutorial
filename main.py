from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# base app for the api
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={self.name}, views={self.views}, likes={self.likes})"

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

# validates request with required fields
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Number of likes on the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Number of views on the video is required", required=True)

# quick way to serialize an obj
def serialize_video(obj):
    name = obj.name
    views = obj.views
    likes = obj.likes

    return {"name": name, "views": views, "likes": likes}

# flask way of serializing objects
resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'views' : fields.Integer,
    'likes' : fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video")
        return result, 200
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="video id taken")
        video = VideoModel(id = video_id, name=args['name'], likes=args['likes'], views=args['views'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    def delete(self, video_id):
        result = VideoModel.query.get(id=video_id)
        
        

api.add_resource(Video,"/video/<int:video_id>")


if __name__=="__main__":
    app.run(debug=True)