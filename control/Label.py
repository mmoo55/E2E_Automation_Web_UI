from control.Control import Control


class Label(Control):

    def __init__(self, driver, type, locator):
        super(Label, self).__init__(driver, type, locator)