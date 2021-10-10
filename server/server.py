# # from flask import Flask, render_template
# # from flask_socketio import SocketIO, emit

# # app = Flask(__name__)
# # app.config['SECRET_KEY'] = 'secret!'
# # socketio = SocketIO(app)

# # @socketio.on('aaa')
# # def test_connect():
# #     print("Welcome, aaa received")
# #     emit('aaa_response', {'data': 'Server'})

# # if __name__ == '__main__':
# #     socketio.run(app, port=8000)


# from flask import Flask, render_template, request
# import eventlet
# import socketio
# import eventlet.wsgi

# sio = socketio.Server()#async_mode=async_mode)
# app = Flask(__name__)
# app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

# dict1={}
# i=0
# @app.route('/')
# def index():
# 	return render_template('file.html')

# @sio.event()
# def pingpong(sid):
# 	print("//////////////////////////")
# 	sio.emit("send_data", room=sid)

# @sio.event
# def connect(sid, data):	
# 	print("[INFO] Connect to the server")
# 	pingpong(sid)

# @sio.event
# def send(sid, data):
# 	global i
# 	if sid not in dict1:
# 		i+=1
# 		dict1[sid]=i
# 	key=dict1[sid]
# 	print("Reached here")
# 	sio.emit('response',{'key':key, 'data':data})
# 	pingpong(sid)

# @sio.event
# def disconnect(sid):
# 	print("[INFO] disconnected from the server")

# if __name__ == '__main__':
# 	eventlet.wsgi.server(eventlet.listen(('0.0.0.0',5000)), app)
# 	# D:\gil\client_server_socket\server\server.py


# from flask import Flask
# from flask_socketio import SocketIO, send
# import time

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret'
# app.config['DEBUG'] = True
# socketio = SocketIO(app)

# @socketio.on('connect')
# def on_connect():
#     print('Server received connection')

# @socketio.on('message')
# def on_message(msg):
#     print(msg)
#     endtime = time.time() + 5 # loop for 5 secs
#     while time.time() < endtime:
#         socketio.emit("custom event", f"The time is: {time.strftime('%H:%M:%S')}")
#         socketio.sleep(1)

# if __name__=="__main__":
#     socketio.run(app)


#Server.py
# from typing import TextIO
import pickle
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import cv2
import numpy as np
import base64
import pickle
import random
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# counter=0
socketio = SocketIO(app)
def on_aaa_response(args):
    print('on_aaa_response', args['data']) #D:\gil\client_server_socket\client\client.py
@socketio.on('connected')
def test_connect(args):
    # global counter
    # counter+=1
    print(args['counter'])
    data=args['data']
    jpg_original=base64.b64decode(data)
    jpg_as_np=np.frombuffer(jpg_original,dtype=np.uint8)
    img=cv2.imdecode(jpg_as_np,flags=1)
    cv2.imwrite("output.jpg",img)
    # cv2.imshow("server",img)
    # if cv2.waitKey(0) & 0xFF == ord('Q'):cv2.
    #     # break
    #     pass
    # cv2.imwrite(f'images/{random.random()}.jpg',img)

    # nparr = np.fromstring(data, np.uint8)
    # frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # data=pickle.loads(args)
	# data=args['data']
    # jpg=base64.b64decode(data,)
    # jpg_as_np = np.frombuffer(jpg, dtype=np.uint8)
    # image_buffer = cv2.imdecode(jpg_as_np, flags=1)
    # cv2.imshow("server side",img)
    # cv2.waitKey(0)

	# socketio.on('connected', on_aaa_response)
    # print("Welcome, aaa received")
	# print()
    # emit('aaa_response', {'data': 'Server'})

if __name__ == '__main__':
    socketio.run(app, port=8000)