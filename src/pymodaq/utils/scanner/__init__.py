from importlib import import_module
from pathlib import Path

here = Path(__file__).parent.joinpath('scanners')
for path in here.iterdir():
    if path.is_file():
        import_module(f'.{path.stem}', 'pymodaq.utils.scanner.scanners')


from .scanner import Scanner  # import this one after the scanners because they have to first be registered
