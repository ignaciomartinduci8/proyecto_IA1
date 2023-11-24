import os
import json
import sounddevice as sd

from Knn import Knn
from Kmeans import Kmeans


class Controller:

    def __init__(self):

        self.knn = Knn()
        self.kmeans = Kmeans()
        self.checkDirs()
        self.genClusters()

    def checkDirs(self):

        directories = os.listdir()

        if "dataset" not in directories:
            os.mkdir("dataset")

        if "clusters" not in directories:
            os.mkdir("clusters")

        datasetDirs = os.listdir("dataset")
        if "audio" not in datasetDirs:
            os.mkdir("dataset/audio")

        if "image" not in datasetDirs:
            os.mkdir("dataset/image")

        audioDirs = os.listdir("dataset/audio")
        if "banana" not in audioDirs:
            os.mkdir("dataset/audio/banana")
        if "manzana" not in audioDirs:
            os.mkdir("dataset/audio/manzana")
        if "naranja" not in audioDirs:
            os.mkdir("dataset/audio/naranja")
        if "pera" not in audioDirs:
            os.mkdir("dataset/audio/pera")
        if "userGen" not in audioDirs:
            os.mkdir("dataset/audio/userGen")

        imageDirs = os.listdir("dataset/image")
        if "banana" not in imageDirs:
            os.mkdir("dataset/image/banana")
        if "manzana" not in imageDirs:
            os.mkdir("dataset/image/manzana")
        if "naranja" not in imageDirs:
            os.mkdir("dataset/image/naranja")
        if "pera" not in imageDirs:
            os.mkdir("dataset/image/pera")

    def genClusters(self):

        files = os.listdir("clusters")

        if "audioClusters.json" not in files:
            with open("clusters/audioClusters.json", 'a') as f:

                json.dump([], f)

        else:
            with open("clusters/audioClusters.json", 'r') as f:

                try:
                    elements = json.load(f)
                except json.decoder.JSONDecodeError:

                    elements = []
                    json.dump(elements, f)

                audios = []

                for directory in os.listdir("dataset/audio"):

                    for audio in os.listdir("dataset/audio/" + directory):

                        audios.append(audio)

                if len(elements) != len(audios):
                    self.knn.learn()

        if "imageClusters.json" not in files:
            with open("clusters/imageClusters.json", 'a') as f:
                json.dump([], f)

        else:
            with open("clusters/imageClusters.json", 'r') as f:

                try:
                    elements = json.load(f)

                except json.decoder.JSONDecodeError:
                    elements = []
                    json.dump(elements, f)

                images = []

                for directory in os.listdir("dataset/image"):

                        for image in os.listdir("dataset/image/" + directory):

                            images.append(image)

                if len(elements) != len(images):
                    self.kmeans.learn()

    def resetKnowledge(self):

        files = os.listdir("clusters")

        if "audioClusters.json" in files:
            os.remove("clusters/audioClusters.json")

        if "imageClusters.json" in files:
            os.remove("clusters/imageClusters.json")

        self.genClusters()

    def addAudio(self):

        fs = 44100
        duration = 3

        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()
        sd.play(myrecording, fs)
        sd.wait()


