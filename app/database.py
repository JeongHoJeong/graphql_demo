import json

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

config = json.load(open('config.json'))

db_cfg = config['database']

db_user = db_cfg['user']
db_pwd = db_cfg['password']
db_host = db_cfg['host']
db_name = db_cfg['name']

engine = create_engine(
    f'postgresql://{db_user}:{db_pwd}@{db_host}/{db_name}',
    echo=True,
)

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
)

Base = declarative_base()


def init_db():
    from app.models import User, Post

    data = json.load(open('initial_data.json'))

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    users = data['users']

    for user in users:
        new_user = User(
            name=user.get('name'),
            birthdate=user.get('birthdate', None),
        )

        db_session.add(new_user)
        db_session.flush()
        db_session.refresh(new_user)

        if 'posts' in user:
            for post in user['posts']:
                new_post = Post(
                    author_id=new_user.id,
                    title=post.get('title'),
                    content=post.get('content'),
                )

                db_session.add(new_post)

    db_session.commit()
