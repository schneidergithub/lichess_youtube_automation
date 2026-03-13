
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload(video_path, title):

    youtube = build("youtube","v3")

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet":{
                "title":title,
                "description":"Daily chess puzzle from Lichess.",
                "tags":["chess","lichess","tactics"],
                "categoryId":"22"
            },
            "status":{"privacyStatus":"public"}
        },
        media_body=MediaFileUpload(video_path)
    )

    request.execute()
