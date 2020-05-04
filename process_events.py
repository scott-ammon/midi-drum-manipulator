import midi

from transforms import transform_event

class MidiTrack:
  def __init__(self, pattern):
    self.pattern = pattern

    # Instantiate new track to write MIDI to
    self.new_pattern = midi.Pattern(tracks=[], resolution=pattern.resolution, format=1, tick_relative=True)
    self.track = midi.Track()
    self.new_pattern.append(self.track)

  def process_midi_events(self):
    # TODO Extract this to a separate function process_midi_events(pattern)
    diff_array = []
    # Modify each note event in the single track located at pattern[0]
    for event in self.pattern[0]:
      if type(event) is midi.events.NoteOnEvent:
        new_note_on = transform_event(event)
        self.track.append(new_note_on)
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
        self.track.append(new_note_off)
      else:
        self.track.append(event)

    # Add end of track event and write out the transformed MIDI file
    end_of_track = midi.EndOfTrackEvent(tick=1)
    self.track.append(end_of_track)