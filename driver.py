import email
from turtle import st
from unicodedata import name


class Driver :
    id          = int
    name        = str
    document    = int
    email       = str
    password    = str

    def __init__(self, name, document, email, password):
        self.name       = name
        self.document   = document
        self.email      = email
        self.password   = password