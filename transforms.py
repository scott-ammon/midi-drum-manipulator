import midi
import random

# implement a stack that records the previous note and tick here

def randomize_velocity(velocity, min, max):
  if (velocity + max > 127):
    max = 127 - velocity
  if (velocity + min < 0):
    min = -velocity
  return velocity + random.randint(min, max)

def drag_note(tick, amount):
  return tick + random.randint(-amount, 0)

def rush_note(tick, amount):
  return tick + random.randint(0, amount)

def transform_kick_event(event):
  new_velocity = randomize_velocity(event.data[1], -10, 10)
  return midi.NoteOnEvent(tick=event.tick, velocity=new_velocity, pitch=event.data[0])

def transform_snare_event(event):
  new_velocity = randomize_velocity(event.data[1], -5, 25)
  newTick = rush_note(event.tick, 5)
  return midi.NoteOnEvent(tick=newTick, velocity=new_velocity, pitch=event.data[0])

def transform_hi_hat_event(event):
  new_velocity = randomize_velocity(event.data[1], -25, 25)
  newTick = rush_note(event.tick, 12)
  return midi.NoteOnEvent(tick=newTick, velocity=new_velocity, pitch=event.data[0])

def transform_event(event):
  if event.data[0] == 36:
    return transform_kick_event(event)
  elif event.data[0] == 40:
    return transform_snare_event(event)
  elif event.data[0] == 42:
    return transform_hi_hat_event(event)
  else:
    return event

# transform entire sequence of events with some sinusoidal function here
def modulate_track_time(track):
  # calculate total length of track, use that to calculate modulation at each noteEvent tick
  return track