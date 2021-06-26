from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Songs(Resource):

    def get(self):
        return {
            'songs': [
                {
                    'artist': 'Belmondawg',
                    'song_title': 'Followup',
                    'file format': 'mp4',
                    'album': 'Followup',
                    'year': '2021',
                    'duration': '2:30'
                },

                {
                    'artist': 'Rasmenatlism',
                    'song_title': 'Dobra muzyka',
                    'file format': 'mp3',
                    'album': 'Za młodzi na Heroda',
                    'year': '2012',
                    'duration': '3:46'
                },

                {
                    'artist': 'Juan Pablo',
                    'song_title': 'Inba Trwa',
                    'file format': 'wav',
                    'album': 'Nieznany',
                    'year': '2006',
                    'duration': '2:13'
                }
            ]
        }


api.add_resource(Songs, '/')

if __name__ == '__main__':
    app.run(debug=True)
