from sqlalchemy import create_engine


class DbConnection:
    def __init__(self, db_url: str):
        self.db_url = db_url

    def connect(self):
        return create_engine(self.db_url)
    
