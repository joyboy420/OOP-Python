class Silly:
    def _get_silly(self):
        print("Getting silly huh!!")
        return self._silly

    def _set_silly(self, value):
        print("Your silly argument is {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("Well, you deleted silly")
        del self._silly

    silly = property(_get_silly, _set_silly, 
            _del_silly, "Well , a silly property I guess")