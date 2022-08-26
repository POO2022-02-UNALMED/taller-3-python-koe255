class TV:
    numTV = 0

    def __init__(self, _marca, _estado):
        self._marca = _marca
        self._estado = _estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500

        TV.numTV += 1

    def getMarca(self):
        return self._marca

    def setMarca(self, _marca):
        self._marca = _marca

    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control = control

    def getPrecio(self):
        return self._precio

    def setPrecio(self, _precio):
        self._precio = _precio

    def getVolumen(self):
        return self._volumen

    def setVolumen(self, _volumen):
        self._volumen = _volumen

    def getCanal(self):
        return self._canal

    def setCanal(self, _canal):
        if (_canal >= 1 and _canal <= 120 and self._estado):
            self._canal = _canal

    def getNumTV():
        return TV.numTV

    def setNumTV(numTV):
        TV.numTV = numTV

    def getEstado(self):
        return self._estado

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def canalUp(self):
        if (self._estado and self._canal != 120):
            self._canal += 1

    def canalDown(self):
        if (self._estado and self._canal != 1):
            self._canal -= 1

    def volumenUp(self):
        if (self._estado and self._volumen != 7):
            self._volumen += 1

    def volumenDown(self):
        if (self._estado and self._volumen != 1):
            self._volumen -= 1
