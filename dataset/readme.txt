The columns in the drawing files are as follows:

timestamp (approximate)
x coordinate
y coordinate
pen angle in x plane
pen angle in y plane
pressure

Each row is a sample of the pen's state. Rather than using the timestamp, assume a constant sampling rate of 200Hz. The x and y coordinates are between 0 and 1. These should be mapped to the tablet's true dimensions (20.3cm x 32.5cm) in order to correct the aspect ratio.

Metadata for each of the subjects can be found in the two .sav files. These are in SPSS format (which should be on the department's computers), though you can also open them in the open source PSPP software.

The drawing files are organised into patients and controls directories. The numeric part of each filename shows the ID and the date, although not all of them include a date.

The Diagnosis.csv file indicates whether each patient is PD (normal cognition), PD-MCI (mild cognitive impairment) or PDD (dementia). Further info on clinical scores (e.g. MOCA) is also available if required.

For the pentagon spiral drawings, each subject carried out two repeats using each hand. The simplest approach would be to use just the first repeat of the dominant hand.
