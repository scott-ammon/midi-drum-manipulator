import midi
from transforms import transformEvent

# Read in midi file to transform
pattern = midi.read_midifile("basic_drum.mid")

# Instantiate new track to write midi to
newPattern = midi.Pattern(tracks=[], resolution=480, format=1, tick_relative=True)
track = midi.Track()
newPattern.append(track)

# Loop through note events of track
for event in pattern[0]:
  if type(event) is midi.events.NoteOnEvent:
    modifiedNoteEvent = transformEvent(event)
    track.append(modifiedNoteEvent)
  elif type(event) is midi.events.NoteOffEvent:
    # add func call here to handle modulating note-off events
    track.append(event)
  else:
    track.append(event)

# Add end of track event and write out the transformed file
eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)
midi.write_midifile("transformed_drums.mid", newPattern)
print(newPattern)
    
