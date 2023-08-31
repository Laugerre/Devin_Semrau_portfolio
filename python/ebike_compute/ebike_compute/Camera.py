# A Class that handles the recording of camera images from an external camera using open cv
# and the storing of that data to an a folder on the local machine

import cv2
import os
import time
import threading
import datetime
import logging
from ebike_compute import settings

class CameraRecorder:
    #Constructure that takes in the camera id
    def __init__(self, camera_id):
        self.camera_id = camera_id
        self.camera = None
        self.recording = False
        self.recording_thread = None
        self.recording_thread_stop = False

    # Start recording a video from the camera
    def start_recording(self):
        self.recording = True
        self.recording_thread_stop = False
        self.recording_thread = threading.Thread(target=self._record_video)
        self.recording_thread.start()

    # Stop recording video from the camera
    def stop_recording(self):
        self.recording = False
        self.recording_thread_stop = True

    # Get the camera id
    def get_camera_id(self):
        return self.camera_id

    # Get the camera
    def get_camera(self):
        return self.camera

    # Get the recording status
    def get_recording(self):
        return self.recording

    # Get the recording thread
    def get_recording_thread(self):
        return self.recording_thread

    # Get the recording thread stop status
    def get_recording_thread_stop(self):
        return self.recording_thread_stop

    # Set the camera id
    def set_camera_id(self, camera_id):
        self.camera_id = camera_id

    # Set the camera
    def set_camera(self, camera):
        self.camera = camera

    # Set the recording status
    def set_recording(self, recording):
        self.recording = recording

    # Set the recording thread
    def set_recording_thread(self, recording_thread):
        self.recording_thread = recording_thread

    # Set the recording thread stop status
    def set_recording_thread_stop(self, recording_thread_stop):
        self.recording_thread_stop = recording_thread_stop

    # Record video from the camera
    def _record_video(self):
        # Get the camera id
        camera_id = self.get_camera_id()

        # Get the camera
        camera = self.get_camera()

        # Get the recording status
        recording = self.get_recording()

        # Get the recording thread stop status
        recording_thread_stop = self.get_recording_thread_stop()

        # Set the video recording path
        video_recording_path = os.path.join(settings.VIDEO_RECORDING_PATH, str(camera_id))

        # Create the video recording path if it does not exist
        if not os.path.exists(video_recording_path):
            os.makedirs(video_recording_path)

        # Get the current time
        current_time = time.time()

        # Set the video recording file name as an mp4
        video_recording_file_name = str(current_time) + ".mp4"

        # Set the video recording file path
        video_recording_file_path = os.path.join(video_recording_path, video_recording_file_name)

        # Create the video writer
        video_writer = cv2.VideoWriter(video_recording_file_path, cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (640, 480))

        # While the recording is still active
        while recording:
            # Get the camera
            camera = self.get_camera()

            # Get the recording thread stop status
            recording_thread_stop = self.get_recording_thread_stop()

            # If the camera is not none
            if camera is not None:
                # Get the frame from the camera
                ret, frame = camera.read()

                # If the frame was read successfully
                if ret:
                    # Write the frame to the video writer
                    video_writer.write(frame)

            # If the recording thread stop status is true
            if recording_thread_stop:
                # Stop the recording
                recording = False

        # Release the video writer
        video_writer.release()

        # Set the recording status to false
        self.set_recording(False)

        # Set the recording thread stop status to false
        self.set_recording_thread_stop(False)

        

    

        




