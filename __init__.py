#!/usr/bin/python
# -*- coding: utf-8 -*-

# schimpfwort.py
#by SullenLook

from random import randint
from plugin import *
import os, random



class schimpfwort(Plugin):

    @register("de-DE",".*Du .*fotze.*|.*Fotze.*|.*Du .*nutte.*|.*Nutte.*|.*Du .*drecksau.*|.*Drecksau.*|.*Du .*schlampe.*|.*Schlampe.*|.*Du .*hure.*|.*Hure.*|.*Du .*Kackvogel.*|.*Kackvogel.*|.*Du .*Wichser.*|.*Wichser.*|.*Du .*Lutscher.*|.*Lutscher.*|.*Du .*Arschloch.*|.*Arschloch.*|.*Du .*Penner.*|.*Penner.*|.*Du .*Assi.*|.*Assi.*|.*Du .*Mistvieh.*|.*Mistvieh.*|.*Mist .*Vieh.*|.*Du .*Mist .*Vieh.*|.*Du .*Dreckvieh.*|.*Du .*Dreck .*Vieh.*|.*Dreckvieh.*|.*Dreck .*Vieh.*|.*Du .*Drecksau.*|.*Du .*Dreck .*Sau.*|.*Drecksau.*|.*Dreck .*Sau.*|.*Du .*Mistschwein.*|.*Du .*Mist .*Schwein.*|.* Mistschwein.*|.*Mist .*Schwein.*|.*Du .*Dreckschwein.*|.*Du .*Dreck .*Schwein.*|.*Dreckschwein.*|.*Dreck .*Schwein.*|.*Du .*Mongo.*|.*Mongo.*|.*Du .*Blödmann.*|.*Blödmann.*|.*Du .*Stricher.*|.*Stricher.*|.*Du .*Hurensohn.*|.*Hurensohn.*|.*Du .*bist .*Behindert.*|.*Du .*Kloppi.*|.*Kloppi.*|.*Du .*Hilli.*|.*Du .*Reha .*Hilli.*|.*Hilli.*|.*Reha .*Hilli.*|.*Du .*Spast.*|.*Spast.*|.*Du .*Fisch.*|.*Du .*Kloppholz.*|.*Kloppholz.*|.*Du .*Klopp .*Holz.*|.*Klopp .*Holz.*|.*Du .*Hannes.*|.*Hannes.*|.*Du .*Hesslo.*|.*Hesslo.*|.*Du .*Dummbrot.*|.*Du .*Dumm .*Brot.*|.*Dummbrot.*|.*Dumm .*Brot.*|.*Du .*Wichskopf.*|.*Du .*Wichs .*Kopf.*|.*Du .*Wixkopf.*|.*Du .*Wix .*Kopf.*|.*Wichskopf.*|.*Wixkopf.*|.*Du .*Vollpfosten.*|.*Du .*Voll .*Pfosten.*|.*Vollpfosten.*|.*Voll .*Pfosten.*|.*Du .*Pfirsich.*|.*Pfirsich.*|.*Du .*Hackfresse.*|.*Du .*Hack .*Fresse.*|.*Hackfresse.*|.*Hack .*Fresse.*|.*Du .*Gesichtsgulasch.*|.*Du .*Gesichts .*Gulasch.*|.*Gesichtsgulasch.*Gesichts .*Gulasch.*|.*Du .*Opfer.*|.*Opfer.*|.*Du .*Fisch.*|.*Fisch.*")
    def st_catfact(self, speech, language):
        if language == 'de-DE':
            filename = "./plugins/schimpfwort/schimpfwort.txt"
            file = open(filename, 'r')

            #Get the total file size
            file_size = os.stat(filename)[6]

            #Seek to a place int he file which is a random distance away
            #Mod by the file size so that it wraps around to the beginning
            file.seek((file.tell()+random.randint(0, file_size-1))%file_size)

            #Dont use the first readline since it may fall in the middle of a line
            file.readline()

            #this will return the next (complete) line from the file
            line = file.readline()

            #here is the random line
            self.say(line)

        self.complete_request()

