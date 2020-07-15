import datetime
import os

from peewee import *
DATABASE_PATH = os.path.join(os.getcwd(), 'insta_auto_sub.db')
db = SqliteDatabase(DATABASE_PATH)

class BaseModel(Model):
    class Meta:
        database = db

class Historys(BaseModel):
    id = BigIntegerField(null=False, primary_key=True, column_name='ID')
    date_time = DateTimeField(null=True, column_name='date_time')
    user_name = TextField(null=True, column_name='user_name')
    insta_login = TextField(null=True, column_name='insta_login')

    class Meta:
        table_name = 'historys'

class Config(BaseModel):
    id = BigIntegerField(null=False, primary_key=True, column_name='ID')
    chrome_path = TextField(null=True, column_name='chrome_path')
    timeout = BigIntegerField(null=True, column_name='timeout')
    start_data_time = DateTimeField(null=True, column_name='start_data_time')
    stop_data_time = DateTimeField(null=True, column_name='stop_data_time')
    sheduled = BooleanField(null=True, column_name='sheduled')
    last_start_dt = DateTimeField(null=True, column_name='last_start_dt')
    class Meta:
        table_name = 'config'