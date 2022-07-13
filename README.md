# lws_chat
How to run the application.
  1)you will need to have Redis server running
        docker run -p 6379:6379 -d redis:5
  2)run pip install requirements.txt
  3)then you can start the server with:
        python manage.py runserver
