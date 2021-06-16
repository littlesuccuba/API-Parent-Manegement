import hashlib
import os
from manageAPI import settings


class UploadFilesReName():
    def rename(instans, filename):
        # 
        base_dir = settings.MEDIA_ROOT + '\\' + 'ChildImg\\'
        print(base_dir)
        path = base_dir + instans.childID + '\\'
        print(path)
        if not os.path.exists(path):
            os.makedirs(path)
        obj = {
            "id": instans.childID,
        }
        ext = filename.split('.')[-1]
        data = str(obj)
        hash = hashlib.sha256()
        hash.update(data.encode())
        result = hash.hexdigest() + '.' + ext
        media_base_dir = 'ChildImg/' + instans.childID + '/'
        return media_base_dir + result
