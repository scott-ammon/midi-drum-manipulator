import midi
from transforms import transformEvent

# Read in midi file to transform
pattern = midi.read_midifile("basic_drum.mid")

# Instantiate new track to write midi to
newPattern = midi.Pattern(tracks=[], resolution=pattern.resolution, format=1, tick_relative=True)
track = midi.Track()
newPattern.append(track)

diffArray = []
# Loop through note events of track
for event in pattern[0]:
  if type(event) is midi.events.NoteOnEvent:
    newNoteOn = transformEvent(event)
    track.append(newNoteOn)
    diffArray.append({ 
      "instrument": event.data[0], 
      "diff": newNoteOn.tick - event.tick
    })
  elif type(event) is midi.events.NoteOffEvent:
    for obj in diffArray:
      if obj["instrument"] == event.data[0]:
        newTick = event.tick + obj["diff"]
        diffArray.remove(obj)
      else:
        newTick = event.tick
    newNoteOff = midi.NoteOffEvent(tick=newTick, velocity=event.data[1], pitch=event.data[0])
    track.append(newNoteOff)
  else:
    track.append(event)

# difference between event.tick and newNoteOn
# Add end of track event and write out the transformed file
eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)
midi.write_midifile("transformed_drums.mid", newPattern)
print("OLD: ")
print(pattern)
print("NEW: ")
print(newPattern)
    
