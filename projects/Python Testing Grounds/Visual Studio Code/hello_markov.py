import numpy    as np
import pandas   as pd

# Collection of lists containing notes.
# Each note occurs in order on a measure of music.
list_1 = ['A', 'B', 'C', 'C#', 'D', 'E', 'F', 'F#', 'G', 'G#'   ]
list_2 = ['C', 'C', 'F', 'C#', 'G#', 'A', 'B', 'A', 'A', 'F#'   ]
list_3 = ['C', 'A', 'A', 'F', 'E', 'B', 'B', 'C', 'F', 'E'      ]
list_4 = ['E', 'E', 'F', 'B', 'F#', 'F', 'A', 'B', 'B', 'B'     ]

# Data structure encapuslating our Markov Chain.
# Each unique note is paired with a dictionary defining
# possible notes which can occur after it.

# The possible notes comprise of occurances (measuring how
# many of these notes follow our current note), and probability
# of this note occuring.
notes = {
    'C'     : {
        'C'     : {'Occurances' : 0, 'Probability' : 0.0},
        'C#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'D'     : {'Occurances' : 0, 'Probability' : 0.0},
        'D#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'E'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'G'     : {'Occurances' : 0, 'Probability' : 0.0},
        'G#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'A'     : {'Occurances' : 0, 'Probability' : 0.0},
        'A#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'B'     : {'Occurances' : 0, 'Probability' : 0.0}
        },
    'C#'    : {
        'C'     : {'Occurances' : 0, 'Probability' : 0.0},
        'C#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'D'     : {'Occurances' : 0, 'Probability' : 0.0},
        'D#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'E'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'G'     : {'Occurances' : 0, 'Probability' : 0.0},
        'G#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'A'     : {'Occurances' : 0, 'Probability' : 0.0},
        'A#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'B'     : {'Occurances' : 0, 'Probability' : 0.0}
        },
    'D'     : {
        'C'     : {'Occurances' : 0, 'Probability' : 0.0},
        'C#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'D'     : {'Occurances' : 0, 'Probability' : 0.0},
        'D#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'E'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'G'     : {'Occurances' : 0, 'Probability' : 0.0},
        'G#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'A'     : {'Occurances' : 0, 'Probability' : 0.0},
        'A#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'B'     : {'Occurances' : 0, 'Probability' : 0.0}
        },
    'D#'    : {
        'C'     : {'Occurances' : 0, 'Probability' : 0.0},
        'C#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'D'     : {'Occurances' : 0, 'Probability' : 0.0},
        'D#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'E'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'G'     : {'Occurances' : 0, 'Probability' : 0.0},
        'G#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'A'     : {'Occurances' : 0, 'Probability' : 0.0},
        'A#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'B'     : {'Occurances' : 0, 'Probability' : 0.0}
        },
    'E'     : {
        'C'     : {'Occurances' : 0, 'Probability' : 0.0},
        'C#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'D'     : {'Occurances' : 0, 'Probability' : 0.0},
        'D#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'E'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'G'     : {'Occurances' : 0, 'Probability' : 0.0},
        'G#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'A'     : {'Occurances' : 0, 'Probability' : 0.0},
        'A#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'B'     : {'Occurances' : 0, 'Probability' : 0.0}
        },
    'F'     : {
        'C'     : {'Occurances' : 0, 'Probability' : 0.0},
        'C#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'D'     : {'Occurances' : 0, 'Probability' : 0.0},
        'D#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'E'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'G'     : {'Occurances' : 0, 'Probability' : 0.0},
        'G#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'A'     : {'Occurances' : 0, 'Probability' : 0.0},
        'A#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'B'     : {'Occurances' : 0, 'Probability' : 0.0}
        },
    'F#'    : {
        'C'     : {'Occurances' : 0, 'Probability' : 0.0},
        'C#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'D'     : {'Occurances' : 0, 'Probability' : 0.0},
        'D#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'E'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'G'     : {'Occurances' : 0, 'Probability' : 0.0},
        'G#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'A'     : {'Occurances' : 0, 'Probability' : 0.0},
        'A#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'B'     : {'Occurances' : 0, 'Probability' : 0.0}
        },
    'G'     : {
        'C'     : {'Occurances' : 0, 'Probability' : 0.0},
        'C#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'D'     : {'Occurances' : 0, 'Probability' : 0.0},
        'D#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'E'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'G'     : {'Occurances' : 0, 'Probability' : 0.0},
        'G#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'A'     : {'Occurances' : 0, 'Probability' : 0.0},
        'A#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'B'     : {'Occurances' : 0, 'Probability' : 0.0}
        },
    'G#'    : {
        'C'     : {'Occurances' : 0, 'Probability' : 0.0},
        'C#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'D'     : {'Occurances' : 0, 'Probability' : 0.0},
        'D#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'E'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'G'     : {'Occurances' : 0, 'Probability' : 0.0},
        'G#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'A'     : {'Occurances' : 0, 'Probability' : 0.0},
        'A#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'B'     : {'Occurances' : 0, 'Probability' : 0.0}
        },
    'A'     : {
        'C'     : {'Occurances' : 0, 'Probability' : 0.0},
        'C#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'D'     : {'Occurances' : 0, 'Probability' : 0.0},
        'D#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'E'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'G'     : {'Occurances' : 0, 'Probability' : 0.0},
        'G#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'A'     : {'Occurances' : 0, 'Probability' : 0.0},
        'A#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'B'     : {'Occurances' : 0, 'Probability' : 0.0}
        },
    'A#'    : {
        'C'     : {'Occurances' : 0, 'Probability' : 0.0},
        'C#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'D'     : {'Occurances' : 0, 'Probability' : 0.0},
        'D#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'E'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'G'     : {'Occurances' : 0, 'Probability' : 0.0},
        'G#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'A'     : {'Occurances' : 0, 'Probability' : 0.0},
        'A#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'B'     : {'Occurances' : 0, 'Probability' : 0.0}
        },
    'B'     : {
        'C'     : {'Occurances' : 0, 'Probability' : 0.0},
        'C#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'D'     : {'Occurances' : 0, 'Probability' : 0.0},
        'D#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'E'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F'     : {'Occurances' : 0, 'Probability' : 0.0},
        'F#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'G'     : {'Occurances' : 0, 'Probability' : 0.0},
        'G#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'A'     : {'Occurances' : 0, 'Probability' : 0.0},
        'A#'    : {'Occurances' : 0, 'Probability' : 0.0},
        'B'     : {'Occurances' : 0, 'Probability' : 0.0}
        }
}

# Store all data in a list.
training_data = [list_1, list_2, list_3, list_4]

# Iterate through each list of notes.
for i in range(0, len(training_data)):
    # Iterate up until the penultimate note for the current list.
    for j in range(0, len(training_data[i])-1):
        # Take the current note and the note following it.
        current_note    = training_data[i][j     ]
        next_note       = training_data[i][j+1   ]
        
        # Increment the occurance count for the subsequent note.
        notes[next_note][current_note]['Occurances'] += 1
        
# Calculate the probability of each note occuring based on the current note.
# Count the number of occurances for ALL notes, then divide each
# note's occurances by this subtotal to yield the probability...

# Convert dictionary into convenient Pandas DataFrame.
notes_df = pd.DataFrame.from_dict(notes)

# Increment target notes.
for i in range(0, len(notes_df.values)):
    subtotal_occurances = 0
    # Count how many notes occur ahead of the target note.
    for j in range(0, len(notes_df.iloc[i].values)):
        subtotal_occurances = subtotal_occurances + notes_df.iloc[j][i]['Occurances']
    
    print("Notes following {}:\t {}".format(notes_df.iloc[i].name, subtotal_occurances))
    # If a note is followed by at least one other note, calculate its probability of occurance.
    if subtotal_occurances > 0:
        # Determine the probability of a note occuring ahead of the target note.           
        for j in range(0, len(notes_df.iloc[i].values)):
            notes_df.iloc[j][i]['Probability'] = float(notes_df.iloc[j][i]['Occurances'] / subtotal_occurances).__round__(5)
            
# Utilize the dataset to generate a musical score.
# This can be achieved with a single seed (musical note), then appending
# a note ahead of it based on a predetermined probability.

# Our seed will be a single musical note.
# Let us say we want to generate a musical score of 100 notes.
seed        = 'C'
notes       = [seed]
note_count  = 100

for i in range(0, note_count):
    # Now we want to access the notes in our list.
    # For each note we encounter, we can reference the probabilities
    # for each subsequent note occuring via the DataFrame made earlier.
    # These probabilities can be interpreted as ratios, the abundance
    # of a particular note in a list for a random number generator.
    pass
