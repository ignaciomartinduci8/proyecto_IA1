import os
from ExtractAudioData import ExtractAudioData
from Audio import Audio
import json


class Knn:

    def __init__(self):
        self.audios = []
        self.audioProcessor = ExtractAudioData()

    def learn(self):

        directories = os.listdir("dataset/audio")

        for directory in directories:
            files = os.listdir("dataset/audio/" + directory)
            for file in files:

                audioData = self.audioProcessor.getAllAudioData("dataset/audio/" + directory + "/" + file)

                self.audios.append(Audio(directory, audioData))

        for audio in self.audios:

            tag, mfcc = audio.getData()

            with open("./clusters/audioClusters.json", 'r') as f:
                elements = json.load(f)

            elements.append({"tag": tag, "mfcc": mfcc})

            with open("./clusters/audioClusters.json", 'w') as f:

                json.dump(elements, f)

    def evaluate(self):
        pass