#!/usr/bin/env python
# *-* coding:utf-8 *-*

import cv2
import numpy as np


class Camera(object):
    """
    通过openvcv读取摄像头
    """

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        ret, frame = self.cap.read()
        assert ret
        ret, jpg = cv2.imencode('.jpg', frame)
        assert ret
        return np.array(jpg).tostring()
