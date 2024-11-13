notes = ('C', 'C#', 'D', 'D#','E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
# major_scale = (2,2,1,2,2,2,1)
# minor_scale = (2,1,2,2,1,2,2)
# major_pentatonic = (2,2,3,2,3)
# minor_pentatonic = (3,2,2,3,2)
# blues_scale = (3,2,1,1,3,2)
scales_formulas = {
        'major': (2,2,1,2,2,2,1),
        'minor': (2,1,2,2,1,2,2),
        'major_pentatonic': (2,2,3,2,3),
        'minor_pentatonic': (3,2,2,3,2),
        'blues': (3,2,1,1,3,2)
        }
class Scale:
    
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

class Chord:
    def __init__(self, note):
        self.note = note
    pass
class GuitarNotation:
    pass

def Builder():
  user_input = input('Please, choose the root note: ')
  while user_input not in notes:
      print ('There isn\'t such note')
      user_input = input('Please, choose the root note: ')

  print ('What are you want to construct?' + ' You can choose from major/minor scale with penta/hepta option or blues scale')
  scale_or_chord = input('Please, type lowercases only: ')
  if scale_or_chord == 'major scale':
    user_scale = Scale(user_input, 'major')
    print(user_scale.build_scale())

notes_string = ''
for note in notes:
    if note != notes[-1]:
        notes_string += note + ', '
    else:
        notes_string += note + '.'
print ('In modern music there are 12 notes:', notes_string, 'Any scale or chord is builded from these notes with specific formula.', 'For example, the formula for major scale is: root, whole, whole, half, whole, whole, whole, half', sep = '\n')
 
pause_input = input(' ')

Builder()

