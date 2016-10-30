# The problem
![](http://i.imgur.com/eDpzL8S.png)

At some point, Spotify started using some API to pop up media controls along with the volume when you move the volume slider on your keyboard/mouse/header/whatever. It's really big, and kind of annoying, especially if you're playing a video game.

# The solution
**MediaPopupModifier**. Version 1.0 hides the media controls by setting the width of the window using low level Windows APIs.

# Shop talk
I found the window with WinSpy++, hoping that the volume control and media controls would be two separate child windows which I could hide individually. Instead, I found that I could lower the width until the media controls were hidden.

![](http://i.imgur.com/8EbdBTV.gif)

# TODO
* A nice GUI with options for minimize to tray
* Change popup duration
* Option for removing the entire popup

# Download
Click on the Releases button above, and select the newest option.
