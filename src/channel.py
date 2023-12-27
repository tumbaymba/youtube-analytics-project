import json
import os
from googleapiclient.discovery import build


class Channel:
    """ Класс для ютуб канала """
    API_KEY: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    #print(os.getenv('API_KEY'))

    def __init__(self, channel_id: str) -> None:
        """ Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API. """
        self.channel = None
        self.__channel_id = channel_id
        #self.youtube.channels().list(id=channel_id, part='snippets, statistics').execute()
    def print_info(self) -> None:
        """ Выводит в консоль информацию о канале """
        print(json.dumps(self.channel))
    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, channel_id=None):
        if channel_id == None:
            self.__channel_id