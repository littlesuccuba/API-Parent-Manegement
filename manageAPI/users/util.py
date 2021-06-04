import hashlib
import os
from manageAPI import settings


# 自定义jwt登陆成功后返回的数据格式
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'id': user.id,
        'username': user.username,
        'phone': user.phone_num,
        'identity': user.get_identity_display(),
        'name': user.name,
        'token': token,
    }

class UploadFilesReName():
    # 重命名文件
    def rename(instans, filename):
        # 从settings获取设置的媒体路径
        base_dir = settings.MEDIA_ROOT+'\\'+'avatar\\'
        # 在base_dir的基础上拼接用户名
        path = base_dir+instans.username+'\\'
        # 根据用户来创建文件夹，如果已存在则不创建
        if not os.path.exists(path):
            os.mkdir(path)
        # 获取instans内的用户id与用户名
        obj = {
            "id": instans.id,
            "username": instans.username
        }
        # 以 . 分割文件的后缀名
        ext = filename.split('.')[-1]
        # 自定义的instans字典转化为字符串类型
        data = str(obj)
        # 调用哈希对象的sha256算法
        hash = hashlib.sha256()
        # 对data进行编码
        hash.update(data.encode())
        # 将编码后的data进行加密后拼接上原先分离的后缀名
        result = hash.hexdigest()+ '.' + ext
        # 图片存储根路径
        media_base_dir = 'avatar/'+instans.username+'/'
        # 返回图片路径+加密后的文件名
        return media_base_dir + result
