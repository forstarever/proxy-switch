#!/usr/bin/env python3

import gi
import subprocess

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, GObject, Gio, AppIndicator3, GLib

class ProxySwitcher:
    def __init__(self):
        self.indicator = AppIndicator3.Indicator.new(
            "proxy-switcher",
            "proxy-off",
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

        self.update_icon()
        self.indicator.set_menu(self.create_menu())

    def create_menu(self):
        menu = Gtk.Menu()

        # 添加“Toggle Proxy”菜单项
        toggle_item = Gtk.MenuItem(label="Toggle Proxy")
        toggle_item.connect("activate", self.toggle_proxy)  # 绑定切换代理状态的函数
        menu.append(toggle_item)

        # 添加“Quit”菜单项
        quit_item = Gtk.MenuItem(label="Quit")
        quit_item.connect("activate", self.quit)
        menu.append(quit_item)

        menu.show_all()
        return menu

    def update_icon(self):
        mode = subprocess.getoutput("gsettings get org.gnome.system.proxy mode").strip("'")
        if mode == "manual":
            self.indicator.set_icon_full("/opt/proxy-GUI/proxy-on.png", "Proxy On")
        else:
            self.indicator.set_icon_full("/opt/proxy-GUI/proxy-off.png", "Proxy Off")

    def toggle_proxy(self, widget=None):
        mode = subprocess.getoutput("gsettings get org.gnome.system.proxy mode").strip("'")
        if mode == "manual":
            subprocess.run(["gsettings", "set", "org.gnome.system.proxy", "mode", "none"])
        else:
            subprocess.run(["gsettings", "set", "org.gnome.system.proxy", "mode", "manual"])
        self.update_icon()

    def quit(self, source):
        Gtk.main_quit()

if __name__ == "__main__":
    proxy_switcher = ProxySwitcher()
#    GLib.timeout_add(1000, proxy_switcher.update_icon)  # 使用 GLib.timeout_add 代替 GObject.timeout_add
    Gtk.main()

