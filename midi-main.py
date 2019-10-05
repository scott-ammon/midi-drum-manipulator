import midi
import random

# implement a stack that records the previous note and tick here


# re-do all these functions as a separate file, and add logic
def transformKickEvent(event):
  return midi.NoteOnEvent(tick=event.tick, velocity=event.data[1], pitch=event.data[0])

def transformSnareEvent(event):
  return midi.NoteOnEvent(tick=event.tick, velocity=event.data[1], pitch=event.data[0])

def transformHiHatEvent(event):
  newVelocity = event.data[1] + random.randint(-25, 25)
  return midi.NoteOnEvent(tick=event.tick, velocity=event.data[1], pitch=event.data[0])

def transformEvent(event):
  # logic to transform event based on the note/instrument
  if event.data[0] == 36:
    return transformKickEvent(event)
  elif event.data[0] == 40:
    return transformSnareEvent(event)
  elif event.data[0] == 42:
    return transformHiHatEvent(event)
  else:
    return event

# Read in midi file to transform
pattern = midi.read_midifile("basic_drum.mid")
print pattern

# Instantiate new track to write midi to
newPattern = midi.Pattern()
track = midi.Track()
newPattern.append(track)

# Add track header and other info here?


# Loop through note events of track
for event in pattern[0]:
  if type(event) is midi.events.NoteOnEvent:
    # Send note to transorm function
    # modifiedNoteEvent = midi.NoteOnEvent(tick=event.tick, velocity=event.data[1], pitch=(event.data[0]+10))
    modifiedNoteEvent = transformEvent(event)
    track.append(modifiedNoteEvent)
    print("ORIGINAL: ", event)
    print("MODIFIED: ", modifiedNoteEvent)

# transform entire sequence of events with some sinusoidal function here
# extract this function out to a separate module
def modulateTrackTime(track):
  # calculate total length of track, use that to calculate modulation at each noteEvent tick
  return track

# Add end of track event and write out the transformed file
eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)
midi.write_midifile("transformed_drums.mid", newPattern)
    
