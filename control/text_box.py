from control.control import Control

class TextBox(Control):

    def __init__(self, type, locator):
        super(TextBox, self).__init__(type, locator)

    def set_text(self, texto: str):
        """
        Permite escribir el texto de entrada en un elemento de tipo INPUT/ Caja de texto.
        :param texto: Texto alfanumérico que se ingresara a la caja de texto.
        :return:
        """
        self.find()
        print("Escribiendo en el campo {} el texto -> {} ".format(self.control, texto))
        self.control.send_keys(texto)

    def set_text_clear(self, texto: str):
        """
        Limpia la caja de texto y permite escribir el texto de entrada en un elemento de tipo INPUT/ Caja de texto.
        :param texto: Texto alfanumérico que se ingresara a la caja de texto.
        :return:
        """
        self.find()
        print("Escribiendo en el campo {} el texto -> {} ".format(self.control, texto))
        self.control.clear()
        self.control.send_keys(texto)
