from script_benchmark_tools.benchmark import benchmark
from script_benchmark_tools.kwargs_provider import KwargsProvider


def run_benchmarks(scripts, kwargs_generator: KwargsProvider, n=1000):

    kwargs = kwargs_generator.get()

    benchmarks = []
    for script in scripts:
        result = benchmark(script, kwargs, n)
        benchmarks.append(result)

    return benchmarks