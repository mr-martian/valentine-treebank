#!/usr/bin/env python3

import random

sources = ['ai-weirdness', 'hallmark', 'vampire']

def load_sents(name):
    with open('%s-edited.conllu' % name) as fin:
        sents = []
        cur = []
        for line_ in fin:
            line = line_.strip()
            if not line:
                if cur:
                    sents.append('\n'.join(cur))
                    cur = []
            elif line[0] == '#':
                mode = line.split()[1]
                if mode == 'text':
                    cur.append(line)
                elif mode == 'sent_id':
                    cur.append(line.replace('= ', '= '+name+'-'))
            else:
                cur.append(line)
        if cur:
            sents.append('\n'.join(cur))
        return sents

def write_sents(fname, sents):
    with open(fname, 'w') as fout:
        fout.write('\n\n'.join(sents) + '\n\n')

sents = []
for name in sources:
    sents += load_sents(name)
random.shuffle(sents)
tenth = int(len(sents) / 10)
write_sents('valentine.test.conllu', sents[:tenth])
write_sents('valentine.dev.conllu', sents[tenth:2*tenth])
write_sents('valentine.train.conllu', sents[2*tenth:])
