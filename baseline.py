#baseline testing 
import random
import math
import numpy
import random
import collections
import sys
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm

def main():
	# code here to grab sparse vector containing needed info
	# -> means data given by the parser
	# *** means data given to the classifier
	# -> notes = [88 1 34 2 6 67 ...]
	# *** noteFrequency = {"1":29, "2":32, ..., "87":14, "88":6}
	# noteNGram = [[5, 8, 43], [8, 43, 88], [43, 88, 12], ...]
	# *** noteNGramFrequency = {[5, 8, 43]:13, [21, 45, 88]:9, ...}
	# *** noteRange = int (highest note minus lowest note)
	# -> *** key = (i.e. A#)
	# -> pitchClass = [1 2 4 1 6 7 12 11 3 5 8 9 10 7 5 2 3 4, ...] [=] each note in the song normalized to its pitch class as an array
	# *** pitchClassFrequency = {"1": 127; "2": 312; "3":221; "4":123, ..., "12":178} as a default dict sparse vector
	# *** pitchGradient [=] variance in changes in 
	# -> chordsRoman = [V, III, I, VII, ...]
	# *** chordFrequencyRoman = {"I":2, "II":5, "III":10, ...}
	# chordNGramRoman = [[V, III, I], [III, I, VII], [I, VII, III], ...] [=] chord progression
	# *** chordNGramFrequencyRoman = {[I V VII]:8, [I II V]:10, ...}

	noteFrequency = defaultdict(int)
	for note in notes:
		noteFrequency[note] = noteFrequency[note] + 1
	composers = ["Bach", "Beethoven", "Chopin", "Debussy", "Haydn", "Liszt", "Mozart", "Rachmaninov", "Ravel", "Schubert"]

	print baselineClassifierNaiveBayes(noteFrequency, notes)

def baselineClassifierNaiveBayes(noteFrequency, notes):
	totalNoteCount = sum(notes)
	probPitch = collections.defaultdict(float)
	for pitchClass in noteFrequency:
		probPitch[pitchClass] = float(noteFrequency[pitchClass])/totalNoteCount

	clf = svm.SVC(gamma=0.001, C=100.)
	clf.fit(notes.data[:-1], notes.target[:-1])

	clf.predict(notes.data[-1:])

if __name__ == '__main__':
	main()