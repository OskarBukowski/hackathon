import datetime as dt

from marshmallow import Schema, fields


class Tweet:
    def __init__(self, id, amount, type):
        self.id = id


    def __repr__(self):
        return '<Transaction(id={self.id!r})>'.format(self=self)

    # output without !r -- > <Transaction(name=Ticker)>
    # output with !r -- > <Transaction(name='Ticker')>  ---> makes the description string


class TweetSchema(Schema):
    id = fields.Int()
