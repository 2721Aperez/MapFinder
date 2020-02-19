import webbrowser, sys, pyperclip

sys.argv
if len(sys.argv) > 1:
    #['program name', 'Address', 'Street']
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)