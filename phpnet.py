import sublime_plugin
import webbrowser

APPLYABLE_FILES = ('.php')
PHPNET_URL = 'http://php.net/%s'

class PhpNetCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.file_name().split('.')[-1] not in APPLYABLE_FILES:
            return

        for region in self.view.sel():
            selection = self.view.substr(region)

            webbrowser.open(PHPNET_URL % selection, autoraise=True)
