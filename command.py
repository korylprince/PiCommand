import commands
import re

page = """<!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>PiCommand</title>
    </head>
    <body>
    <form method="post" action="/">{buttons}</form>
    <pre>{output}</pre>
    </body>
    </html>"""

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    method = env['REQUEST_METHOD']
    buttons = [(lsprint,'Show Directory'),(dateprint,'Show Server Time')] 
    output = ''
    if method == 'POST':
        body = env['wsgi.input'].read()
        try:
            func = re.match('action\=([a-z]+)',body).group(1)
            if func in [x[0].__name__ for x in buttons]:
                output = eval(func+'()')
        except:
            pass
    return page.format(buttons=buttongen(buttons),output=output)

def buttongen(buttonlist):
    buttonstr = []
    for button in buttonlist:
        buttonstr.append('<button name="action" type="submit" value="{func}">{label}</button>'.format(
            func=button[0].__name__,label=button[1]))
    return ''.join(buttonstr)

def lsprint():
    return commands.getoutput('ls')

def dateprint():
    return commands.getoutput('date')
