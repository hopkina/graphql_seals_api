from main import db


class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x_coord = db.Column(db.Integer)
    y_coord = db.Column(db.Integer)
    description = db.Column(db.String)
    date_updated = db.Column(db.Date)

    def to_dict(self):
        return {
            "id": self.id,
            "x_coord": self.x_coord,
            "y_coord": self.y_coord,
            "description": self.description,
            "date_updated": str(self.date_updated.strftime('%d-%m-%Y'))
        }
