from control.Control import Control


class Button(Control):

    def __init__(self, driver, type, locator):
        super(Button, self).__init__(driver, type, locator)