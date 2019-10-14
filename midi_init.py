import midi
from transforms import transformEvent

# Read in MIDI file to transform
pattern = midi.read_midifile("basic_drum.mid")

# Instantiate new track to write MIDI to
newPattern = midi.Pattern(tracks=[], resolution=pattern.resolution, format=1, tick_relative=True)
track = midi.Track()
newPattern.append(track)

diffArray = []
# Modify each note event in the single track located at pattern[0]
for event in pattern[0]:
  if type(event) is midi.events.NoteOnEvent:
    newNoteOn = transformEvent(event)
    track.append(newNoteOn)
    diffArray.append({ 
      "inst": event.data[0], 
      "diff": newNoteOn.tick - event.tick
    })
  elif type(event) is midi.events.NoteOffEvent:
    for obj in diffArray:
      if obj["inst"] == event.data[0]:
        newTick = event.tick + obj["diff"]
        diffArray.remove(obj)
      else:
        newTick = event.tick
    newNoteOff = midi.NoteOffEvent(tick=newTick, velocity=event.data[1], pitch=event.data[0])
    track.append(newNoteOff)
  else:
    track.append(event)

# Add end of track event and write out the transformed MIDI file
eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)
midi.write_midifile("output_transformed.mid", newPattern)
    
