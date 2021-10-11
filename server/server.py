# import pickle
# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit
# import cv2
# import numpy as np
# import base64
# import pickle
# import random
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# # counter=0
# socketio = SocketIO(app)
# def on_aaa_response(args):
#     print('on_aaa_response', args['data']) #D:\gil\client_server_socket\client\client.py
# @socketio.on('connected')
# def test_connect(args):
#     # global counter
#     # counter+=1
#     print(args['counter'])
#     data=args['data']
#     jpg_original=base64.b64decode(data)
#     jpg_as_np=np.frombuffer(jpg_original,dtype=np.uint8)
#     img=cv2.imdecode(jpg_as_np,flags=1)
#     cv2.imwrite("output.jpg",img)

# if __name__ == '__main__':
#     socketio.run(app, port=8000)



# import socketio

# sio = socketio.Server()
# app = socketio.WSGIApp(sio)


# @sio.event
# def connect(sid, environ):
#     print(sid, 'connected')


# @sio.event
# def disconnect(sid):
#     print(sid, 'disconnected')

# import eventlet
# import socketio

# sio = socketio.Server()
# app = socketio.WSGIApp(sio)

# @sio.event
# def connect(sid, environ):
#     print('connect ', sid)

# @sio.event
# def message(sid, data):
#     print('message ', data['response'])

# @sio.event
# def disconnect(sid):
#     print('disconnect ', sid)

# if __name__ == '__main__':
#     eventlet.wsgi.server(eventlet.listen(('192.168.18.207', 8080)), app)

# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit

# # Creating a flask app and using it to instantiate a socket object
# app = Flask(__name__)
# socketio = SocketIO(app)

# # values['slider1'] and values['slider2'] store the current value of the sliders
# # This is done to prevent data loss on page reload by client.
# values = {
#     'slider1': 25,
#     'slider2': 0,
# }

# # Handler for default flask route
# # Using jinja template to render html along with slider value as input
# @app.route('/')
# def index():
#     return "render_template('index.html',**values)"

# # Handler for a message recieved over 'connect' channel
# @socketio.on('connect')
# def test_connect():
#     print("hello")
#     emit('after connect',  {'data':'Lets dance'})
# @socketio.on('message')
# def message(data):
#     print("server printing :",data)
#     emit('returns',  {'data':'Lets dance'})

# # Notice how socketio.run takes care of app instantiation as well.
# if __name__ == '__main__':
#     socketio.run(app, host='192.168.18.207',port=8080)

# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# @socketio.on('aaa')
# def test_connect():
#     print("Welcome, aaa received")
#     emit('aaa_response', {'data': 'Server'})

# if __name__ == '__main__':
#     socketio.run(app, port=8000)



#Server.py
# from flask import Flask, render_template, request, jsonify
# from flask_socketio import SocketIO,emit
# app = Flask(__name__)
# # app.config['SECRET_KEY'] = "Social Distance Secret"
# socket_app = SocketIO(app)


# @socket_app.on('connected')
# def handle_id(data):
#     print("server")
#     print(data)
#     print(request.sid)
#     emit('message', {"Data": "Device_id"})

# if __name__ == '__main__':
#     socket_app.run(app, debug=True, host='127.0.0.1', port=3000)

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import base64
import cv2    
import numpy as np
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    print("html")
    return "hello html"
# @socketio.
@socketio.event
def connect(sid):
    print("connection successful")
    print("sid server ",sid)
    # emit('message_to_client',d="hellos",to=sid)

@socketio.event
def message(data):
    print("message server recieved",data['sid'])
    img=data['frame']
    jpg_original=base64.b64decode(img)
    jpg_as_np=np.frombuffer(jpg_original,dtype=np.uint8)
    cv2.imshow('my',jpg_as_np)
    if cv2.waitKey(1) & 0xFF == 27:
        # break
        cv2.destroyAllWindows()
    # img=cv2.imdecode(jpg_as_np,flags=1)
    # emit('message_to_client',data=data)

if __name__ == '__main__':
    socketio.run(app,debug=True, host='127.0.0.1', port=5000)



# from flask import Flask
# from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# @socketio.on('connect')
# def test_connect():
#     print('connected')


# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')

# @socketio.on('message')
# def handle_message(msg):
#     print('Recieved',msg)

# @socketio.on('json')
# def handle_json(json):
#     print(str(json))

# if __name__ == '__main__':
#     socketio.run(app,debug=True)




# from flask import Flask
# from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# @socketio.on('connect')
# def test_connect():
#     print('connected')


# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')

# @socketio.on('message')
# def handle_message(msg):
#     print('Recieved',msg)

# @socketio.on('json')
# def handle_json(json):
#     print(str(json))

# if __name__ == '__main__':
#     socketio.run(app,debug=True)



# from flask import Flask
# from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# @socketio.on('connect')
# def test_connect():
#     print('connected')


# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')

# @socketio.on('message')
# def handle_message(msg):
#     print('Recieved',msg)

# @socketio.on('json')
# def handle_json(json):
#     print(str(json))

# if __name__ == '__main__':
#     socketio.run(app,debug=True,host='127.0.0.1',port=5000)

# from aiohttp import web
# import socketio

# sio = socketio.AsyncServer()
# app = web.Application()
# sio.attach(app)

# async def index(request):
#     """Serve the client-side application."""
#     with open('index.html') as f:
#         return web.Response(text=f.read(), content_type='text/html')

# @sio.event
# def connect(sid, environ):
#     print("connect ", sid)

# @sio.event
# async def chat_message(sid, data):
#     print("message ", data)
#     await sio.emit('reply', room=sid)

# @sio.event
# def disconnect(sid):
#     print('disconnect ', sid)

# # app.router.add_static('/static', 'static')
# # app.router.add_get('/', index)

# if __name__ == '__main__':
#     web.run_app(app,host='192.168.18.207')