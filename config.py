from redis import StrictRedis
class Config:
    DEBUG = None


# 定义开发模式的配置
class developmentConfig(Config):
    DEBUG = True
    # 设置密钥
    SECRET_KEY = 'clwy.cn'  # 此处密钥是随便填的，正式项目请自行生成
    # 配置数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/cms'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis连接信息，实现状态保持，存储用户的session信息
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 签名
    PERMANENT_SESSION_LIFETIME = 86400  # 设置session过期时间




# 定义生产模式的配置
class productionConfig(Config):
    DEBUG = False


# 定义字典，方便取值
config = {
    'development': developmentConfig,
    'production': productionConfig
}



