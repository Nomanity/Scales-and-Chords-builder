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

    def related_chords(self):
        pass
    
class GuitarNotation:
    pass

def Builder():
  user_input = input('Please, choose the root note: ')
  while user_input not in notes:
      print ('There isn\'t such note')
      user_input = input('Please, choose the root note: ')

  typo_filter = [scale for scale in scales_formulas] + [chord for chord in chords_formulas]
  user_progression = (input('What do you want to construct? ')).lower()

  while user_progression not in typo_filter:
     user_progression = (input('What do you want to construct? ')).lower()
  
  if 'scale' in user_progression:
    user_scale = Notes(user_input, user_progression)
    print(user_scale.build_scale())
  
  if 'chord' in user_progression:
     user_chord = Notes(user_input, user_progression)
     print(user_chord.build_chord())

notes_string = ''
for note in notes:
    if note != notes[-1]:
        notes_string += note + ', '
    else:
        notes_string += note + '.'
print ('In modern music there are 12 notes:', notes_string, 'Any scale or chord is builded from these notes with specific formula.', 'For example, the formula for major scale is: root, whole, whole, half, whole, whole, whole, half', sep = '\n')
 
pause_input = input(' ')

Builder()

