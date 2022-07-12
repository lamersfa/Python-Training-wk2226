import cv2
import numpy as np
import math


class DrumCam:
    """Class for the camera handling of the virtual drums.
    Given a cv2.VideoCapture() in capture and starts a live video feed off of it.
    Tracks a variable amount of objects, for which the names and bounds of the masks are defined in bounds_list.
    Then gives the positions of the center of these objects to the DrumHandler."""

    def __init__(self, capture, bounds_list):
        self.masks = bounds_list  # TODO: throw error if every element is not name, lower, upper or if it is empty.
        for bounds in bounds_list:
            print(f"Mask for '{bounds[0]}' found.")
        self.cap = capture  # TODO: throw error if not valid
        self.width = capture.get(3)  # TODO: Check if it's used
        self.height = capture.get(4)  # TODO: Check if it's used
        self.drums = self._drum_init()

    def _drum_init(self):
        """Create the coordinates of the drum rectangles."""
        width = int(self.width)
        height = int(self.height)
        drums = [('Hi-hat toggle', (0, 0), (2 * math.floor(width / 11), math.floor(height / 5))),
                 ('Hi-hat', (3 * math.floor(width / 11), 0),
                  (5 * math.floor(width / 11), math.floor(height / 5))),
                 ('Crash', (6 * math.ceil(width / 11), 0),
                  (8 * math.ceil(width / 11), math.floor(height / 5))),
                 ('Ride', (9 * math.ceil(width / 11), 0),
                  (width - 1, math.floor(height / 5))),
                 ('Snare', (3 * math.floor(width / 11), 2 * math.floor(height / 5)),
                  (5 * math.floor(width / 11), 3 * math.floor(height / 5))),
                 ('Bass', (6 * math.ceil(width / 11), 2 * math.floor(height / 5)),
                  (8 * math.ceil(width / 11), 3 * math.floor(height / 5))),
                 ('High tom', (0, 4 * math.floor(height / 5)),
                  (2 * math.floor(width / 8), height - 1)),
                 ('Mid tom', (3 * math.floor(width / 8), 4 * math.floor(height / 5)),
                  (5 * math.ceil(width / 8), height - 1)),
                 ('Floor tom', (6 * math.ceil(width / 8), 4 * math.floor(height / 5)),
                  (width - 1, height - 1))]  # Name, Top left coord, bottom right coord.
        return drums

    def contour_handler(self, img, hsv, bounds):
        """Creates a color mask based on the hsv image and the bounds. Then detects the contours of the object if
        it is found. If the object is found, takes the biggest contour area (largest object) and creates a dot
        on the center of the object. Also returns the coordinates of this center if found, else returns (-1,-1)"""
        lower = bounds[1]
        upper = bounds[2]
        x = -1
        y = -1
        mask = cv2.inRange(hsv, lower, upper)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            center = (math.floor(x + 0.5 * w), math.floor(y + 0.5 * h))
            cv2.circle(img, center, 1, (255, 255, 0), 2)
        coords = (x, y)
        return coords

    def drum_drawer(self, img):
        """Draws the rectangles and names of the drums on the screen."""
        for item in self.drums:
            text = item[0]
            font = cv2.FONT_HERSHEY_SIMPLEX
            textsize = cv2.getTextSize(text, font, 0.5, 2)[0]
            center_x = int((item[1][0] + item[2][0] - textsize[0]) / 2)
            center_y = int((item[1][1] + item[2][1] + textsize[1]) / 2)
            rec = cv2.rectangle(img, item[1], item[2], (255, 0, 0), 1)
            cv2.putText(rec, text, (center_x, center_y), font, 0.5, (255, 0, 0), 2)

    def cam_loop(self):
        """Starts the camera loop. For each frame, get the image, convert it to hsv, apply the masks with
        contour_handler and then shows the image on screen. Loop stops when 'q' is pressed."""
        while True:
            coords = []
            success, img = self.cap.read()
            if not success:
                print("TODO throw error")
            img = cv2.flip(img, 1)  # TODO: make an argument for enabling flip
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            for mask in self.masks:
                coord = self.contour_handler(img, hsv, mask)
                coords.append(coord)

            self.drum_drawer(img)
            # TODO: send coords to a handler that raises events when stuff gets called.

            cv2.imshow("Output", img)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break


def run():
    # Create a new video capture on the external webcam
    cap = cv2.VideoCapture(1)
    # Give lower and upper color values (hsv) for all masks
    lower_blue = np.array([95, 130, 110])
    upper_blue = np.array([140, 255, 255])
    lower_red = np.array([170, 180, 180])
    upper_red = np.array([180, 255, 255])
    # Make a list of all masks in the form (name, lower, upper)
    bounds_list = [('blue', lower_blue, upper_blue), ('red', lower_red, upper_red)]
    # Create a new camera
    drum_cam = DrumCam(cap, bounds_list)
    drum_cam.cam_loop()


if __name__ == '__main__':
    run()
