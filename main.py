from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes})"



video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument('views', type=int, help="Views of the video", required=True)
video_put_args.add_argument('likes', type=int, help="Likes on the video", required=True)


video_patch_args = reqparse.RequestParser()
video_patch_args.add_argument("name", type=str, help="Views of the video")
video_patch_args.add_argument('views', type=int, help="Views of the video")
video_patch_args.add_argument('likes', type=int, help="Likes on the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        video = VideoModel.query.filter_by(id=video_id).first()
        if not video:
            abort(404, message="Could not find video with that id")
        return video
    

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        if video:
            abort(409, message='Video id taken!')
        db.session.add(video)
        db.session.commit()
        return video, 201
    

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_patch_args.parse_args()
        video = VideoModel.query.filter_by(id=video_id).first()

        if not video:
            abort(404, message="Video does not exist!")

        if args['name']:
            video.name = args['name']
        if args['views']:
            video.views = args['views']
        if args['likes']:
            video.likes = args['likes']
        
        db.session.commit()
        return video, 200


    def delete(self, video_id):
        video = VideoModel.query.get(id=video_id)
        db.session.delete(video)
        db.session.commit()
        return '', 204
        

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
