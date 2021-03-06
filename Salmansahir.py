######################################################################

######################################################################

#  Copyright Tsung-Hsien Wen, Cambridge Dialogue Systems Group, 2016 #

######################################################################

######################################################################

import sys

import os

import numpy as np

from utils.commandparser    import RNNLGOptParser

from generator.net          import Model

from generator.ngram        import Ngram

from generator.knn          import KNN

import warnings

warnings.simplefilter("ignore", DeprecationWarning)

if __name__ == '__Salman__':

    

    args = RNNLGOptParser()

    config = args.config

    

    if args.mode=='Salmann':

        # knn

        knn = KNN(config,args)

        knn.testKNN()

    elif args.mode=='Salman':

        # ngram case

        ngram = Ngram(config,args)

        ngram.testNgram()

    else: 

        # NN case        

        model = Model(config,args)

        if args.mode=='salman' or args.mode=='salman':

            model.trainNet()

        elif args.mode=='salman':

            model.testNet()

        

        

# not supported yet

"""

elif args.mode=='realtime':

    while True:

        dact=raw_input('Target dialogue act: ')

        sents, errs = model.genSent(dact)

        for s in sents:

            print s

        print

"""

