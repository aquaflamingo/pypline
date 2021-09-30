from pypline import structures

class StdOutLogger:
    def __call__(self, msg, params):
        print(msg)
        print(params)

class DecoratorPipeline(structures.Pipeline):
    def __init__(self, src, sink):
        i = structures.In(source, lambda x: x * 5)
        o = structures.Out(sink, lambda x: "DECORATED:" + str(x))
        l = StdOutLogger()

        super().__init__(
                id='decorator.pipeline',
                source=src,
                sink=sink,
                pipe_in=i,
                pipe_out=o,
                logger=l
                )

class DisplaySink(structures.Sink):
    def __flush__(self):
        print(f"Flushing {self.data}")
        self.data.clear()

source = structures.Source([1,2,3,4])
# Flush immediately
sink = DisplaySink(buffer_size=0)

pipeline = DecoratorPipeline(source, sink)

pipeline.start()
