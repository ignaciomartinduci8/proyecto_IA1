import librosa


class ExtractAudioData:

    def getAllAudioData(self, path):

        y, sr = librosa.load(path)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfcc = mfcc.tolist()
        audioData = [mfcc]

        return audioData
