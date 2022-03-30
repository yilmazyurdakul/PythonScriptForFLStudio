# name=yyCustom

# imports
# location C:\Users\**username**\Documents\Image-Line\FL Studio\Settings\Hardware\yyCustom

import mixer
import ui
import transport

# define variables
play_this_song = 44
stop_key = 45
show_mx = 46
show_pl = 53

def OnMidiMsg(event):
	event.handled = False
	if event.data1 > 0:
            if event.status == 144:	
                if event.data1 == play_this_song:
                    transport.start()
                    event.handled = True
                if event.data1 == stop_key:
                    transport.stop()
                    event.handled = True
                if event.data1 == show_mx:
                    if ui.getVisible(0) == 0: #if window is not visible
                        ui.showWindow(0) #make it visible
                        ui.setFocused(0)
                        event.handled = True
                    else:
                        ui.hideWindow(0)  # if it is visible hide it
                        event.handled = True 
                if event.data1 == show_pl:
                    if ui.getVisible(2) == 0:
                        ui.showWindow(2)
                        event.handled = True
                    else:
                        ui.hideWindow(2)
                        event.handled = True
  
def OnControlChange(event):

 if 1 <= event.data1 <= 5: #I have 5 faders. You can edit fader channels or use this block to use every single fader.
            mixer.setTrackVolume((event.data1 - 1),(event.data2 / 127) * 0.8)
            event.handled = True
