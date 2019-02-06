# This module transforms records from a csv file into a sqlite database
# using pure (as opposed to flask_sqlalchemy which will be used at
# next step) SQLAlchemy orm to create the database

import csv
import os

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine("sqlite:///ca.db")
Base = declarative_base()

# sqlalchemy class needs to inherit from declarative_base


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    population = Column(Integer)
    province_id = Column(Integer,
                         ForeignKey("provinces.id"),
                         nullable=False)

    def __repr__(self):
        return f"""<City(name={self.name}, 
                population={self.population}, 
                province_id={self.province_id})>"""


class Province(Base):
    __tablename__ = "provinces"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    cities = relationship("City", backref="province")

    def __repr__(self):
        return f"Province(name={self.name})"


Base.metadata.create_all(engine)  # create sqlalchemy schema
Session = sessionmaker(bind=engine)
session = Session()

file_path = 'ca.csv'  # csv file is placed on the same directory

if os.path.isfile(file_path):
    with open(file_path, 'r', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')

        # make a set of already existing rows in Province table
        prov_set = set(
            [item.name for item in session.query(Province).all()]
        )
        # if province does not exist already, add it to database
        for line in reader:
            if line['admin'] not in prov_set:
                prov_set.add(line['admin'])
                province = Province(name=line['admin'])
                session.add(province)
        session.commit()

    # create reader object again to populate database city table
    with open(file_path, 'r', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for line in reader:
            city = City(name=line['city'],
                        population=line['population'],
                        province_id=session.query(Province).
                        filter_by(name=line['admin']).one().id)
            session.add(city)
        session.commit()
