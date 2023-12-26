import json
import os
from googleapiclient.discovery import build

class Channel:
    """ Класс для ютуб канала """
    API_KEY: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    #print(os.getenv('API_KEY'))

    def __init__(self, channel_id='UC-OVMPlMA3-YCIeg4z5z23A' ) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.youtube.channels.list(id=channel_id, part='snippet, statistics').execute()

    def print_info(self):
        """ Выводит в консоль информацию о канале """
        print(json.dumps(self.channel()))
