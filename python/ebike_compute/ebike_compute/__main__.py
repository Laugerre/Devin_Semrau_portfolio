
#import the camera class from file CameraRecorder.py
import Camera   #import Camera.py


def main():
    # Create a camera recorder object
    camera_recorder = Camera.CameraRecorder(1)

    # Start the camera recorder
    camera_recorder.start_recording()

    # If the q key is pressed than Stop the camera recorder
    if cv2.waitKey(1) & 0xFF == ord('q'):
        camera_recorder.stop_recording()

    # Release the camera recorder
    camera_recorder.release()

if __name__ == "__main__":
    main()