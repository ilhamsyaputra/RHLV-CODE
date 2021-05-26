import lasio
import matplotlib.pyplot as plt
import time

def tolist(string):
    lizt = list(string.split(', '))
    return lizt

process_start = time.time()
f = open('config.txt')
readfile = f.readlines()

#read config file
filename = readfile[0]
ylimitconfig = tolist(readfile[1])
ylimitconfig[-1] = ylimitconfig[-1].replace('\n', '') #hapus \n
nsubplot = int(readfile[2])     #baca banyak subplot dari file config
curve_1 = tolist(readfile[3])   #jadiin line ke 4 file config jd list
curve_1[-1] = curve_1[-1].replace('\n', '') #hapus \n
curve_2 = tolist(readfile[4])   #jadiin line ke 4 file config jd list
curve_2[-1] = curve_2[-1].replace('\n', '') #hapus \n
curve_3 = tolist(readfile[5])   #jadiin line ke 4 file config jd list
curve_3[-1] = curve_3[-1].replace('\n', '') #hapus \n

crv1_scale = readfile[6].replace('\n', '')
crv2_scale = readfile[7].replace('\n', '')
crv3_scale = readfile[8].replace('\n', '')

f.close()

#start stop config
strt_config = int(ylimitconfig[0])
stop_config = int(ylimitconfig[1])

#read file las
filedir = 'LAS_File/' + filename

try:
    data = lasio.read(filedir)

    # data well
    comp = data.well['COMP']['value']  # company
    well_name = data.well['WELL']['value']  # well
    field_name = data.well['FLD']['value']  # field
    start = data.well['STRT']['value']  # start
    start_unit = data.well['STRT']['unit']  # start-unit
    stop = data.well['STOP']['value']  # stop

    if nsubplot == 1:
        size = [2.7, 9]
    else:
        size = [5, 9]

    fig, ax = plt.subplots(nrows=1, ncols=nsubplot, sharey=True, figsize=size)
    plt.suptitle(well_name, fontsize=20)

    # cycling color
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'olive', 'cyan', 'lime', 'slateblue', 'orangered',
              'darkviolet', 'aqua', 'lawngreen']
    jarak = [40, 70, 100, 130, 160, 190, 220, 250]
    clr, j1, j2, j3 = 0, 0, 0, 0

    if nsubplot == 1:
        if crv1_scale == 'log':
            xscl1 = 'log'
        else:
            xscl1 = 'linear'

        for i in curve_1:
            plt1 = ax.twiny()
            plt1.plot(data.curves[i].data, data.curves['DEPT'].data, color=colors[clr], linewidth=1)
            plt1.invert_yaxis()
            plt1.set_xscale(xscl1)
            plt1.set_xlabel(i + ' (' + data.curves[i].unit + ')', fontsize=8)
            plt1.xaxis.label.set_color(colors[clr])
            plt1.tick_params(axis='x', colors=colors[clr], labelsize=8)
            plt1.spines['top'].set_edgecolor(colors[clr])
            plt1.spines['top'].set_position(('outward', jarak[j1]))
            ax.get_xaxis().set_visible(False)
            clr += 1
            j1 += 1

        ax.set_ylabel(start_unit)
        ax.set_ylim(stop_config, strt_config)

        for ax in [plt1]:
            ax.xaxis.set_ticks_position("top")
            ax.xaxis.set_label_position("top")
            ax.spines["top"].set_position(("axes", 1.02))

        plt.tight_layout()
        plt.savefig('./output/' + well_name + '.png', dpi=300, bbox_inches='tight')

        process_end = time.time()
        process_time = process_end - process_start
        print('Generated. Processing Time: ' + str(process_time))

    elif nsubplot == 2:
        if crv1_scale == 'log':
            xscl1 = 'log'
        else:
            xscl1 = 'linear'

        if crv2_scale == 'log':
            xscl2 = 'log'
        else:
            xscl2 = 'linear'

        for i in curve_1:
            plt1 = ax[0].twiny()
            plt1.plot(data.curves[i].data, data.curves['DEPT'].data, color=colors[clr], linewidth=1)
            plt1.invert_yaxis()
            plt1.set_xscale(xscl1)
            plt1.set_xlabel(i + ' (' + data.curves[i].unit + ')', fontsize=8)
            plt1.xaxis.label.set_color(colors[clr])
            plt1.tick_params(axis='x', colors=colors[clr], labelsize=8)
            plt1.spines['top'].set_edgecolor(colors[clr])
            plt1.spines['top'].set_position(('outward', jarak[j1]))
            ax[0].get_xaxis().set_visible(False)
            clr += 1
            j1 += 1

        for i in curve_2:
            plt2 = ax[1].twiny()
            plt2.plot(data.curves[i].data, data.curves['DEPT'].data, color=colors[clr], linewidth=1)
            plt2.invert_yaxis()
            plt1.set_xscale(xscl2)
            plt2.set_xlabel(i + ' (' + data.curves[i].unit + ')', fontsize=8)
            plt2.xaxis.label.set_color(colors[clr])
            plt2.tick_params(axis='x', colors=colors[clr], labelsize=8)
            plt2.spines['top'].set_edgecolor(colors[clr])
            plt2.spines['top'].set_position(('outward', jarak[j2]))
            ax[1].get_xaxis().set_visible(False)
            clr += 1
            j2 += 1

        ax[0].set_ylabel(start_unit)
        ax[0].set_ylim(stop_config, strt_config)

        for ax in [plt1, plt2]:
            ax.xaxis.set_ticks_position("top")
            ax.xaxis.set_label_position("top")
            ax.spines["top"].set_position(("axes", 1.02))

        plt.tight_layout()
        plt.savefig('./output/' + well_name + '.png', dpi=300, bbox_inches='tight')

        process_end = time.time()
        process_time = process_end - process_start
        print('Generated. Processing Time: ' + str(process_time))

    elif nsubplot == 3:
        if crv1_scale == 'log':
            xscl1 = 'log'
        else:
            xscl1 = 'linear'

        if crv2_scale == 'log':
            xscl2 = 'log'
        else:
            xscl2 = 'linear'

        if crv3_scale == 'log':
            xscl3 = 'log'
        else:
            xscl3 = 'linear'

        for i in curve_1:
            plt1 = ax[0].twiny()
            plt1.plot(data.curves[i].data, data.curves['DEPT'].data, color=colors[clr], linewidth=1)
            plt1.invert_yaxis()
            plt1.set_xscale(xscl1)
            plt1.set_xlabel(i + ' (' + data.curves[i].unit + ')', fontsize=8)
            plt1.xaxis.label.set_color(colors[clr])
            plt1.tick_params(axis='x', colors=colors[clr], labelsize=8)
            plt1.spines['top'].set_edgecolor(colors[clr])
            plt1.spines['top'].set_position(('outward', jarak[j1]))
            ax[0].get_xaxis().set_visible(False)
            clr += 1
            j1 += 1

        for i in curve_2:
            plt2 = ax[1].twiny()
            plt2.plot(data.curves[i].data, data.curves['DEPT'].data, color=colors[clr], linewidth=1)
            plt2.invert_yaxis()
            plt2.set_xscale(xscl2)
            plt2.set_xlabel(i + ' (' + data.curves[i].unit + ')', fontsize=8)
            plt2.xaxis.label.set_color(colors[clr])
            plt2.tick_params(axis='x', colors=colors[clr], labelsize=8)
            plt2.spines['top'].set_edgecolor(colors[clr])
            plt2.spines['top'].set_position(('outward', jarak[j2]))
            ax[1].get_xaxis().set_visible(False)
            clr += 1
            j2 += 1

        for i in curve_3:
            plt3 = ax[2].twiny()
            plt3.plot(data.curves[i].data, data.curves['DEPT'].data, color=colors[clr], linewidth=1)
            plt3.invert_yaxis()
            plt3.set_xscale(xscl3)
            plt3.set_xlabel(i + ' (' + data.curves[i].unit + ')', fontsize=8)
            plt3.xaxis.label.set_color(colors[clr])
            plt3.tick_params(axis='x', colors=colors[clr], labelsize=8)
            plt3.spines['top'].set_edgecolor(colors[clr])
            plt3.spines['top'].set_position(('outward', jarak[j3]))
            ax[2].get_xaxis().set_visible(False)
            clr += 1
            j3 += 1

        ax[0].set_ylabel(start_unit)
        ax[0].set_ylim(stop_config, strt_config)

        for ax in [plt1, plt2, plt3]:
            ax.xaxis.set_ticks_position("top")
            ax.xaxis.set_label_position("top")
            ax.spines["top"].set_position(("axes", 1.02))

        plt.tight_layout()
        plt.savefig('./output/' + well_name + '.png', dpi=300, bbox_inches='tight')

        process_end = time.time()
        process_time = process_end - process_start
        print('Generated. Processing Time: ' + str(process_time))
    else:
        print('The Number of Subplot is exceeded the limit, limit: 3')

except:
    print('Something wrong with the LAS file, cannot proceed.')
