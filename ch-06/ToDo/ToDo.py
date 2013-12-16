from Cocoa import *
from Foundation import NSObject
from PyObjCTools import AppHelper


class ToDoController(NSWindowController):
    def awakeFromNib(self):
        NSLog('awakeFromNib')

    def windowDidLoad(self):
        NSWindowController.windowDidLoad(self)
        NSLog('windowDidLoad')

    def windowShouldClose_(self, sender):
        NSLog('windowShouldClose')
        return True

    def windowWillClose_(self, notification):
        NSLog('windowWillClose')
        AppHelper.stopEventLoop()

    def applicationShouldTerminateAfterLastWindowClosed_(self, sender):
        NSLog('applicationShouldTerminateAfterLastWindowClosed')
        return True


if __name__ == '__main__':
    app = NSApplication.sharedApplication()

    viewController = ToDoController.alloc().initWithWindowNibName_('ToDo')
    viewController.showWindow_(viewController)

    NSApp.activateIgnoringOtherApps_(True)

    AppHelper.runEventLoop()
