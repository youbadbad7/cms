from qiniu import Auth, put_data
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class MyStorage(FileSystemStorage):
    def _save(self, name, content):
        # 延续原方法的写法
        filename = name.replace('\\', '/')
        # 将文件传入封装好的对象里
        q = Qiniu()
        q.upload_stream(filename, content.file.getvalue())
        image_url = settings.QINIU_DOMIN_PREFIX + filename
        return image_url

class Qiniu():
    def __init__(self):
        self.access_key = settings.QINIU_ACCESS_KEY
        self.secret_key = settings.QINIU_SECRET_KEY
        # 要上传的空间
        self.bucket_name = settings.QINIU_BUCKET_NAME
        # 构建鉴权对象
        self.auth = Auth(self.access_key, self.secret_key)


    def get_token(self, key):
        """

        :param key: 文件名
        :return: 上传令牌
        """
        policy = {
            'scope': settings.QINIU_BUCKET_NAME,
            'mimeLimit': 'image/jpeg;image/png',
            'deadline': 3600
        }
        # 3600为token过期时间，秒为单位。3600等于一小时
        token = self.auth.upload_token(self.bucket_name, key, 3600, policy)
        return token


    def upload_stream(self, filename, stream_data):
        """

        :param filename: 文件名
        :param stream_data: 二进制数据
        :return: 无
        """
        # 上传后保存的文件名
        key = filename
        # 生成上传 Token，可以指定过期时间等
        token = self.auth.upload_token(self.bucket_name, key, 3600)
        # 要上传文件的本地路径
        # localfile = file_path
        ret, info = put_data(up_token=token, key=key, data=stream_data)
        assert ret['key'] == key
        # assert ret['hash'] == etag_stream(stream_data)