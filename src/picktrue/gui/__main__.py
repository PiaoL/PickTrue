import tkinter as tk
import webbrowser
from tkinter import ttk

from picktrue import version
from picktrue.gui.downloader import downloaders
from picktrue.gui.toolkit import info


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.tabs = ttk.Notebook(self)
        self.title("PickTrue - 相册下载器 v%s" % version.__version__)
        self.build_menu()

        for downloader in downloaders:
            self.tabs.add(downloader(self), text=downloader.title)
        self.tabs.pack(
            side=tk.LEFT,
        )

    @staticmethod
    def open_online_help():
        url = 'https://github.com/winkidney/PickTrue'
        webbrowser.open_new_tab(url)

    @staticmethod
    def show_about():
        webbrowser.open_new_tab(
            'https://winkidney.com'
        )

    @staticmethod
    def contact():
        info(
            "任何问题或者建议请联系作者\n"
            "用户QQ群： 863404640\n"
        )

    def build_menu(self):
        menu_bar = tk.Menu(self)
        help_menu = tk.Menu(menu_bar)
        help_menu.add_command(label="在线帮助", command=self.open_online_help)
        help_menu.add_command(label="关于", command=self.show_about)
        help_menu.add_command(label="联系作者/用户群", command=self.contact)
        menu_bar.add_cascade(label="帮助", menu=help_menu)
        self.config(menu=menu_bar)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
