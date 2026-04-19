from app.main import app

# Vercel requires the handler to be named correctly
def handler(request):
    return app
