
import sys
import pandas as pd
import matplotlib.pyplot as plt
sys.path.append("../src")
import plotting

def main(argv):
    dataFilename = "../../data/All_three_exp_conditions_4.csv"
    figFilename = "../../figures/spikeRateVsabsSpeedV1RSPg_allConditions_neat.png"
    data = pd.read_csv(dataFilename, index_col=0)

    fig, axs = plt.subplots(3, 2)

    plotting.plot_panel(condition="Visual", region="V1", data=data,
                        ax=axs[0, 0])
    plotting.plot_panel(condition="Vestibular", region="V1", data=data,
                        ax=axs[1, 0])
    plotting.plot_panel(condition="VisVes", region="V1", data=data,
                        ax=axs[2, 0], title="V1: Visual + Vestibular")

    plotting.plot_panel(condition="Visual", region="RSPg", data=data,
                        ax=axs[0, 1])
    plotting.plot_panel(condition="Vestibular", region="RSPg", data=data,
                        ax=axs[1, 1])
    plotting.plot_panel(condition="VisVes", region="RSPg", data=data,
                        ax=axs[2, 1], title="V1: Visual + Vestibular")

    plt.tight_layout()

    plt.savefig(figFilename)

    plt.show()

if __name__=="__main__":
    main(sys.argv)
