class Box:
    """Creates a box object, with a name, coordinates for the top left and bottom right, and a dictionary
    which keeps track of which object is inside the box."""

    def __init__(self, name, coords1, coords2, object_names, command):
        self.name = name
        self.x1 = coords1[0]
        self.y1 = coords1[1]
        self.x2 = coords2[0]
        self.y2 = coords2[1]
        self.command = command
        self._press_status = {}
        for name in object_names:
            self._press_status[name] = False

    def check_bounds(self, objname, coords):
        """Checks if an object has entered the box. If it enters the box, calls the command and changes its
        press_status to True. If it leaves the box when the press_status is True, it turns the press_status
        to False."""
        if not self._press_status[objname] and self.x1 <= coords[0] <= self.x2 and self.y1 <= coords[1] <= self.y2:
            self.command(self.name)
            self._press_status[objname] = True

        elif self._press_status[objname] and coords != (-1, -1) and ((self.x1 > coords[0] or coords[0] > self.x2)
                                                                     or (self.y1 > coords[1] or self.y2 < coords[1])):
            self._press_status[objname] = False
