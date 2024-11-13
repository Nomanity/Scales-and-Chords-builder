notes = ('C', 'C♯', 'D', 'D♯','E', 'F', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B')
class Scale:
    def __init__(self, note):
        self.note = user_input
    pass
class Chord:
    def __init__(self, note):
        self.note = user_input
    pass
class GuitarNotation:
    pass

print ('In modern music there are 12 notes:', str(notes), 'Any scale or chord is builded from these notes with specific formula.', 'For example, the formula for major scale is: root, whole, whole, half, whole, whole, whole, half', sep = '\n')

pause_input = input(' ')
user_input = input('Please, choose the root note: ')
while user_input not in notes:
    print ('There isn\'t such note')
    user_input = input('Please, choose the root note: ')

scale_or_chord = input('Will it be a scale or a chord: ')


