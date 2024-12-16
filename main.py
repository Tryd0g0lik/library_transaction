import asyncio
from project.apps import app_ as app
import project.views
async def main():
    app.run(debug=False)
    return app

if __name__ == "__main__":
    asyncio.run(main())