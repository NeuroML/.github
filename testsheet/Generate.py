
from RepoInfo import *
import os

info = """
## Tests on NeuroML repositories
"""

count = 0


allrefs = {'Specification repositories': srefs,
           'Core Java repositories': jrefs,
           'Core Python repositories': pyrefs,
           'Related repositories': otherrefs,}

for cat in allrefs:
    info += '\n### %s\n\n'%cat

    info += '| Repository | Tests | PRs |\n'
    info += '|----------|:------:|:------:|\n'

    refs = allrefs[cat]
    for name in refs.keys():
        ref = refs[name]

        print("Looking at: %s in %s"%(ref, name))

        info += '| <a href="https://github.com/%s">%s</a> |'%(ref,name)

        wfs = ['ci.yml'] if not name in workflows else workflows[name]
        for wf in wfs:
            info += '  [![OMV](https://github.com/%s/actions/workflows/%s/badge.svg)](https://github.com/%s/actions/workflows/%s) '%(ref,wf,ref,wf)

        info += '  | '

        info += '  [![GitHub pull requests](https://img.shields.io/github/issues-pr/%s)](https://github.com/%s/pulls) | \n'%(ref,ref)


        count+=1

info += '  </table>\n'


readme = open('README.md','w')
readme.write(info)
readme.close()
