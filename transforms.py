import midi
import random

# implement a stack that records the previous note and tick here

def randomizeVelocity(velocity, min, max):
  return velocity + random.randint(min, max)

def dragNote(tick, amount):
  return tick + random.randint(-amount, 0)

def rushNote(tick, amount):
  return tick + random.randint(0, amount)

def transformKickEvent(event):
  newVelocity = randomizeVelocity(event.data[1], -10, 10)
  return midi.NoteOnEvent(tick=event.tick, velocity=newVelocity, pitch=event.data[0])

def transformSnareEvent(event):
  newVelocity = randomizeVelocity(event.data[1], -5, 25)
  newTick = rushNote(event.tick, 5)
  return midi.NoteOnEvent(tick=newTick, velocity=newVelocity, pitch=event.data[0])

def transformHiHatEvent(event):
  newVelocity = randomizeVelocity(event.data[1], -25, 25)
  newTick = rushNote(event.tick, 12)
  return midi.NoteOnEvent(tick=newTick, velocity=newVelocity, pitch=event.data[0])

def transformEvent(event):
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