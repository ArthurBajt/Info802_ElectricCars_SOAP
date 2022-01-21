from .DataBase import db
from pymongo import ASCENDING, DESCENDING
from pymongo.database import Collection
from faker import Faker
from random import randrange


class ElectricCarsController(object):
    collection: Collection = db["ElectricCars"]

    @classmethod
    def get_all_electric_cars(cls) -> dict:
        res: dict = cls.collection.find({}, {'_id': False}).sort("year", DESCENDING)
        return {"data": res}


    @classmethod
    def generate_fake_cars(cls):
        fake: Faker = Faker()
        cls.collection.drop()
        for _ in range(1500):
            car: dict = {
                "name": fake.first_name() + " " + fake.bs(),
                "range": randrange(100, 1200, 5),
                "charge_time": randrange(60, 420, 5),
                "year":  randrange(2016, 2022),
                "maker": fake.company()
            }
            cls.collection.insert_one(car)
