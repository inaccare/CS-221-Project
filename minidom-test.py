#!/usr/bin/python

from xml.dom import minidom
import os
import collections

# ToDo:
# Figure out how to scrape accidentals for the specific note
# Finish commenting all this code
# Use sentiment assigment code to implement machine learning baseline on accidental count
# Figure out any other parameters from the XML file we might need

if __name__ == "__main__":

	doOnce = True #Allows us to control whether to parse multiple songs or just one
	domList = []
	#composerList = ["bach", "mozart", "haydn", "beeth", "liszt", "rachmaninov", "schubert", "debussy", "ravel", "chopin"]

	# Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order
	for f in os.listdir("mozart"):
		if f.endswith((".xml")): # if the file is an XML file
			name = 'mozart/' + f #filepath
			dom = minidom.parse(name) #Return a Document from the given input
			domList.append((f, dom)) #Add (document name, document) to domList 

		if doOnce == True: #If we only want to parse a single song then break
			if len(domList) == 1:
				break
	songs = {}

	#Loop over every song
	for i in range(0, len(domList)):
		song = domList[i][1] #song = document pertaining to song
		measures = song.getElementsByTagName('measure') #measures is a NodeList where each measure is a Node
		measureList = []

		for j in range(0, len(measures)):
			measure = []

			measureOnePitches = measures[j].getElementsByTagName('step')
			measureOneOctave = measures[j].getElementsByTagName('octave')
			measureOneNoteLengths = measures[j].getElementsByTagName('type')
			measureOneAccidentals = measures[j].getElementsByTagName('accidental')

			standard_keys = ['note', 'octave', 'length', 'accidental']
			note = {key:"" for key in standard_keys}

			for k in range(0, len(measureOnePitches)):
				note['note'] = measureOnePitches[k].firstChild.nodeValue
				note['octave'] = measureOneOctave[k].firstChild.nodeValue
				note['length'] = measureOneNoteLengths[k].firstChild.nodeValue
				print len(measureOneAccidentals)
				if len(measureOneAccidentals) > 0:
					note['accidental'] = measureOneAccidentals[k].firstChild.nodeValue
				print note
				measure.append(note)

			measureList.append(measure)

		songs[domList[i][0]] = measureList


	for key in songs:
		print songs[key][0]

		
