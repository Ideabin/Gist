# -*- coding: utf-8 -*-

import sublime_plugin

IDEA_TEMPLATE = """\
---
id:
desc: " #ideabin"
---
"""


class GistIdeaCommand(sublime_plugin.WindowCommand):

    def run(self):
        view = self.window.new_file()
        view.set_syntax_file('Packages/MarkdownEditing/Markdown.tmLanguage')
        view.run_command('append', {'characters': IDEA_TEMPLATE})
        # view.set_scratch(True)
