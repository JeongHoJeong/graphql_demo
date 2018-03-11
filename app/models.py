from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('users_id_seq'), primary_key=True,
                nullable=False)
    name = Column(String)
    birthdate = Column(Date)

    def __repr__(self):
        return f'''<User(id={self.id}, name={self.name},
            birthdate={self.birthdate})>'''


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, Sequence('posts_id_seq'), primary_key=True)
    author_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String)
    content = Column(String)

    def __repr__(self):
        return f'''<Post(id={self.id}, author_id={self.author_id},
            title={self.title})>'''
