#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

TARGET = 'to-deploy/'

def main():
    here = os.path.dirname(__file__)
    deploy_target = os.path.join(here, TARGET)
    loader = jinja2.FileSystemLoader(os.path.join(here, 'templates'))
    templates = jinja2.Environment(loader=loader)

    if os.path.exists(deploy_target):
        shutil.rmtree(deploy_target)
    os.makedirs(deploy_target)
    shutil.copytree(os.path.join(here, 'static'), os.path.join(deploy_target, 'static'))

    pages = ['index.html', 'games.html', 'resume.html']

    ctx = {}
    for page in pages:
        tem = templates.get_template(page)
        with codecs.open(os.path.join(deploy_target, page), 'w') as out:
            out.write(tem.render(**ctx))

if __name__ == '__main__':
    main()
