# -*- coding: utf-8 -*-

import os
import sublime
import sublime_plugin
from . import frontmatter
from . import helpers

Idea_Template = """\
---
id:
desc: " #ideabin"
---
"""

Markdown_Syntax = 'Packages/MarkdownEditing/Markdown.tmLanguage'
Gist_Url = "https://api.github.com/gists/{0}}"
Gist_Html_Url = "https://gist.github.com/{0}"


class GistIdeaCommand(sublime_plugin.WindowCommand):

    def run(self):
        view = self.window.new_file()
        view.set_syntax_file(Markdown_Syntax)
        view.run_command('append', {'characters': Idea_Template})
        # view.set_scratch(True)


class GistOnLoadListener(sublime_plugin.EventListener):

    def on_load_async(self, view):
        if view.settings().get('syntax') != Markdown_Syntax:
            return

        region = sublime.Region(0, view.size())
        gist = frontmatter.loads(view.substr(region))

        if gist.get('id'):
            g = {}
            g['description'] = gist.get('desc')
            g['html_url'] = Gist_Html_Url.format(gist.get('id'))
            g['url'] = Gist_Html_Url.format(gist.get('id'))

            # Bug: gistify_view needs a gist object that has 'files'
            helpers.gistify_view(view, g, os.path.basename(view.file_name()))
