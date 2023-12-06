import ahk


ahk.run_script('Run Notepad') # Open notepad
win = ahk.find_window(title=b'Untitled - Notepad') # Find the opened window

win.send('hello')  # Send keys directly to the window (does not need focus!)
win.move(x=200, y=300, width=500, height=800)

win.activate()           # Give the window focus
win.activate_bottom()    # Give the window focus
win.close()              # Close the window
win.hide()               # Hide the windwow
win.kill()               # Kill the window
win.maximize()           # Maximize the window
win.minimize()           # Minimize the window
win.restore()            # Restore the window
win.show()               # Show the window
win.disable()            # Make the window non-interactable
win.enable()             # Enable it again
win.to_top()             # Move the window on top of other windows
win.to_bottom()          # Move the window to the bottom of the other windows

win.always_on_top = True # Make the window always on top

for window in ahk.windows():
    print(window.title)

    # Some more attributes
    print(window.text)
    print(window.rect)   # (x, y, width, height)
    print(window.id)     # ahk_id
    print(window.pid)
    print(window.process)


if window.active:        # Check if window active
    window.minimize()

if window.exist:         # Check if window exist
    window.maximize()
