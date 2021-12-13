
from RepoInfo import *
import os

info = """
## Tests on NeuroML repositories
"""

count = 0

info += '  | Model | Tests | PRs |\n'
info += '  |----------|:------:|:------:|\n'


for name in jrefs.keys():
    ref = jrefs[name]

    print("Looking at: %s in %s"%(ref, name))

    info += ' | <a href="https://github.com/%s">%s</a> |'%(ref,name)
    info += '  [![OMV](https://github.com/%s/actions/workflows/ci.yml/badge.svg)](https://github.com/%s/actions/workflows/ci.yml) | '%(ref,ref)
    info += '  [![GitHub pull requests](https://img.shields.io/github/issues-pr/%s)](https://github.com/%s/pulls) | \n'%(ref,ref)


    count+=1

info += '  </table>\n'


readme = open('README.md','w')
readme.write(info)
readme.close()
