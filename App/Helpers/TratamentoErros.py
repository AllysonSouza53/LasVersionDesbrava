class Erros:
    def __init__(self):
        self._errors = []

    def SetErro(self, msg: str) -> None:
        self._errors.append(msg)

    def GetErros(self) -> str:
        return self._errors

    def TemErros(self) -> bool:
        if self._errors:
            return True
        else:
            return False

    def LimpeErros(self) -> None:
        self._errors.clear()