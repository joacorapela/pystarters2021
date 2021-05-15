
import pdb
import sys
import pandas as pd
import matplotlib.pyplot as plt
sys.path.append("../src")
import plotting

def main(argv):
    regions = ("V1", "RSPg")
    conditions = ("Visual", "Vestibular", "VisVes")
    dataFilename = "../../data/All_three_exp_conditions_4.csv"
    figFilename = "../../figures/spikeRateVsabsSpeedV1RSPd_allConditions.png"
    data = pd.read_csv(dataFilename, index_col=0)

    fig, axs = plt.subplots(len(conditions), len(regions))
    fig.tight_layout()

    for iCond in range(len(conditions)):
        for iReg in range(len(regions)):
            plotting.plot_panel(condition=conditions[iCond],
                                region=regions[iReg],
                                data=data, ax=axs[iCond, iReg])

    plt.savefig(figFilename)

    plt.show()

    pdb.set_trace()

if __name__=="__main__":
    main(sys.argv)
