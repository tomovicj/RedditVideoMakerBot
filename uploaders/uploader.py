from uploaders.yt.upload_video import upload as yt_upload
# from uploaders.ig.upload_reel import upload as ig_upload
# from moviepy.editor import *
import requests


def upload(config, path, title):
    if config["uploader"]["upload"] == False:
        print("Not uploading anywhere")
        return False

    url = config["discord"]["webhook"]
    link = "none"

    #YT
    if config["uploader"]["youtube"]["upload"] == True:
        print("Uploading to YouTube...")
        id  = yt(config, path, title)
        if id:
            link = f"https://www.youtube.com/watch?v={id}"
            print("Successfully uploaded to YouTube!", link)
        else: 
            print("Unsuccessfully uploaded to YouTube!")
        
        if url:
            discord(url, id, "yt", link)

    # #IG
    # if config["uploader"]["instagram"]["upload"] == True:
    #     print("Uploading to Instagram...")
    #     id = ig_upload(config, path, title, get_thumbnail(path))
    #     if id:
    #         link = f"https://www.instagram.com/reel/{id}"
    #         print("Successfully uploaded to Instagram!", link) 
    #     else:
    #         print("Unsuccessfully uploaded to Instagram!")
        
    #     if url:
    #         discord(url, id, "ig", link)


def yt(config, path, title):
    description = config["uploader"]["youtube"]["description"]
    category = config["uploader"]["youtube"]["category"]
    keywords = config["uploader"]["youtube"]["keywords"]
    privacyStatus = config["uploader"]["youtube"]["privacyStatus"]
    madeForKids = config["uploader"]["youtube"]["madeForKids"]
    id = yt_upload(config, path, title, description, category, keywords, privacyStatus, madeForKids)
    return id


def discord(url: str, success, platform: str, link: str):  
    if success:
        success = "Successfully"
        color = 65280
    else:
        success = "Unsuccessfully"
        color = 16711680
        link = "none"

    if platform == "yt":
        platform = "Youtube"
        picture = "https://play-lh.googleusercontent.com/lMoItBgdPPVDJsNOVtP26EKHePkwBg-PkuY9NOrc-fumRtTFP4XhpUNk_22syN4Datc"
    # elif platform == "ig":
    #     platform = "Instagram"
    #     picture = "https://play-lh.googleusercontent.com/LM9vBt64KdRxLFRPMpNM6OvnGTGoUFSXYV-w-cGVeUxhgFWkCsfsPSJ5GYh7x9qKqw"
    
    obj = {
    "content": None,
    "embeds": [
        {
        "title": platform,
        "color": color,
        "fields": [
            {
            "name": success,
            "value": link
            }
        ],
        "thumbnail": {
            "url": picture
        }
        }
    ],
    "attachments": []
    } 

    x = requests.post(url, json = obj)

    if x.status_code != 204:
        print(f"Discord weebhook error: {x.status_code}")

# def get_thumbnail(path):
#     try:
#         clip = VideoFileClip(path)
#         # Saving a frame at 1 second
#         clip.save_frame(f"{path}.jpg", t = 1)
#     except:
#         return None
#     else:
#         return f"{path}.jpg"
