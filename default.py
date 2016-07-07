import sys
import xbmcaddon
import xbmcgui
import xbmc
import os

Addon = xbmcaddon.Addon('script.screensaver.xbian-hdmioff')

__scriptname__ = Addon.getAddonInfo('name')
__path__ = Addon.getAddonInfo('path')


class Screensaver(xbmcgui.WindowXMLDialog):

    class ExitMonitor(xbmc.Monitor):

        def __init__(self, exit_callback):
            self.exit_callback = exit_callback

        def onScreensaverDeactivated(self):
            print '3 ExitMonitor: sending exit_callback'
            os.system("vcgencmd display_power 1")
            self.exit_callback()

    def onInit(self):
        print '2 Screensaver: onInit'
        self.monitor = self.ExitMonitor(self.exit)

    def exit(self):
        print '4 Screensaver: Exit requested'
        self.close()


if __name__ == '__main__':
    print '1 Python Screensaver Started'
    sys.modules.clear()
    os.system("vcgencmd display_power 0")    
