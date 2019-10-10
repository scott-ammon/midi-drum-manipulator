import midi
import random

# implement a stack that records the previous note and tick here

# add logic
def transformKickEvent(event):
  newVelocity = event.data[1] + random.randint(-10, 10)
  return midi.NoteOnEvent(tick=event.tick, velocity=newVelocity, pitch=event.data[0])

def transformSnareEvent(event):
  newVelocity = event.data[1] + random.randint(-5, 25)
  newTick = event.tick + random.randint(0,5)
  return midi.NoteOnEvent(tick=newTick, velocity=newVelocity, pitch=event.data[0])

def transformHiHatEvent(event):
  newVelocity = event.data[1] + random.randint(-25, 25)
  newTick = event.tick + random.randint(0,12)
  return midi.NoteOnEvent(tick=newTick, velocity=newVelocity, pitch=event.data[0])

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

# transform entire sequence of events with some sinusoidal function here
def modulateTrackTime(track):
  # calculate total length of track, use that to calculate modulation at each noteEvent tick
  return track