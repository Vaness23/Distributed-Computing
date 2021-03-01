from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class Post(DeclarativeBase):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    url = Column('url', String)

    #def __repr__(self):
        #return "".format(self.code)


from sqlalchemy.orm import sessionmaker

def main():
    engine = create_engine('postgres://postgres:1@localhost:5432/data')
    #DeclarativeBase.metadata.create_all(engine)
    #Session = sessionmaker(bind=engine)
    #session = Session()
    #new_post = Post(name='Two record', url="http://testsite.ru")
    #session.add(new_post)
    #session.commit()

    #for post in session.query(Post):
        #print(post)
    
    #from sqlalchemy import inspect

    #inspector = inspect(engine)
    #print(inspector.get_columns('posts'))

    with engine.connect() as con:
        rs = con.execute('SELECT * FROM "posts";')

        for row in rs:
            print(row)

if __name__ == "__main__":
    main()