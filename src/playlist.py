import os
# from channel import Channel
from datetime import timedelta

from googleapiclient.discovery import build

api_key: str = os.getenv('API_KEY')
counter = 0


class PlayList:
    # api_key: str = os.getenv('API_KEY')

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.title = self.playlists_to_print()
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"

    @classmethod
    def get_service(cls):

        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def playlists_to_print(self):

        playlists = self.get_service().playlists().list(channelId='@moscowdjangoru', part='contentDetails,snippet')

    def get_video_response(self):

        playlist_videos = self.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                                  part='contentDetails', maxResults=50).execute()
        video_ids: list[str] = [video['contentDetails']['videoId']
                                for video in playlist_videos['items']]
        video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                                          id=','.join(video_ids)).execute()
        return video_response

    def get_duration(self):
        time_list = []
        counter1 = 0
        time = self.get_video_response()['items']
        for t in time:
            ratio = time[counter1]['contentDetails']['duration']
            time_list.append(ratio)
            counter1 += 1
        return time_list

    @property
    def total_duration(self):
        minutes = 0
        seconds = 0
        for z in self.get_duration():
            seconds += (z[5:7])
            minutes += (z[2:4])
            total_sec = minutes * 60 + seconds
            total_hours = int(total_sec / 3600)
            total_minutes = int((total_sec - total_hours * 3600) / 60)
            total_seconds = int(total_sec - total_hours * 3600 - total_minutes * 60)
            delta = timedelta(hours=total_hours, minutes=total_minutes, seconds=total_seconds)

        return delta

    def show_best_video(self):

        videos = self.get_video_response()['items']
        for v in videos:
            best_video = max((videos[counter]['statistics']['likeCount']), key=lambda i: int(i))

        return f"https://youtu.be/{v['id']}"


pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')


