import time

class In:
    def __init__(self, origin, transform_fn):
        self.origin = origin
        self.transform_fn = transform_fn

    def pull(self):
        if self.origin.__has_data__():
            return self.transform_fn(self.origin.__pull__())
        else:
            return False

class Out:
    def __init__(self, destination, transform_fn):
        self.destination = destination
        self.transform_fn = transform_fn

    def push(self, data):
        if self.destination.__has_space__():
            self.destination.__push__(self.transform_fn(data))
        else:
            return False

class Sink:
    def __init__(self, buffer_size):
        self.data = []
        self.buffer_size = buffer_size

    def __has_space__(self):
        return len(self.data) < self.buffer_size

    def __push__(self,d):
        self.data.append(d)

    def __flush__(self):
        d = self.data
        self.data = []
        return d


class Source:
    def __init__(self, init_data):
        self.data = init_data

    def __has_data__(self):
        if len(self.data) < 1:
            return False

    def __pull__(self):
        return self.data.pop()

class Pipeline:
    def __init__(self, config):
        self.id = config.id
        self.source = config.source
        self.delay_sec = config.delay_sec
        self.sink = config.sink
        self.pipe_in = config.pipe_in
        self.pipe_out = config.pipe_out
        self.logger = config.logger

    def __log__(self, msg, params):
        if self.logger != None:
            self.logger.__call__(msg, params)

    def __delay__(self):
        if self.delay_sec:
            time.sleep(self.delay_sec)

    # Starts the Pipeline job
    def start(self):
        self.__log__(f"Pipeline {self.id} started", {})

        has_data = True
        counter = 0

        while has_data:
            counter += 1
            self.__log__(f"Pipeline working... operation {counter}", {})

            self.__delay__()

            val = self.pipe_in.pull()

            has_data = (val != False)

            result = self.pipe_out.push(val)

            if result == False:
                self.__log__(f"Sink buffer exhausted, flushing...", {})
                self.sink.__flush__()

            self.__log__(f"Operation {counter} complete", {})

        self.__log__(f"Pipeline {self.id} finished", {})

    # Easter egg method
    def __poompeet__(self):
        self.start()
