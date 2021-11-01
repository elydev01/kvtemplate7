from threading import Thread

from kivy.lang import Builder
from kivymd.app import MDApp as App
from kivymd.uix.screen import MDScreen
from playsound import playsound


class ScanMainScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.last_scanned = ""

    def read_qr(self, data):
        url = data.decode()
        
        if self.last_scanned != url:
            if "wav" in url:
                self.last_scanned = url
                Thread(target=lambda: playsound("assets/audio/success.mp3")).start()
            else:
                Thread(target=lambda: playsound("assets/audio/warning.wav")).start()

    def on_leave(self, *_):
        self.last_scanned = ""


with open('views/scan.kv', encoding='utf-8') as f:
    Builder.load_string(f.read())


class ScanScreenApp(App):
    def build(self):
        return ScanMainScreen()


def main():
    ScanScreenApp().run()


if __name__ == '__main__':
    main()
