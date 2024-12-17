import asyncio
from project.apps import app_ as app
from project.views import api_path
async def main():
    paths = asyncio.create_task(api_path())
    await paths
    app.run(debug=False)
    return app

if __name__ == "__main__":
    asyncio.run(main())