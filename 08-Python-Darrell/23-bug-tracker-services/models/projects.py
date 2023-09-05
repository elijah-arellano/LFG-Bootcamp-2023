from db import db
from datetime import datetime
class ProjectModel(db.Model):

    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(255))
    start_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.today())

    def __repr__(self):
        return '<Project %r>' % self.title

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'desc' : self.desc,
            'start_date': self.start_date,
            'created_at': self.created_at
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
