import asyncio
from project.apps import app_ as app

async def main():
    app.run(debug=False)
    return app

if __name__ == "__main__":
    asyncio.run(main())