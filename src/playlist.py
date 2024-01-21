import os
from datetime import timedelta

import isodate
from googleapiclient.discovery import build


class PlayList:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        playlist_info = self.get_service().playlists().list(id=self.playlist_id,
                                                            part='snippet',
                                                            ).execute()
        self.title = playlist_info['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def get_video_response(self):

        playlist_videos = self.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                                  part='contentDetails', maxResults=50).execute()
        video_ids: list[str] = [video['contentDetails']['videoId']
                                for video in playlist_videos['items']]
        video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                                          id=','.join(video_ids)).execute()
        return video_response

    @property
    def total_duration(self):
        video_response = self.get_video_response()
        duration = timedelta()
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration += isodate.parse_duration(iso_8601_duration)
        return duration

    def show_best_video(self):
        video_response = self.get_video_response()
        max_likes = 0
        video_id = ''
        for video in video_response['items']:
            like_count = int(video['statistics']['likeCount'])
            if like_count > max_likes:
                max_likes = like_count
                video_id = video['id']

        return f'https://youtu.be/{video_id}'
pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')

print(pl.total_duration)
#duration = pl.total_duration
#print(duration)
#print(str(duration))
print(pl.show_best_video())