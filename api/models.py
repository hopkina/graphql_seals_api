from main import db


class Site(db.Model):
    site_id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String)
    x_coord = db.Column(db.Integer)
    y_coord = db.Column(db.Integer)
    management_area = db.Column(db.String)
    seal_species = db.Column(db.String)
    comments = db.Column(db.String)
    date_from = db.Column(db.Date)

    def to_dict(self):
        return {
            "site_id": self.site_id,
            "site_name": self.site_name,
            "x_coord": self.x_coord,
            "y_coord": self.y_coord,
            "management_area": self.management_area,
            "seal_species": self.seal_species,
            "comments": self.comments,
            "date_from": str(self.date_from.strftime('%d-%m-%Y'))
        }
