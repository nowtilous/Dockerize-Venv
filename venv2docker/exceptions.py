class InvalidVirtualEnvironmentPath(Exception):
    def __init__(self):
        import sys
        try:
            ln = sys.exc_info()[-1].tb_lineno
        except AttributeError:
            import inspect
            ln = inspect.currentframe().f_back.f_lineno
        self.args = "{0.__name__} (line {1})".format(type(self), ln),
        sys.exit(self)
