import  os
class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://collo:collins@localhost/pitch'
    SECRET_KEY="colo"
class DevConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    pass

config_options={
'development':DevConfig,
"production":ProdConfig
}
