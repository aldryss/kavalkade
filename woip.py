from minicli import cli, run


def kavalkade_web():
    from src.kavalkade import Kavalkade
    from tinydb import TinyDB
    return Kavalkade(
        database=TinyDB('./data/kavalkade.json')
    )


@cli
def http(debug: bool = False):
    import asyncio
    from aiowsgi import create_server

    app = create_web_app()

    loop = asyncio.new_event_loop()
    wsgi_server = create_server(app, loop=loop, port=8000)

    try:
        wsgi_server.run()
    finally:
        loop.stop()


if __name__ == '__main__':
    run()