import seaborn as sn
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def draw(n):
    normalize = True
    save_dir = ''
    names = ['People', 'Road', '自行车', '公交车', 'влак', 'Straße', 'дарога'] * 20
    names = names[:n]
    matplotlib.rc("font", family='Microsoft YaHei')

    nc, nn = n, n  # number of classes, names
    matrix = np.random.random((nc, nc))
    array = matrix / ((matrix.sum(0).reshape(1, -1) + 1E-9) if normalize else 1)  # normalize columns
    array[array < 0.005] = np.nan  # don't annotate (would appear as 0.00)

    fig, ax = plt.subplots(1, 1, figsize=(12, 9), tight_layout=True)
    sn.set(font_scale=1.0 if nc < 50 else 0.8)  # for label size
    labels = (0 < nn < 90) and (nn == nc)  # apply names to ticklabels
    sn.heatmap(array,
               ax=ax,
               annot=nc < 30,
               annot_kws={'size': 8},
               cmap='Blues',
               fmt='.2f',
               square=True,
               vmin=0.0,
               xticklabels=names if labels else 'auto',
               yticklabels=names if labels else 'auto').set_facecolor((1, 1, 1))
    if labels:
        ticks_size = 14
        if nn >= 40:
            ticks_size *= 38 / nn
        plt.xticks(fontsize=ticks_size)
        plt.yticks(fontsize=ticks_size)
    label_size = 20 if nc < 50 else 16
    ax.set_xlabel('True').set_size(label_size)
    ax.set_ylabel('Predicted').set_size(label_size)
    ax.set_title('Confusion Matrix').set_size(22)
    ax.set()
    path = Path(save_dir) / ('cm_classes_%d.png'%(n,))
    fig.savefig(path, dpi=250)
    plt.close(fig)
    print('Save:', path)

draw(5)
draw(10)
draw(30)
draw(50)
draw(70)
draw(90)
draw(100)
draw(120)
