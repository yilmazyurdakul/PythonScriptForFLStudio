# name=BehringerUMX250

# imports
# location C:\Users\**username**\Documents\Image-Line\FL Studio\Settings\Hardware\yyCustom

import mixer
import ui
import transport
import midi

# define variables
play_key = 97
stop_key = 96
record_key = 66
song_key = 67



def OnMidiMsg(event):
	event.handled = False
	if event.data1 > 0:
            if event.status == 176:	
                if event.data1 == play_key:
                    transport.start()
                    event.handled = True
                if event.data1 == stop_key:
                    transport.stop()
                    event.handled = True
                if event.data1 == record_key:
                    transport.record()
                    event.handled = True
                if event.data1 == song_key:
                    transport.setLoopMode()
                    event.handled = True
                    
                if event.data1 == 64:
                    transport.globalTransport(midi.FPT_Metronome, 1)
                    event.handled = True   
                   
                if event.data1 == 65:
                    if ui.getVisible(0) == 0: #if window is not visible
                        ui.showWindow(0) #make it visible
                        event.handled = True
                    else:
                        ui.hideWindow(0)  # if it is visible hide it
                        event.handled = True 
  
def OnControlChange(event):

 if event.data1 == 7: 
            mixer.setTrackVolume(0,(event.data2 / 127) * 0.8)
            event.handled = True
 if event.data1 == 91: 
            mixer.setTrackVolume(1,(event.data2 / 127) * 0.8)
            event.handled = True
 if event.data1 == 93: 
            mixer.setTrackVolume(2,(event.data2 / 127) * 0.8)
            event.handled = True
 if event.data1 == 74: 
            mixer.setTrackVolume(3,(event.data2 / 127) * 0.8)
            event.handled = True
 if event.data1 == 71: 
            mixer.setTrackVolume(4,(event.data2 / 127) * 0.8)
            event.handled = True
 if event.data1 == 73: 
            mixer.setTrackVolume(5,(event.data2 / 127) * 0.8)
            event.handled = True
 if event.data1 == 75: 
            mixer.setTrackVolume(6,(event.data2 / 127) * 0.8)
            event.handled = True
 if event.data1 == 72: 
            mixer.setTrackVolume(7,(event.data2 / 127) * 0.8)
            event.handled = True
 if event.data1 == 10: 
            mixer.setTrackVolume(8,(event.data2 / 127) * 0.8)
            event.handled = True