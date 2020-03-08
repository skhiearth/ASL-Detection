import cv2
import numpy as np
from tensorflow.keras.models import load_model
import time
import os
from App.cv import text_sound_file
from App.freeze_graph import freeze_graph

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

# Loading the model
model = load_model('models/model.h5')
freeze_graph()

# video_capture = cv2.VideoCapture(0)
# print('Detecting camera...')
# time.sleep(10)
#
# text = ''
# flag = []
#
# frame_count = 0
#
# while video_capture.isOpened():
#     re, frame = video_capture.read()
#
#     if re:
#         cv2.rectangle(frame, pt1=(100, 100), pt2=(400, 400), color=(0, 0, 255), thickness=4)
#         cv2.imshow("Capturing", frame)
#
#         frame_count += 1
#
#         if frame_count % 100 == 0:
#             img_array = np.asarray(frame)
#             clone = img_array[100:400, 100:400].copy()
#             clone_resized = cv2.resize(clone, (64, 64))
#             img_array = clone_resized / 255
#             img_final = np.expand_dims(img_array, axis=0)
#
#             prediction = model.predict(img_final)
#             label = np.argmax(prediction)
#
#             if label == 0:
#                 ch = 'A'
#             elif label == 1:
#                 ch = 'B'
#             elif label == 2:
#                 ch = 'C'
#             elif label == 3:
#                 ch = 'D'
#             elif label == 4:
#                 ch = 'E'
#             elif label == 5:
#                 ch = 'F'
#             elif label == 6:
#                 ch = 'G'
#             elif label == 7:
#                 ch = 'H'
#             elif label == 8:
#                 ch = 'I'
#             elif label == 9:
#                 ch = 'J'
#             elif label == 10:
#                 ch = 'K'
#             elif label == 11:
#                 ch = 'L'
#             elif label == 12:
#                 ch = 'M'
#             elif label == 13:
#                 ch = 'N'
#             elif label == 14:
#                 ch = 'O'
#             elif label == 15:
#                 ch = 'P'
#             elif label == 16:
#                 ch = 'Q'
#             elif label == 17:
#                 ch = 'R'
#             elif label == 18:
#                 ch = 'S'
#             elif label == 19:
#                 ch = 'T'
#             elif label == 20:
#                 ch = 'U'
#             elif label == 21:
#                 ch = 'V'
#             elif label == 22:
#                 ch = 'W'
#             elif label == 23:
#                 ch = 'X'
#             elif label == 24:
#                 ch = 'Y'
#             elif label == 25:
#                 ch = 'Z'
#             elif label == 26:
#                 ch = ''
#             elif label == 27:
#                 ch = ''
#             elif label == 28:
#                 ch = ' '
#
#             flag.append(ch)
#
#     else:
#         print('No camera detected.')
#
#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break
#
# text = ''
# for i in flag:
#     text += i
#
# video_capture.release()
# cv2.destroyAllWindows()
#
# print(text)
# text_sound_file(text, "en")
