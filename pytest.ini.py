import pytest

[pytest]
asyncio_default_fixture_loop_scope = function
filterwarnings =
    ignore::DeprecationWarning
addopts = --headed --browser chromium

addopts = --html=report.html --self-contained-html --headed --browser chromium
testpaths = tests