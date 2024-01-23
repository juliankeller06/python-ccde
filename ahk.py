import ahk

def my_callback():
    print('Hello callback!')

# when WIN + n is pressed, fire `my_callback`
ahk.add_hotkey('#n', callback=my_callback)
ahk.start_hotkeys()  # start the hotkey process thread
ahk.block_forever()  # not strictly needed in all scripts -- stops the script from exiting; sleep forever