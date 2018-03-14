import argparse

from app import app

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--initialize', dest='initialize', action='store_const', const=True,
    )

    args = parser.parse_args()

    if args.initialize:
        from app.database import init_db
        init_db()

    app.debug = True
    app.run()
