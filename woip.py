from minicli import cli, run

def kavalkade_web():
    """Kavalkade web application"""
    from src.kavalkade import Kavalkade
    from src.kavalkade.controllers import router
    from src.kavalkade.controllers import main
    from tinydb import TinyDB
    return Kavalkade(
        database=TinyDB('./data/kavalkade.json'),
        router=router
    )


@cli
def http(debug: bool = False):
    import asyncio
    from aiowsgi import create_server

    app = kavalkade_web()
    loop = asyncio.new_event_loop()

    wsgi_server = create_server(app, loop=loop, port=8000)

    try:
        wsgi_server.run()
    finally:
        loop.stop()


if __name__ == '__main__':
    run()