from uploaders.yt.upload_video import upload as yt_upload


def upload(config, path, title):
    if config["uploader"]["upload"] == False:
        print("Not uploading anywhere")
        return False

    if config["uploader"]["youtube"]["upload"] == True:
        yt(config, path, title)

def yt(config, path, title):
    print("Uploading to YouTube...")
    description = config["uploader"]["youtube"]["description"]
    category = config["uploader"]["youtube"]["category"]
    keywords = config["uploader"]["youtube"]["keywords"]
    privacyStatus = config["uploader"]["youtube"]["privacyStatus"]
    madeForKids = config["uploader"]["youtube"]["madeForKids"]
    id = yt_upload(config, path, title, description, category, keywords, privacyStatus, madeForKids)
    if id:
        print(f"https://www.youtube.com/watch?v={id}")
    else: 
        print("Unsuccessfully uploaded to YouTube!")