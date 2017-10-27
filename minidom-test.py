#!/usr/bin/python

from xml.dom import minidom
import untangle
import xmltodict
import os
import collections


if __name__ == "__main__":

	doOnce = False
	domList = []
	#composerList = ["bach", "mozart", "haydn", "beeth", "liszt", "rachmaninov", "schubert", "debussy", "ravel", "chopin"]


	for f in os.listdir("mozart"):
		if f.endswith((".xml")):
			print(":)") #To keep track of the progress
			name = 'mozart/' + f
			dom = minidom.parse(name)
			domList.append((f, dom))

		if doOnce == True:
			if len(domList) == 1:
				break



	songs = {}


	for i in range(0, len(domList)):
		song = domList[i][1]
		measures = song.getElementsByTagName('measure')
		measureList = []

		for j in range(0, len(measures)):
			measure = []

			measureOnePitches = measures[j].getElementsByTagName('step')
			measureOneOctave = measures[j].getElementsByTagName('octave')
			measureOneNoteLengths = measures[j].getElementsByTagName('type')

			standard_keys = ['note', 'octave', 'length']
			note = {key:"" for key in standard_keys}

			for k in range(0, len(measureOnePitches)):
				note['note'] = measureOnePitches[k].firstChild.nodeValue
				note['octave'] = measureOneOctave[k].firstChild.nodeValue
				note['length'] = measureOneNoteLengths[k].firstChild.nodeValue
				measure.append(note)

			measureList.append(measure)

		songs[domList[i][0]] = measureList


	for key in songs:
		print songs[key][0]

		