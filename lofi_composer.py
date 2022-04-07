from midiutil.MidiFile import MIDIFile
from midiutil import MIDIFile
import random
from notes import major_harmonic_field

MyMIDI = MIDIFile(1) 
track    = 0
channel  = 0
time     = 0    # In beats
duration = 4    # In beats
volume   = 100  # 0-127, as per the MIDI standard
MyMIDI.addProgramChange(track, channel, time, 4) # 4 IS FOR CHOOSING PIANO 'RHODES'

scale = random.choice(major_harmonic_field) #RANDOMLY CHOOSE A SCALE
chords = []
# RANDOMLY PICK 4 CHORDS THAT ARE IN INSIDE THE PREVIOUSLY CHOSEN SCALE
for i in range(4): 
    x = random.choice(scale)     
    chords.append(x) # CHORDS WILL BE TUPLES INSIDE A LIST, E.G: [(26, 29, 33) (26, 29, 33) (33, 24, 28) (34, 26, 29)]
    
# UNPACKING THE NOTES SO ALL OF THEM WILL BE STORED IN A LIST
notes_unp = []
for x in range (4):
    for i in range(3):
        notes_unp.append(chords[x][i])
tone = random.choice(range(3,6)) # CHOOSING A TONE FOR THE NOTES
notes_unp = [x * tone for x in notes_unp]


duration = 4  # DURATION OF CHORDS
c_time = 0  # WHE THE CHORDS START TO BE PLAYED
m_duration = 1  # DURATION OF MELODY NOTES
tempo = random.choice(range(60,80))
MyMIDI.addTempo(0, 0, tempo)
c_volume = 100  # CHORDS VOLUME
m_time = duration - 2  # MELODIES START TO BE PLAYED 2 SECONDS BEFORE THE NEXT CHORD
song_duration = random.choice(range(8,12)) #HOW MANY TIMES THE CHOSEN CHORDS(4) WILL BE REPEATED ALONG WITH THE MELODY

# PLAYING THE NOTES
for x in range(song_duration):
    for i in range(4):
        MyMIDI.addNote(track,channel, chords[i][0], c_time, duration,c_volume)
        MyMIDI.addNote(track,channel, chords[i][1], c_time, duration,c_volume)
        MyMIDI.addNote(track,channel, chords[i][2], c_time, duration,c_volume)

        m_1 = random.choice(chords[i]) # MELODY NOTe 1
        m_2 = random.choice(chords[i]) # MELODY NOTe 2
        MyMIDI.addNote(track,channel, m_1, m_time, m_duration,volume)
        MyMIDI.addNote(track,channel, m_2, m_time + 1, m_duration,volume)
        c_time = c_time + duration
        m_time = (c_time * 2) -1
   
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

