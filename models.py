from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, 
                    primary_key=True, 
                    autoincrement=True)
    
    name = db.Column(db.Text, 
                    nullable=False)
    
    species = db.Column(db.Text,
                        nullable=False)
    
    photo_url = db.Column(db.Text,
                            default='https://thumbs.dreamstime.com/b/no-image-available-icon-flat-vector-no-image-available-icon-flat-vector-illustration-132482953.jpg')

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean,
                            nullable=False,
                            default=True)
    
    def __repr__(self):
        return f"<Pet {self.id} Name={self.name} Age={self.age} Species={self.species} Photo Url={self.photo_url} Notes={self.notes} Available={self.available}>"