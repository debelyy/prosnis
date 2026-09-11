# Коллекция — десктоп-обёртка (pywebview/WebView2).
# Окно с автозапуском снимает шаг «найти вкладку» — capture в нуле действий.
# Данные: localStorage в постоянном профиле WebView2 — поэтому private_mode=False обязателен
# (в инкогнито-профиле localStorage стирается при закрытии, проверено пробой).
import os
from pathlib import Path

import webview

PAGE = Path(os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")).as_uri()

if __name__ == "__main__":
    webview.create_window(
        "проснись",
        PAGE,
        width=1440,
        height=900,
        min_size=(1100, 700),
        background_color="#100e0c",
    )
    webview.start(private_mode=False)
