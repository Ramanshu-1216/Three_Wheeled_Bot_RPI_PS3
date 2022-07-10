from flask import Flask, render_template, Response
import time
import cv2
from subprocess import check_output

app = Flask(__name__)

IPAddr = str(check_output(["hostname", "-I"]).split()[0])[2:-1]
print(IPAddr)

cv2.destroyAllWindows()

# time.sleep(2)
print("...........................")
camera = cv2.VideoCapture(0)


def gen_frames():  # generate frame by frame from camera
    print("I am in here")
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            print("Coming")
            break
        else:
            # print("coing here")

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    # Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    # camera = cv2.VideoCapture(3)
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host=IPAddr, port=8080)
