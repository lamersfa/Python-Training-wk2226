import cv2
import math
from box import Box


class DrumCam:
    """Class for the camera handling of the virtual drums.
    Given a cv2.VideoCapture() in capture and starts a live video feed off of it.
    Tracks a variable amount of objects, for which the names and bounds of the masks are defined in bounds_list.
    Then gives the positions of the center of these objects to the DrumHandler."""

    def __init__(self, capture, bounds_list, command, hihat_off_color, drum_off_color, hflip, vflip):
        self.masks = bounds_list
        for bounds in bounds_list:
            print(f"Mask for '{bounds[0]}' found.")
        self.cap = capture
        self.width = capture.get(3)
        self.height = capture.get(4)
        self.command = command
        self.drums = self._drum_init(hihat_off_color, drum_off_color)
        self.hflip = hflip
        self.vflip = vflip

    def _drum_init(self, hihat_off_color, drum_off_color):
        """Create the coordinates of the drum rectangles."""
        width = int(self.width)
        height = int(self.height)
        names = [item[0] for item in self.masks]
        drums = [Box('Hi-hat toggle', (0, 0), (2 * math.floor(width / 11),
                                               math.floor(height / 5)), names, self.command, hihat_off_color),
                 Box('Hi-hat', (3 * math.floor(width / 11), 0),
                     (5 * math.floor(width / 11), math.floor(height / 5)), names, self.command, drum_off_color),
                 Box('Crash', (6 * math.ceil(width / 11), 0),
                     (8 * math.ceil(width / 11), math.floor(height / 5)), names, self.command, drum_off_color),
                 Box('Ride', (9 * math.ceil(width / 11), 0),
                     (width - 1, math.floor(height / 5)), names, self.command, drum_off_color),
                 Box('Snare', (3 * math.floor(width / 11), 2 * math.floor(height / 5)),
                     (5 * math.floor(width / 11), 3 * math.floor(height / 5)), names, self.command, drum_off_color),
                 Box('Bass', (6 * math.ceil(width / 11), 2 * math.floor(height / 5)),
                     (8 * math.ceil(width / 11), 3 * math.floor(height / 5)), names, self.command, drum_off_color),
                 Box('High tom', (0, 4 * math.floor(height / 5)),
                     (2 * math.floor(width / 8), height - 1), names, self.command, drum_off_color),
                 Box('Mid tom', (3 * math.floor(width / 8), 4 * math.floor(height / 5)),
                     (5 * math.ceil(width / 8), height - 1), names, self.command, drum_off_color),
                 Box('Floor tom', (6 * math.ceil(width / 8), 4 * math.floor(height / 5)),
                     (width - 1, height - 1), names,
                     self.command, drum_off_color)]  # Name, Top left coord, bottom right coord, mask_names, color
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
            if cv2.contourArea(c) > 60:
                x, y, w, h = cv2.boundingRect(c)
                center = (math.floor(x + 0.5 * w), math.floor(y + 0.5 * h))
                cv2.circle(img, center, 1, (255, 255, 0), 2)
        coords = (x, y)
        return coords

    def drum_drawer(self, img):
        """Draws the rectangles and names of the drums on the screen."""
        for item in self.drums:
            color = item.cur_color
            text = item.name
            font = cv2.FONT_HERSHEY_SIMPLEX
            text_size = cv2.getTextSize(text, font, 0.5, 2)[0]
            center_x = int((item.x1 + item.x2 - text_size[0]) / 2)
            center_y = int((item.y1 + item.y2 + text_size[1]) / 2)
            rec = cv2.rectangle(img, (item.x1, item.y1), (item.x2, item.y2), color, 1)
            cv2.putText(rec, text, (center_x, center_y), font, 0.5, (255, 0, 0), 2)

    def cam_loop(self):
        """Starts the camera loop. For each frame, get the image, convert it to hsv, apply the masks with
        contour_handler and then shows the image on screen. Loop stops when 'q' is pressed."""
        while True:
            success, img = self.cap.read()
            if not success:
                print("Unable to read from the video capture. Exiting.")
                exit(1)
            if self.vflip:
                img = cv2.flip(img, 0)
            if self.hflip:
                img = cv2.flip(img, 1)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            for mask in self.masks:
                coord = self.contour_handler(img, hsv, mask)
                for drum in self.drums:
                    drum.check_bounds(mask[0], coord)

            self.drum_drawer(img)

            cv2.imshow("Output", img)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break
