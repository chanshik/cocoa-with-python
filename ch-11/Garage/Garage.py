from Cocoa import NSWindowController, NSLog, objc, NSApplication, NSApp
from Foundation import NSObject
from PyObjCTools import AppHelper


class Garage(NSWindowController):
    tableView = objc.IBOutlet()
    db = []

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

    @objc.IBAction
    def add_(self, sender):
        pass

    @objc.IBAction
    def remove_(self, sender):
        pass

    # data source methods
    def numberOfRowsInTableView_(self, aTableView):
        return len(self.todos)

    def tableView_objectValueForTableColumn_row_(
            self, aTableView, aTableColumn, rowIndex):

        return self.todos[rowIndex]

    #def tableView_setObjectValue_forTableColumn_row_(
    #        self, aTableView, anObject, aTableColumn, rowIndex):
    #    pass

    # delegate methods
    def tableView_shouldSelectRow_(self, aTableView, rowIndex):
        return True

    def tableView_shouldEditTableColumn_row_(self, aTableView, aTableColumn, rowIndex):
        return False

    def tableViewSelectionDidChange_(self, notification):
        row = self.tableView.selectedRow()

        NSLog('Selected: ' + str(row))


if __name__ == '__main__':
    app = NSApplication.sharedApplication()

    viewController = Garage.alloc().initWithWindowNibName_('Garage')
    viewController.showWindow_(viewController)

    NSApp.activateIgnoringOtherApps_(True)

    AppHelper.runEventLoop()
