from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Province(db.Model):
    __tablename__ = "provinces"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    cities = db.relationship("City", backref="province", lazy=True)

    def __repr__(self):
        return f"Province(name={self.name})"


class City(db.Model):
    __tablename__ = "cities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    population = db.Column(db.Integer)
    province_id = db.Column(db.Integer,
                            db.ForeignKey("provinces.id"),
                            nullable=False)

    def __repr__(self):
        return f"""<City(name={self.name}, 
                population={self.population}, 
                province_id={self.id})>"""