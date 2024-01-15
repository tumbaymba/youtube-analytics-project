from src.channel import Channel


class Video(Channel):

    def __init__(self, video_id): #channel_id):

        #super().__init__(channel_id)
        self.video_id = video_id
        try:
            youtube = self.get_service()
            self.video = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=self.video_id).execute()
            self.channel_title = self.video['items'][0]['snippet']['title']
            self.channel_url = 'https://www.youtube.com/watch?v=' + self.video_id
            self.view_count = self.video['items'][0]['statistics']['viewCount']
            self.like_count = self.video['items'][0]['statistics']['likeCount']
        except IndexError:
            print('Non-existen ID')
            self.youtube = None
            self.channel_title = None
            self.channel_url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):

    def __init__(self, video_id, play_list_id):
        super().__init__(video_id)
        self.play_list_id = play_list_id
