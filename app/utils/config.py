from os import getenv
from dotenv import load_dotenv
load_dotenv(verbose=True)

class Config(object): 
  SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
  SQLALCHEMY_TRACK_MODIFICATIONS = getenv("SQLALCHEMY_TRACK_MODIFICATIONS")