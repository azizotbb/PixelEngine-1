#!/bin/bash

# Open a new terminal window and run PixelEngine
osascript -e 'tell application "Terminal" 
    do script "cd '\''$(dirname $0)'\'' && ./PixelEngine"
    activate
end tell'
