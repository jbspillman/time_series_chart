import json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, MultipleLocator, FormatStrFormatter, AutoMinorLocator, ScalarFormatter
from mplcursors import cursor

the_json = "series.json"
df = pd.read_json(the_json)
totals = df["Total"].tolist()
hours = df["Hour"].tolist()
reads = df["Read"].tolist()
writes = df["Write"].tolist()

fig, ax = plt.subplots(tight_layout=True)
fig.set_size_inches(14, 5)
ax.set_xlim(0, 24)
ax.set_ylim(0, 2000000)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter(FormatStrFormatter('%02d'))
ax.yaxis.set_major_locator(MultipleLocator(100000))
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

ax.set_title("NAOHIO0102\nCluster Daily IOPs")
ax.set_ylabel('IOPs')
ax.set_xlabel('Hour (UTC)')

ax.plot(hours, totals, label="Totals", linestyle="solid", color="red")
ax.plot(hours, reads, label="Reads", linestyle="dashdot", color="yellow")
ax.plot(hours, writes, label="Writes", linestyle="dotted", color="green")
plt.legend()
plt.grid(axis='x', color='gray', linestyle='dotted', linewidth=0.2)
plt.grid(axis='y', color='gray', linestyle='dashed', linewidth=0.2)
cursor(hover=True)

fig.savefig('poo.png')
# plt.show()
plt.close(fig)
plt.close()


