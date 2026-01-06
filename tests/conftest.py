import pytest
from datetime import datetime


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot(type="png", full_page=True)
            import base64
            encoded = base64.b64encode(screenshot).decode("ascii")
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                extras.append(pytest_html.extras.image(encoded))
                report.extra = extras