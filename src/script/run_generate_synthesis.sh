python generate_synthesis.py --ppg2mel_model /home/zheng_zhang7/fac-via-ppg/checkpoint/train_0803/checkpoint_8000 \
--waveglow_model /home/zheng_zhang7/fac-via-ppg/interspeech19-stage/ppg2speech-si-am-si-tacotron-bdl2ykwk-final/waveglow_270000 \
--teacher_utterance_path /home/zheng_zhang7/seq2seq_accent_conversion_model/ppg_emb/bdl/bdl_arctic_a0001.npy \
--output_dir /home/zheng_zhang7/fac-via-ppg/bdl_syn_output 
