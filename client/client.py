

# #Client.py
# from socketIO_client import SocketIO, LoggingNamespace
# import cv2
# import base64
# import pickle
# import random
# def on_aaa_response(args):
#     print('on_aaa_response', args['data'])

# socketIO = SocketIO('localhost', 8000, LoggingNamespace)
# # socketIO.on('aaa_response', on_aaa_response)
# # emit('aaa_response', {'data': 'Server'})
# cap=cv2.VideoCapture(0)
# counter=0
# while True:
#     ret,frame=cap.read()
#     if ret:
#         rand=random.random()
#         counter+=1
#         print(counter)
#         frame=cv2.resize(frame,(256,256))
#         # data = cv2.imencode('.jpg', frame)[1].tostring()
#         string_img = base64.b64encode(cv2.imencode('.jpg', frame,  [int(cv2.IMWRITE_JPEG_QUALITY), 50])[1]).decode()
#         # frame=pickle.dumps(frame)
#         # retval, frame = cv2.imencode('.jpg', frame)
#         # jpg_as_text = base64.b64encode(frame,'utf-8')
#         socketIO.emit('connected',{'data':string_img,'counter':counter})
        # socketIO.wait(seconds=1)

        # print(jpg_as_text[:80])

        # Convert back to binary
        # jpg_original = base64.b64decode(jpg_as_text)

# socketIO.emit('connected',{'data': 'client'})
# socketIO.wait(seconds=1)

import socketio
import cv2
import time
import base64
sio = socketio.Client()
cap=cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')) # depends on fourcc available camera
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# cap.set(cv2.CAP_PROP_FPS, 5)

@sio.event
def connect():
    print('connection established')
    print('message sent')
    frame_rate = 20
    prev = 0
    while True:
        
        time_elapsed = time.time() - prev
        ret,frame=cap.read()
        if not ret:
            break
        # frame=cv2.resize(frame,(300,300))
        print(frame.shape)
        if time_elapsed > 1./frame_rate:
            prev = time.time()
        # frame=base64.encodestring(cv2.imencode('.png',frame)[1])
            frame = base64.b64encode(cv2.imencode('.jpg', frame,[cv2.IMWRITE_JPEG_QUALITY, 80])[1]).decode()
            
        # print(frame.shape)
        # string_img = base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode()
            sio.emit('my image',frame)


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://127.0.0.1:8000')
sio.wait()


# import asyncio
# import socketio

# sio = socketio.AsyncClient()

# @sio.event
# async def connect():
#     print('connection established')
#     await sio.emit('message',data='detection', callback=done)
#     print('message sent')

# @sio.event
# def disconnect():
#     print('disconnected from server')

# async def done():
#     await sio.disconnect()

# async def main():
#     await sio.connect('http://localhost:5000')
#     await sio.wait()

# if __name__ == '__main__':
#     asyncio.run(main())


# import asyncio
# import socketio

# sio = socketio.Client()

# @sio.event
# def connect():
#     print('connection established')
#     sio.emit('message',data='detection')
#     print('message sent')

# @sio.event
# def disconnect():
#     print('disconnected from server')

# def done():
#     sio.disconnect()

# def main():
#     sio.connect('http://127.0.0.1:5000')
#     sio.wait()

# if __name__ == '__main__':
#     main()

# import asyncio
# import socketio

# sio = socketio.AsyncClient()

# @sio.event
# async def connect():
#     print('connection established')
#     await sio.emit('message',data='detection', callback=done)
#     print('message sent')

# @sio.event
# def disconnect():
#     print('disconnected from server')

# async def done():
#     await sio.disconnect()

# async def main():
#     await sio.connect('http://localhost:5000')
#     await sio.wait()

# if __name__ == '__main__':
#     asyncio.run(main())

#Client.py
# import time
# import socketio
# sio = socketio.Client(engineio_logger=True)
# start_timer = None

# # if __name__ == '__main__':
# sio.connect('http://127.0.0.1:3000')
# sio.wait()
# sio.emit('message', {"Data": "Device_id"})
# @socketio.event
# def connect():
#     print("client message recieved",message)
    # sio.emit('my_response', {'data': 'got it!'})
# @sio.event
# def message(data):
#     print("client receiving the message from the server")

