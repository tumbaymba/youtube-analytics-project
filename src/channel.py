import json
import os

from googleapiclient.discovery import build


class Channel:
    """ Класс для ютуб канала """
    API_KEY: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet, statistics').execute()

    def print_info(self) -> None:
        print(json.dumps(self.channel))

    @classmethod
    def get_service(cls):
        api_key = os.getenv('API_KEY')
        return build("youtube", "v3", developerKey=api_key)

    def to_json(self, filename):
        data = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "link": self.url,
            "subscribers": self.subscribers,
            "video_count": self.video_count,
            "view_count": self.view_count
        }

        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent=2)
