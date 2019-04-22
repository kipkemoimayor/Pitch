import  os
class Config:
    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://collo:collins@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY="colo"

    #markdown configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://collo:collins@localhost/pitch'
    DEBUG=True

class ProdConfig(Config):
    pass
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://collo:collins@localhost/pitch_test'

config_options={
'development':DevConfig,
"production":ProdConfig,
'test':TestConfig
}
