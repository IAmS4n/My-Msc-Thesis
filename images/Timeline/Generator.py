"""
for use tex file, remove document scope and add latin and cite color
replace XYZ -- > \textcolor{white}
\hypersetup{citecolor=white}
\begin{latin}

\end{latin}
\hypersetup{citecolor=magenta

"""

from datetime import date

from labella.timeline import TimelineSVG, TimelineTex
from labella.utils import COLOR_10

def main():
    items = [
            {'time': date(2014, 6,10), 'text': 'GAN \cite{Goodfellow2014}'},
            {'time': date(2017, 3,31), 'text': 'WGAN-GP \cite{Gulrajaniy17ImprovedWasserstein}'},
            {'time': date(2017,6 ,5), 'text': 'Vocab Distribution Generation \cite{press2017langwasserstein}'},

#            {'time': date(1989, 6,15),  'text': 'Teacher Forcing'},
            {'time': date(2015, 6,9), 'text': 'Scheduled Sampling \cite{bengio2015scheduled}'},
            {'time': date(2015, 11,19), 'text': 'VAE-LSTM-LSTM \cite{Bowman2016VAE}'},
            {'time': date(2017, 2,27), 'text': 'VAE-LSTM-CNN \cite{Yang2017ImprovedVAE}'},

            {'time': date(2016, 11,12), 'text': 'GSGAN \cite{kusner2016gans}'},

            {'time': date(2016, 10,27), 'text': 'Professor Forcing \cite{lamb2016professor}'},
            {'time': date(2017, 6,12), 'text': 'TextGAN \cite{Zhang2017TextGAN}'},

            {'time': date(2016,9 ,18), 'text': 'SeqGAN \cite{SeqGAN}'},
            {'time': date(2017,5 ,30), 'text': 'ORGAN \cite{ORGAN}'},
            {'time': date(2017, 5,31), 'text': 'RankGAN \cite{lin2017adversarial}'},
            {'time': date(2017,9 ,24), 'text': 'LeakGAN \cite{Guo2018}'},
            {'time': date(2017,2 ,26), 'text': 'MaliGAN \cite{Che2017}'}
            ]

    options = {
        'initialWidth': 200,
        'initialHeight': 300,
        'direction': 'right',
        'dotColor': COLOR_10,
        'labelBgColor': COLOR_10,
        'linkColor': COLOR_10,
        'layerGap': 40,
        'textFn': lambda x :"XYZ{%s}" % x["text"] ,
        'labelPadding': {'left': 2, 'right': 2, 'top': 4, 'bottom': 4},
        'labella': {
            'maxPos': 300,
            'algorithm': 'simple'
            }
        }

    tl = TimelineSVG(items, options=options)
    tl.export('timeline_kit_3.svg')

    tl = TimelineTex(items, options=options)
    tl.export('timeline_kit_3.tex')

if __name__ == '__main__':
    main()