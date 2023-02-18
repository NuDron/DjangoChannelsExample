# DjangoChannelsExample

PYTHON VERSION: 3.11.2

Please note that I use [DJANGO v4]

# 1) Install Project

Install all necessary Python libraries.
```
pip install -r requirements.txt
```

To run the project as ASGI application:
```
python -m uvicorn DjangoCore.asgi:application
```

HINT: In case that your Uvicorn development server tells you there's no WebSocket support try following:
```
pip install 'uvicorn[standard]'
```

# 2) How to check if it works?

Start the Uvicorn server and head to http://127.0.0.1:8000/ -> then R-Click in your browser and view console.
You should see message like this:
```
Received:  
    {type: 'connection_established', message: 'You are now connected'}
    message: "You are now connected"
    type: "connection_established"
    [[Prototype]]: Object
```
This is a generic response from ChatConsumer.connect() method (see chat.consumers.py -> ChatConsumer class).