'''
# ACM-Research-Coding-Challenge-S21
# Michelle Kuwahara
# This program reads and collects data from a genbank file,
# then uses those data to create and display a circular genome map.
# NOTE: To output the map as a png format, put a path where you
# want the image to show up on code line 125.
'''

# importing libraries
import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO

# read and store genbank file
gb_file = "Genome.gb"
gb_record = SeqIO.read(open(gb_file,"r"), "genbank")

''' collect data from file'''

# index
i = 1
# create dictionary
data = {}
data3 = {}
for counter in range(1,6):
    gb_feature = gb_record.features[i]
    
    # convert to string
    string = str(gb_feature.location)
    stripStr = string.strip("[]()-+")
    listOfStrs = stripStr.split(":")
    # convert to string
    gene = str(gb_feature.qualifiers['gene'])
    
    # a dictionary of original starts, ends of genes' coding sequences
    data3[counter] = {'orStart': int(listOfStrs[0])+1, 'orEnd': int(listOfStrs[1])}
    
    # cross-multiplying to convert the start, end number
    # i.e. (139/2766)*(x/100) where x is to be evaluated
    start = (int(listOfStrs[0])+ 1)*100/2766/100
    end = (int(listOfStrs[1]))*100/2766/100
    
    # store names of genes and their coding sequences
    data[counter] = {'name': gene.strip("['']"), 'start': start, 'end': end}
    
    # loop features in file every odd number
    i = i + 2

''' end collecting data from file'''

# offset between CDS
data2 = {
    1: { 'offset': 0.1},
    2: {'offset': 0.2},
    3: { 'offset': 0.3},
    4: { 'offset': 0.1},
    5: { 'offset': 0.2},
}

# setup the figure:
fig = plt.figure()
ax = plt.subplot(111, projection='polar')
ax.set_theta_direction(-1)  # make it go clockwise
ax.set_theta_zero_location('N')  # put "0" at top

# remove the labels
ax.set_xticks([])
ax.set_yticks([])
ax.spines['polar'].set_visible(False)
LW = 3.0  ## setting the linewidth globally for fine-tuning


def add_bg_circle(ax):
    # the circle
    circle_x = np.linspace(0, 2 * np.pi, 200)
    circle_y = np.array([1.0 for x in circle_x])
    ax.plot(circle_x, circle_y, c="k", linewidth=LW)
    
    # the top notch
    line_y = np.linspace(1.0, 1.1)  ## change length of the top line here
    line_x = np.array([0 for y in line_y])
    ax.plot(line_x, line_y, c="k", linewidth=LW)
    # the text
    ax.text(0.0, 1.15, "0", ha="center", va="center") 
    
    # name and description text
    plt.text(-0.1, 1.5, "NAME: "+ gb_record.name,  ha="center", va="center")
    plt.text(-0.1, 1.4, "DESCRIPTION: "+ gb_record.description,  ha="center", va="center")
    
    # gene V2 text 
    ax.text(0.5, 1.35, "Gene: " + data[1]["name"], ha="left", va="center") 
    ax.text(0.5, 1.25, "CDS: " + str(data3[1]["orStart"]) + "..." + str(data3[1]["orEnd"]), ha="left", va="center")

    # gene v1 text
    ax.text(1.2, 1.60, "Gene: " + data[2]["name"], ha="left", va="center") 
    ax.text(1.2, 1.35, "CDS: " + str(data3[2]["orStart"]) + "..." + str(data3[2]["orEnd"]), ha="left", va="center")

    # gene c3 text
    ax.text(2.5, 1.45, "Gene: " + data[3]["name"], ha="left", va="center") 
    ax.text(2.5, 1.55, "CDS: " + str(data3[3]["orStart"]) + "..." + str(data3[3]["orEnd"]), ha="left", va="center")

    # gene c2 text
    ax.text(3.9, 1.55, "Gene: " + data[4]["name"], ha="left", va="center") 
    ax.text(3.9, 1.70, "CDS: " + str(data3[4]["orStart"]) + "..." + str(data3[4]["orEnd"]), ha="left", va="center")

    # gene c1 text
    ax.text(5.10, 1.80, "Gene: " + data[5]["name"], ha="left", va="center") 
    ax.text(5.05, 1.70, "CDS: " + str(data3[5]["orStart"]) + "..." + str(data3[5]["orEnd"]), ha="left", va="center")

# calling function add_bg_circle
add_bg_circle(ax)

## plot the line segments:
for (k, v), (m,n) in zip(data.items(), data2.items()):
    xs = np.linspace(v['start'] * 2 * np.pi, v['end'] * 2 * np.pi, 200)
    ys = np.array([(1.0 + n['offset']) for x in xs])

    ax.plot(xs, ys, linewidth=LW, label=v['name'])
    
inner_lim = 0.5  # keep this below the value for the main circle at 1.0
outer_lim = 1.3  # adjust to include all plotted segments
ax.set_ylim(inner_lim, outer_lim)

plt.legend() 
#plt.savefig(".png")
plt.show()
