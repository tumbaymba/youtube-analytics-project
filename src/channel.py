import json
import os

from googleapiclient.discovery import build

class Channel:

    API_KEY: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        youtube_channel = 'https://www.youtube.com/channel/'
        self.channel_id = channel_id
        self.channel_title: str = self.snippet['title']
        self.channel_description: str = self.snippet['description']
        self.channel_url: str = youtube_channel + self.channel_id
        self.channel_subs: int = self.to_int(self.statistics['subscriberCount'])
        self.channel_total_video: int = self.to_int(self.statistics['videoCount'])
        self.channel_total_views = self.to_int(self.statistics['viewCount'])


    def print_info(self) -> None:

        self.print_dict(self.channel_info)

    @property
    def channel_info(self) -> dict:

        result: dict = self.youtube.channels().list(part='snippet,statistics', id=self.channel_id).execute()
        return result['items'][0]

    @staticmethod
    def print_dict(dict_to_print: dict) -> None:

        print(json.dumps(dict_to_print, indent=2))

    @classmethod
    def get_service(cls) -> object:

        return cls.youtube


    @property
    def title(self) -> str:

        return self.channel_title

    @property
    def description(self) -> str:

        return self.channel_description

    @property
    def url(self) -> str:

        return self.channel_url

    @property
    def subscribers(self) -> int:

        return self.channel_subs

    @property
    def video_count(self) -> int:

        return self.channel_total_video

    @property
    def views(self) -> int:

        return self.channel_total_views

    def to_json(self, file_title: str) -> None:

        data = {
            "id": self.channel_id,
            "title": self.channel_title,
            "description": self.channel_description,
            "url": self.channel_url,
            "subscriberCount": self.channel_subs,
            "videoCount": self.channel_total_video,
            "viewCount": self.channel_total_views
        }

        with open(file_title, 'w', encoding='utf-8') as filename: json.dump(data, filename, indent=2)

    @staticmethod
    def to_int(string_num: str) -> int:

        return int(float(string_num))

    @property
    def snippet(self) -> dict:

        return self.channel_info['snippet']

    @property
    def statistics(self) -> dict:

        return self.channel_info['statistics']

    def __repr__(self) -> str:

        return f"{self.channel_id}"

