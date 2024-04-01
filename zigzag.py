import time, sys

# How many spaces to indent
indent = 0

# Whether the indentation is increasing or not
indentIncreasing = True

try:
    while True:
        print (' ' * indent, end='')
        print ('********')
        time.sleep(0.1)
        
        if indentIncreasing:
            indent += 1
            
            if indent == 20:
                indentIncreasing = False
        
        else:
            indent -= 1

            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()