import os
from .base import Base

class Source(Base):

    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'minisnip'
        self.mark = '[minisnip]'
        self.min_pattern_length = 0
        self.minisnip_dir = self.vim.eval('g:minisnip_dir')
        self.snippets = os.listdir(os.path.expanduser(self.minisnip_dir))

    def process_matches(self, filetypes):
        """ Process and return snippet names"""
        matches = []
        for filetype in filetypes:
            for snippet in self.snippets:
                if filetype in snippet:
                    matches.append(snippet.split(filetype)[1])
        return matches

    def gather_candidates(self, context):
        """Returns all snippets in the users vim minisnip directory"""
        split_filetypes = context['filetype'].split('.')
        filetypes = ['_' + filetype + '_' for filetype in split_filetypes]

        return [{'word': snippet} for snippet in self.process_matches(filetypes)]

