from aiohttp import web
import os

# Path to the directory where the static files are located
static_dir = os.getcwd()

async def handle(request):
    filename = request.match_info.get('filename', 'index.html')
    filepath = os.path.join(static_dir, filename)
    
    if not os.path.isfile(filepath):
        return web.Response(status=404, text="File not found")

    return web.FileResponse(filepath)

app = web.Application()
app.router.add_get('/{filename:.*}', handle)  # Match any filename
app.router.add_get('/', handle)  # Handle root path

if __name__ == '__main__':
    web.run_app(app, port=8080)
