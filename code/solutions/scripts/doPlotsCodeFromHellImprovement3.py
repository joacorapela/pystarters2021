
import pdb
import sys
import pandas as pd
import matplotlib.pyplot as plt
sys.path.append("../src")
import plotting

def main(argv):
    conditions = ("Visual", "Vestibular", "VisVes")
    titles = ("Visual", "Vestibular", "Visual + Vestibular")
    dataFilename = "../../data/All_three_exp_conditions_4.csv"
    figFilename = "../../figures/spikeRateVsabsSpeedV1_allConditions.png"
    data = pd.read_csv(dataFilename, index_col=0)

    fig, axs = plt.subplots(len(conditions), 1)

    for i in range(len(conditions)):
        plotting.plot_panel(condition=conditions[i], data=data, ax=axs[i],
                            title=titles[i])

    plt.savefig(figFilename)

    plt.show()

    pdb.set_trace()

if __name__=="__main__":
    main(sys.argv)
