class Dadu:
    def __init__(self, filme=None, ano=None):
        self._filme = filme   
        self._ano = ano
    def get_filme(self):
        return self._filme
    def get_ano(self):
        return self._ano
    def set_filme(self, new):
         self._filme = new
    def set_ano(self, new):
        self._ano = new
    def set_filmeeano(self,newfil, newano):
        self._filme = newfil
        self._ano = newano
    def get_filmeeano(self):
        return f'{self._filme} de {self._ano}'
    





