#!/usr/bin/python3
# -*- coding: utf-8 -*-
# python start.py

from datetime import datetime
import pprint
import random
#import GameStatus #Subprocess failed

#20230314追加　♪コロブチカ♪
import numpy as np
#import matplotlib.pyplot as pl
import wave
import struct
import pyaudio

                      #1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54	55	56	57	58	59	60	61	62	63	64	65	66	67	68	69	70	71	72	73	74	75	76	77	78	79	80	81	82	83	84	85	86	87	88	89	90	91	92	93	94	95	96	97	98	99	100	101	102	103	104	105	106	107	108	109	110	111	112	113	114	115	116	117	118	119	120	121	122	123	124	125	126	127	128	129	130	131	132	133	134	135	136	137	138	139	140	141	142	143	144	145	146	147	148	149	150	151	152	153	154	155	156	157	158	159	160	161	162	163	164	165	166	167	168	169	170	171	172	173	174	175	176	177	178	179	180	181	182
tetris_direction = [0,1,	3,	1,	3,	0,	0,	1,	1,	3,	3,	0,	0,	0,	0,	0,	1,	3,	3,	0,	1,	1,	0,	2,	2,	2,	0,	1,	1,	0,	1,	2,	0,	0,	1,	0,	0,	2,	1,	1,	0,	1,	0,	0,	3,	0,	3,	0,	0,	1,	0,	1,	0,	0,	0,	1,	0,	0,	3,	3,	2,	0,	1,	1,	0,	0,	3,	1,	0,	0,	0,	0,	2,	1,	0,	0,	1,	1,	0,	2,	2,	1,	0,	1,	1,	0,	3,	2,	0,	0,	1,	1,	0,	2,	0,	0,	0,	1,	1,	0,	1,	0,	2,	0,	1,	0,	0,	2,	3,	0,	0,	0,	1,	0,	0,	2,	3,	0,	1,	1,	0,	0,	0,	2,	0,	1,	1,	0,	3,	0,	2,	0,	0,	0,	0,	1,	3,	1,	0,	0,	0,	0,	3,	3,	2,	0,	1,	0,	0,	0,	2,	2,	0,	1,	0,	0,	2,	0,	1,	0,	0,	1,	0,	1,	3,	0,	0,	1,	1,	0,	3,	3,	0,	0,	1,	1,	0,	2,	1,	0,	0,	1,	0]
tetris_x =         [0,2,	5,	1,	4,	7,	3,	1,	7,	7,	4,	0,	6,	5,	1,	9,	5,	1,	5,	0,	7,	4,	3,	2,	3,	8,	6,	7,	0,	9,	3,	6,	0,	2,	4,	5,	9,	8,	7,	1,	0,	2,	4,	9,	1,	8,	6,	3,	1,	7,	5,	1,	4,	6,	0,	2,	7,	9,	1,	4,	8,	3,	5,	7,	9,	0,	5,	7,	1,	5,	7,	3,	4,	1,	5,	1,	7,	0,	9,	2,	0,	6,	3,	2,	1,	8,	6,	0,	4,	0,	5,	3,	9,	2,	8,	3,	6,	3,	5,	9,	1,	8,	4,	0,	6,	7,	5,	2,	7,	3,	7,	2,	5,	9,	4,	0,	6,	0,	7,	5,	9,	2,	4,	3,	0,	7,	5,	9,	1,	5,	8,	0,	7,	3,	9,	7,	3,	5,	0,	3,	7,	9,	1,	7,	5,	0,	2,	6,	8,	0,	4,	7,	5,	2,	3,	9,	1,	8,	4,	6,	2,	0,	9,	6,	3,	0,	2,	7,	1,	0,	5,	7,	1,	4,	1,	3,	9,	9,	6,	3,	8,	3,	6]

#20230314追加　♪コロブチカ♪

onkai_list =    [-127,5,	0,	1,	3,	1,	0,	-2,	-2,	1,	5,	3,	1,	 0,	 0,	1,	3,	5,	1,	-2,	-2,	-127,	 3,	6,	10,	8,	6,	5,	5,	1,	5,	3,	1,	 0,	 0,	1,	3,	5,	1,	-2,	-2,	-127,	 3,	6,	10,	8,	6,	5,	5,	1,	5,	3,	1,	 0,	 0,	1,	3,	5,	1,	-2,	-2,	5,	0,	1,	3,	1,	0,	-2,	-2,	1,	5,	3,	1,	 0,	 0,	1,	3,	5,	1,	-2,	-2,	-127,	 3,	6,	10,	8,	6,	5,	5,	1,	5,	3,	1,	 0,	 0,	1,	3,	5,	1,	-2,	-2,	-127,	 3,	6,	10,	8,	6,	5,	5,	1,	5,	3,	1,	 0,	 0,	1,	3,	5,	1,	-2,	-2,	5,	0,	1,	3,	1,	0,	-2,	-2,	1,	5,	3,	1,	 0,	 0,	1,	3,	5,	1,	-2,	-2,	-127,	 3,	6,	10,	8,	6,	5,	5,	1,	5,	3,	1,	 0,	 0,	1,	3,	5,	1,	-2,	-2,	-127,	 3,	6,	10,	8,	6,	5,	5,	1,	5,	3,	1,	 0,	 0,	1,	3,	5,	1,	-2,	-2]
duration_list = [0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.2,0.4,0.2,0.2,0.4,0.4,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.2,0.4,0.2,0.2,0.4,0.4,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.4,0.4,0.4,0.4,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.2,0.4,0.2,0.2,0.4,0.4,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.2,0.4,0.2,0.2,0.4,0.4,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.4,0.4,0.4,0.4,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.2,0.4,0.2,0.2,0.4,0.4,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.2,0.4,0.2,0.2,0.4,0.4,0.2,0.4,0.2,0.2,0.4,0.2,0.2,0.4,0.4,0.4,0.4,0.4]






class Block_Controller(object):

    # init parameter
    board_backboard = 0
    board_data_width = 0
    board_data_height = 0
    ShapeNone_index = 0
    CurrentShape_class = 0
    NextShape_class = 0
    sample_hz = 48000


    # GetNextMove is main function.
    # input
    #    GameStatus : this data include all field status, 
    #                 in detail see the internal GameStatus data.
    # output
    #    nextMove : this data include next shape position and the other,
    #               if return None, do nothing to nextMove.
    def GetNextMove(self, nextMove, GameStatus):

        t1 = datetime.now()

        # print GameStatus
        print("=================================================>")
        #pprint.pprint(GameStatus, width = 61, compact = True)

        #currentShape_index = GameStatus["block_info"]["currentShape"]["index"]
        current_block_index = GameStatus["judge_info"]["block_index"]
        print(current_block_index)

        # search best nextMove -->
        # random sample
        #nextMove["strategy"]["direction"] = random.randint(0,4)
        #nextMove["strategy"]["x"] = random.randint(0,9)
        nextMove["strategy"]["direction"] = tetris_direction[current_block_index]
        nextMove["strategy"]["x"] = tetris_x[current_block_index]
        nextMove["strategy"]["y_operation"] = 1
        nextMove["strategy"]["y_moveblocknum"] = random.randint(1,8)
        # search best nextMove <--

        sample_hz = 48000
        note_hz = 440.0 * 2.0**(onkai_list[current_block_index]/12.0)
        print(note_hz)
        t = np.linspace(0., duration_list[current_block_index], int(sample_hz*duration_list[current_block_index]))#1秒分の時間の配列を確保
        # t = np.linspace(0., duration, int(sample_hz*duration))#1秒分の時間の配列を確保
        wv = np.sin(2.0*np.pi*note_hz*t) # waveを作成

        #Chapter2　.wavに出力する

        #Chapter2-1 バイナリ化する

        max_num = 32767.0 / max(wv) #バイナリ化の下準備の下準備
        wv16 = [int(x * max_num) for x in wv] #バイナリ化の下準備
        bi_wv = struct.pack("h" * len(wv16), *wv16) #バイナリ化

        #Chapter2-2　.waveモジュールで.wavファイルを出力

        file = wave.open('sin_wave.wav', mode='wb') #sin_wave.wavを書き込みモードで開く。（ファイルが存在しなければ新しく作成する。）
        param = (1,2,sample_hz,len(bi_wv),'NONE','not compressed') #パラメータ
        file.setparams(param) #パラメータの設定
        file.writeframes(bi_wv) #データの書き込み
        file.close #ファイルを閉じる

        #Chapter3
        file = wave.open('sin_wave.wav', mode='rb')

        p = pyaudio.PyAudio()
        stream = p.open(
            format = p.get_format_from_width(file.getsampwidth()),
            channels = file.getnchannels(),
            rate = file.getframerate(),
            output = True
            )
        chunk = 1024
        file.rewind()
        data = file.readframes(chunk)
        while data:
            stream.write(data)
            data = file.readframes(chunk)
        stream.close()
        p.terminate()






        # return nextMove
        print(nextMove["strategy"]["direction"])
        print("===", datetime.now() - t1)
        print(nextMove)
        return nextMove
    



BLOCK_CONTROLLER = Block_Controller()

