from pypline import structures, configuration

class StdOutLogger:
    def __call__(self, msg, params):
        print(msg)
        print(params)

class DecoratorPipeline(structures.Pipeline):
    def __init__(self, src, sink):
        source = src
        sink = sink
        i = structures.In(source, lambda x: str(x))
        o = structures.Out(sink, lambda x: "DECORATED:" + x)
        l = StdOutLogger()

        conf = configuration.PipelineConfiguration({
            'source': source,
            'sink': sink,
            'pipe_in': i,
            'pipe_out': o,
            'logger': l
        })

        super().__init__(config=conf)

source = structures.Source([1,2,3,4])
sink = structures.Sink(2)

pipeline = DecoratorPipeline(source, sink)

pipeline.start()
