from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os,sys


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing our Custome Exception file....")
    except Exception as e:
        test = CustomException(e,sys)
        logging.info(test.error_message)
        return "Success Analytics Project Bootcamp batch"

if __name__ == '__main__':
    app.run(debug=True)
