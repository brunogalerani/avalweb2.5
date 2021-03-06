# -*- coding: utf-8 -*-

response.menu = [
    (T('Home'), request.controller == 'default' and request.function == 'index', URL('default', 'index')),        
    (T('Sair'), request.controller == 'default' and request.function == 'who', URL('logout', 'logout'))]

#########################################################################
## Changes the menu active item
#########################################################################


def toggle_menuclass(cssclass='pressed', menuid='headermenu'):
    """This function changes the menu class to put pressed appearance"""

    positions = dict(
        index='',
        what='-108px -115px',
        download='-211px -115px',
        who='-315px -115px',
        support='-418px -115px',
        documentation='-520px -115px'
    )

    if request.function in positions.keys():
            jscript = """
            <script>
             $(document).ready(function(){
                         $('.%(menuid)s a').removeClass('%(cssclass)s');
                         $('.%(function)s').toggleClass('%(cssclass)s').css('background-position','%(cssposition)s')

             });
            </script>
            """ % dict(cssclass=cssclass,
                       menuid=menuid,
                       function=request.function,
                       cssposition=positions[request.function]
                       )

            return XML(jscript)
    else:
        return ''
