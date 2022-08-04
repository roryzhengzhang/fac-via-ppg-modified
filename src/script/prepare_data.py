from genericpath import isfile
import os
import glob
from random import shuffle

pairs = []
refer_name = 'bdl'
mode = 'ppg'
root = "/home/zheng_zhang7/fac-via-ppg"

for f in glob.glob(os.path.join(root, f"data_wav_16k/{refer_name}/*.wav")):
    filename = f.split('/')[-1]
    audioname = filename[len(refer_name)+1:-4]

    # for speaker in ['clb', 'EBVS', 'ERMS', 'MBMPS', 'NJS', 'rms', 'slt', 'bdl']:
    for speaker in ['bdl']:
        # src_wav_emb = f'ppg_emb/{refer_name}/{refer_name}_{audioname}.npy'
        # tar_mel_file = f'mel_emb/{speaker}/{speaker}_{audioname}.npy'
        src_wav = f'data_wav_16k/{refer_name}/{refer_name}_{audioname}.wav'
        tar_wav = f'data_wav_16k/{speaker}/{speaker}_{audioname}.wav'
        speaker_emb = f'speaker_emb/{speaker}/{speaker}_{audioname}.npy'
        accent_emb = f'accent_emb/{speaker}/{speaker}_{audioname}.npy'

        pairs.append([src_wav, tar_wav, speaker_emb, accent_emb])
    
shuffle(pairs)
    
with open(f'{mode}_train_pairs.txt', 'w') as train_file, open(f'{mode}_val_pairs.txt', 'w') as val_file:
    for i, pair in enumerate(pairs):
        if i < len(pairs)-50:
            train_file.write(f"{pair[0]},{pair[1]},{pair[2]},{pair[3]}\n")
        else:
            val_file.write(f"{pair[0]},{pair[1]},{pair[2]},{pair[3]}\n")