# Flask - Grephene - SQLAlchemy - React - Relay Demo

- Grephene 2.x

# How to run the project
You need to setup your database before you go. First, create `config.json` with proper database information. (The database is always PostgreSQL.)

```json
{
    "database": {
        "host": "localhost",
        "user": "my_id",
        "password": "some_pwd",
        "name": "my_database"
    }
}
```

Next, prepare initial data with file `initial_data.json` like below.

```json
{
    "users": [
        {
            "name": "Monica",
            "posts": [
                {
                    "title": "Hello",
                    "content": "World"
                },
                {
                    "title": "Random Post",
                    "content": "Random Content"
                }
            ],
            "birthdate": "1988-10-20"
        },
        {
            "name": "Bob",
            "posts": [],
            "birthdate": "1999-9-4"
        },
        {
            "name": "Clare"
        }
    ]
}
```

If you're ready, install dependencies, build JavaScript assets, and run Flask server.

```bash
pip install -r requirements.txt
yarn install
yarn run build
python run.py --initialize
```

If you run `run.py` with `--initialize` flag, it will initialize the database addressed in `config.json` with `initial_data.json`.

Now check `localhost:5000` with your browser.

`localhost:5000/graphql` provides `graphiql` user interface which allows direct query to the GraphQL server.
