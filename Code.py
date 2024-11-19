notes = ('C', 'C#', 'D', 'D#','E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
scales_formulas = {
    'major scale': (2,2,1,2,2,2,1),
    'minor scale': (2,1,2,2,1,2,2),
    'major pentatonic scale': (2,2,3,2,3),
    'minor pentatonic scale': (3,2,2,3,2),
    'blues scale': (3,2,1,1,3,2)
    }
chords_formulas = {
    'major chord': (4,7),
    'minor chord': (3,7),
    'dominant 7 chord': (4,7,10),
    'power chord': (7),
    'sus2 chord': (2,7),
    'sus4 chord': (5,7)
    }
class Notes:
    def __init__(self, note, type):
        self.note = note
        self.type = type
    
    def build_scale(self):
        scale_list = []
        scale_list.append(self.note)
        note_pos = notes.index(self.note)
        for interval in scales_formulas[self.type]:
          note_pos += interval
          note_pos %= len(notes)
          scale_list.append(notes[note_pos])
        return scale_list
    
    def build_chord(self):
        chord_list = []
        chord_list.append(self.note)
        note_pos = notes.index(self.note)
        for interval in chords_formulas[self.type]:
          note_pos += interval
          note_pos %= len(notes)
          chord_list.append(notes[note_pos])
          note_pos = notes.index(self.note)
        return chord_list


def reset_check(input_string):
   if input_string in {'reset', 'exit', 'close', 'clear', 'start', 'refresh'}:
      return True
   else: 
      return False

def root_note_stage():
  user_input = input('Please, choose the root note: ')
  reset_check(user_input)
  while user_input not in notes or reset_check(user_input) == True:
    user_input = input('Please, choose the root note: ')
    reset_check(user_input)
  return user_input

def progression_stage():
  typo_filter = [scale for scale in scales_formulas] + [chord for chord in chords_formulas]
  user_progression = (input('What do you want to construct? ')).lower()
  reset_check(user_progression)
  while user_progression not in typo_filter or reset_check(user_progression) == True:
    if reset_check(user_progression) == True:
       root_note_stage()
    user_progression = (input('What do you want to construct? ')).lower()
    reset_check(user_progression)
  return user_progression

   
def Builder():
  user_note = root_note_stage()
  scale_chord = progression_stage()
  
  if 'scale' in scale_chord:
    user_scale = Notes(user_note, scale_chord)
    print(user_scale.build_scale())
  
  if 'chord' in scale_chord:
    user_chord = Notes(user_note, scale_chord)
    print(user_chord.build_chord())
  
  termination = input ('Type {} to terminate the program or press {} to run it again \n'.format('exit', 'enter'))
  return termination

notes_string = ''
for note in notes:
    if note != notes[-1]:
        notes_string += note + ', '
    else:
        notes_string += note + '.'
print ('In modern music there are 12 notes:', notes_string, 'Any scale or chord is builded from these notes with specific formula.', 'For example, the formula for major scale is: root, whole, whole, half, whole, whole, whole, half', sep = '\n')
 
pause_input = input('')


termination = Builder()
while termination != 'exit':
   termination = Builder()