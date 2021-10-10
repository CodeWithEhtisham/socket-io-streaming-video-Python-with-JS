# # from socketIO_client import SocketIO, LoggingNamespace

# # def on_aaa_response(args):
# #     print('on_aaa_response', args['data'])

# # socketIO = SocketIO('localhost', 8000, LoggingNamespace)
# # socketIO.on('aaa_response', on_aaa_response)
# # socketIO.emit('aaa')
# # socketIO.wait(seconds=1)

# from flask import Flask, render_template, request
# from flask_socketio import SocketIO
# import socketio
# import cv2
# import json
# import base64
# from time import sleep
# cap=cv2.VideoCapture(0)
# sio = socketio.Client(engineio_logger=True)
# i=0;

# @sio.event
# def connect():
# 	print("CONNECTED")

# @sio.event
# def send_data():
# 	while(cap.isOpened()):
# 		ret,img=cap.read()
# 		if ret:
# 			img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# 			frame = cv2.imencode('.jpg', img)[1].tobytes()
# 			frame= base64.encodebytes(frame).decode("utf-8")
# 			message(frame)
# 			sleep(0)
# 		else:
# 			break

# def message(json):
# 	print("/////////////////////////////500")
# 	#sio.emit('send',str(i))
# 	sio.emit('send',json)

# @sio.event
# def disconnect():
# 	print("DISCONNECTED")

# if __name__ == '__main__':
# 	#sio.connect('http://192.168.0.108:5000') ## uncomment this line when the server is on remote system change the ip address with the ip address 
# 	#of the system where the server is running.
# 	sio.connect('0.0.0.0:5000')
# 	sio.wait()
# import socketio

# sio = socketio.Client()

# @sio.on('connect')
# def on_connect():
#     sio.send(f"\nClient {sio.sid} connected...\n")

# @sio.on('custom event')
# def receive_custom(msg):
#     print(msg)

# sio.connect('http://127.0.0.1:5000')
# # sio.wait() # cannot keyboard interrupt this
# sio.sleep(10)
# sio.disconnect()

#Client.py
from socketIO_client import SocketIO, LoggingNamespace
import cv2
import base64
import pickle
import random
def on_aaa_response(args):
    print('on_aaa_response', args['data'])

socketIO = SocketIO('localhost', 8000, LoggingNamespace)
# socketIO.on('aaa_response', on_aaa_response)
# emit('aaa_response', {'data': 'Server'})
cap=cv2.VideoCapture(0)
counter=0
while True:
    ret,frame=cap.read()
    if ret:
        rand=random.random()
        counter+=1
        print(counter)
        frame=cv2.resize(frame,(256,256))
        # data = cv2.imencode('.jpg', frame)[1].tostring()
        string_img = base64.b64encode(cv2.imencode('.jpg', frame,  [int(cv2.IMWRITE_JPEG_QUALITY), 50])[1]).decode()
        # frame=pickle.dumps(frame)
        # retval, frame = cv2.imencode('.jpg', frame)
        # jpg_as_text = base64.b64encode(frame,'utf-8')
        socketIO.emit('connected',{'data':string_img,'counter':counter})
        # socketIO.wait(seconds=1)

        # print(jpg_as_text[:80])

        # Convert back to binary
        # jpg_original = base64.b64decode(jpg_as_text)

# socketIO.emit('connected',{'data': 'client'})
# socketIO.wait(seconds=1)
