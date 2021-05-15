
import sys
import pandas as pd
import matplotlib.pyplot as plt
sys.path.append("../src")
import plotting

def main(argv):
    dataFilename = "../../data/All_three_exp_conditions_4.csv"
    figFilename = "../../figures/spikeRateVsabsSpeedV1_allConditions.png"
    data = pd.read_csv(dataFilename, index_col=0)

    fig, axs = plt.subplots(3, 1)

    plotting.plot_panel(condition="Visual", data=data, ax=axs[0])
    plotting.plot_panel(condition="Vestibular", data=data, ax=axs[1])
    plotting.plot_panel(condition="VisVes", data=data, ax=axs[2],
                        title="Visual + Vestibular")

    plt.savefig(figFilename)

    plt.show()

if __name__=="__main__":
    main(sys.argv)
