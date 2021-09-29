class _Configuration:
    def __init__(self, conf):
        self.__conf__ = conf

    def get(self, name):
        if name not in self.__conf__.keys(): 
            return None  
        return self.__conf__[name]

class PipelineConfiguration(_Configuration):
    @property
    def id(self):
        return self.get('id')
    @property
    def source(self):
        return self.get('source')
    @property
    def sink(self):
        return self.get('sink')
    @property
    def pipe_in(self):
        return self.get('pipe_in')
    @property
    def pipe_out(self):
        return self.get('pipe_out')
    @property
    def delay(self):
        return self.get('delay')
    @property
    def logger(self):
        return self.get('logger')
