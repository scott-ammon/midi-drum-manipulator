import midi

from process_events import MidiTrack

pattern = midi.read_midifile("basic_drum.mid")

midi_track = MidiTrack(pattern)
midi_track.process_midi_events()

midi.write_midifile("output_transformed.mid", midi_track.new_pattern)