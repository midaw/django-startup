# -*- coding: utf-8 -*-
'''
List of application specific views.

Replace "new_app" to your application name.
'''
from libs.project.decorators import render_to


@render_to('new_app/index.html')
def index(request):
    '''Main page of website'''
    return {'say': 'Hello!'}
