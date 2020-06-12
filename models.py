from sqlalchemy import Column, String, Integer, Float
from flask_sqlalchemy import SQLAlchemy

database_path = "postgres://hlfqgnttcnktiz:da37928c7375f60206a5524585b7708d168e902561d993b10860a9e54a5cc3c4@ec2-34-202-88-122.compute-1.amazonaws.com:5432/d7bgv2q367s97t"

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Anime
a persistent anime entity, extends the base SQLAlchemy Model
'''
class Anime(db.Model):
    __tablename__ = 'animes'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    image_url = Column(String)
    mal_url = Column(String)
    score = Column(Float)
    rank = Column(Integer)

    def __init__(self, title, image_url, mal_url, score, rank):
        self.title = title
        self.image_url = image_url
        self.mal_url = mal_url
        self.score = score
        self.rank = rank

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'image_url': self.image_url,
            'mal_url': self.mal_url,
            'score': self.score,
            'rank': self.rank
        }
