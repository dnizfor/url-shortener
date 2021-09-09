from datetime import date
from enum import unique
from . import db


## Model



class Link(db.Model):
    id = db.Column(db.Integer , primary_key= True)
    long_url = db.Column(db.String, nullable = False )
    short_url = db.Column(db.String, nullable = False )
   

    def __init__(self,long_url,short_url):
        self.long_url = long_url
        self.short_url = short_url

    

    def __repr__(self) :
        return f'{self.long_url} {self.short_url} '





db.create_all()

