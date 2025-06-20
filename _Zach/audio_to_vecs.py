from os import PathLike
import numpy as np
import librosa

def audio_to_vecs(audiofile:PathLike):
	'''
	Accept a path to a file. Open it, and process.
	Cut audio into pieces
	Discrete Fourier Transform (DFT)
			Use library (import)
	Return vectors
	'''
	audio = path_to_audio(audiofile)
	chopped_audio = chop_audio_file(audio)
	ft_chopped_audio = np.array([])
	for segment in chopped_audio:
		ft_chopped_audio.append(process_segment(segment))
	vecs = ft_chopped_audio.tolist()
	return vecs

def path_to_audio(audiofile:PathLike)->np.ndarray:
	audio, sr = librosa.load(audiofile,sr=None)
	return audio

def chop_audio_file(audio:np.ndarray)->np.ndarray[np.ndarray]:
	pass
	#return segs

def process_segment(audio_segment:np.ndarray,thresh:int=10)->np.ndarray:
	pass
	# ft_seg = discrete_fourier_transform(audio_segment)
	# # if freq(ft_seg)<thresh: 0, else ft_seg
	# pass

def discrete_fourier_transform(segment:np.ndarray)->np.ndarray:
	pass

if __name__ == '__main__':
	audio_to_vecs()