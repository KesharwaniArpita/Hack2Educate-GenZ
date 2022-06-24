from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
api_key = 'AIzaSyAP_o6qdI81Ox4XfLK-InGSBvkeZuz06Nc'

channel_ids = ['UCdxbhKxr8pyWTx1ExCSmJRw', # Girliyapa
               'UCCKjHsAIxvjtWG8KOcLuG8Q', # Alright!
               'UCgM1AQcoM5TRlzsm1e66vrQ', # Hasley India
               'UCNJcSUSzUeFm8W9P7UUlSeQ', # The Viral Fever
               'UCNyeSfUfffmJXwA2_tmNG9A' # The Screen Patti
              ]
channel_ids2 = [

]
youtube = build('youtube', 'v3', developerKey=api_key)
## Function to get channel stats

def get_channel_stats(youtube, channel_ids):
    all_data = []
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=','.join(channel_ids))
    response = request.execute() 
    
    for i in range(len(response['items'])):
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
                    Subscribers = response['items'][i]['statistics']['subscriberCount'],
                    Views = response['items'][i]['statistics']['viewCount'],
                    Total_videos = response['items'][i]['statistics']['videoCount'],
                    playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)
    
    return all_data
channel_statistics = get_channel_stats(youtube, channel_ids)
channel_data = pd.DataFrame(channel_statistics)
channel_data = pd.DataFrame(channel_statistics)
channel_data['Subscribers'] = pd.to_numeric(channel_data['Subscribers'])
channel_data['Views'] = pd.to_numeric(channel_data['Views'])
channel_data['Total_videos'] = pd.to_numeric(channel_data['Total_videos'])
channel_data.dtypes
sns.set(rc={'figure.figsize':(10,8)})
ax = sns.barplot(x='Channel_name', y='Subscribers', data=channel_data)
ax = sns.barplot(x='Channel_name', y='Views', data=channel_data)
ax = sns.barplot(x='Channel_name', y='Total_videos', data=channel_data)
channel_data
playlist_id = channel_data.loc[channel_data['Channel_name']=='Alright!', 'playlist_id'].iloc[0]
def get_video_ids(youtube, playlist_id):
    
    request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId = playlist_id,
                maxResults = 50)
    response = request.execute()
    
    video_ids = []
    
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
        
    next_page_token = response.get('nextPageToken')
    more_pages = True
    
    while more_pages:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                        part='contentDetails',
                        playlistId = playlist_id,
                        maxResults = 50,
                        pageToken = next_page_token)
            response = request.execute()
    
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            
            next_page_token = response.get('nextPageToken')
        
    return video_ids
video_ids = get_video_ids(youtube, playlist_id)
video_ids
## Function to get video details
def get_video_details(youtube, video_ids):
    all_video_stats = []
    
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
                    part='snippet,statistics',
                    id=','.join(video_ids[i:i+50]))
        response = request.execute()
        
        for video in response['items']:
            video_stats = dict(Title = video['snippet']['title'],
                               Published_date = video['snippet']['publishedAt'],
                               Views = video['statistics']['viewCount'],
                               Likes = video['statistics']['likeCount'],
                               Favorite = video['statistics']['favoriteCount'],
                               Comments = video['statistics']['commentCount']
                               )
            all_video_stats.append(video_stats)
            
    
    return all_video_stats
video_details = get_video_details(youtube, video_ids)
video_data = pd.DataFrame(video_details)
video_data['Published_date'] = pd.to_datetime(video_data['Published_date']).dt.date
video_data['Views'] = pd.to_numeric(video_data['Views'])
video_data['Likes'] = pd.to_numeric(video_data['Likes'])
video_data['Favorite'] = pd.to_numeric(video_data['Favorite'])
video_data['Views'] = pd.to_numeric(video_data['Views'])
video_data
top10_videos = video_data.sort_values(by='Views', ascending=False).head(10)
top10_videos
ax1 = sns.barplot(x='Views', y='Title', data=top10_videos)
video_data
video_data['Month'] = pd.to_datetime(video_data['Published_date']).dt.strftime('%b')
video_data
videos_per_month = video_data.groupby('Month', as_index=False).size()
videos_per_month
sort_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
videos_per_month.index = pd.CategoricalIndex(videos_per_month['Month'], categories=sort_order, ordered=True)
videos_per_month = videos_per_month.sort_index()
ax2 = sns.barplot(x='Month', y='size', data=videos_per_month)
video_data.to_csv('Video_Details(Girliyapa).csv')



