from app import app, socketio

if __name__ == "__main__":
  socketio.run(app)

# Gunicorn and WSGI (Web Server Gateway Interface) are both components used in deploying and serving Python web applications, particularly those built with web frameworks like Flask and Django.