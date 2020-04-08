import midi
from transforms import transform_event

pattern = midi.read_midifile("basic_drum.mid")

# Instantiate new track to write MIDI to
new_pattern = midi.Pattern(tracks=[], resolution=pattern.resolution, format=1, tick_relative=True)
track = midi.Track()
new_pattern.append(track)

# TODO Extract this to a separate function eventIterator(pattern)
diff_array = []
# Modify each note event in the single track located at pattern[0]
for event in pattern[0]:
  if type(event) is midi.events.NoteOnEvent:
    new_note_on = transform_event(event)
    track.append(new_note_on)
    diff_array.append({ 
      "inst": event.data[0], 
      "diff": new_note_on.tick - event.tick
    })
  elif type(event) is midi.events.NoteOffEvent:
    for obj in diff_array:
      if obj["inst"] == event.data[0]:
        new_tick = event.tick + obj["diff"]
        diff_array.remove(obj)
      else:
        new_tick = event.tick
    new_note_off = midi.NoteOffEvent(tick=new_tick, velocity=event.data[1], pitch=event.data[0])
    track.append(new_note_off)
  else:
    track.append(event)

# Add end of track event and write out the transformed MIDI file
end_of_track = midi.EndOfTrackEvent(tick=1)
track.append(end_of_track)
midi.write_midifile("output_transformed.mid", new_pattern)