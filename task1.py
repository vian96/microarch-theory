import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple
from numpy.typing import NDArray


def calculate_metrics(
    f_range: NDArray[np.float64], ipc: float, c_dyn: float
) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
    # calculate voltage based on frequency: u = f + 0.2, bounded by u_min = 1
    voltage = np.maximum(1.0, f_range + 0.2)

    # performance is ipc * frequency
    performance = ipc * f_range

    # power is c * u^2 * f
    power = c_dyn * (voltage**2) * f_range

    return performance, power


def plot_processor_characteristics():
    # define frequency range up to the specified limit
    f_max = 1.8
    f_points = np.linspace(0.8, f_max, 500)

    # core parameters (relative units)
    # efficient core: ipc=1, cdyn=1
    # performance core: ipc=2, cdyn=4
    perf_e, power_e = calculate_metrics(f_points, ipc=1.0, c_dyn=1.0)
    perf_p, power_p = calculate_metrics(f_points, ipc=2.0, c_dyn=4.0)

    # find the optimal curve
    # we interpolate to a common performance grid to compare power
    common_perf = np.linspace(0.01, max(perf_e.max(), perf_p.max()), 1000)

    # interp power for both cores at common performance points
    # use a high fill value for performance points core cannot reach
    p_at_common_e = np.interp(common_perf, perf_e, power_e, right=np.inf)
    p_at_common_p = np.interp(common_perf, perf_p, power_p, right=np.inf)

    # optimal is the minimum power for a given performance target
    optimal_power = np.minimum(p_at_common_e, p_at_common_p)

    # plotting
    plt.figure(figsize=(10, 6), dpi=120)

    # plot individual cores
    plt.plot(
        perf_e, power_e, label="Efficient Core (E-core)", color="#2ca02c", linewidth=2
    )
    plt.plot(
        perf_p, power_p, label="Performance Core (P-core)", color="#d62728", linewidth=2
    )

    # plot optimal execution curve
    plt.plot(
        common_perf,
        optimal_power,
        "--",
        label="Optimal (Heterogeneous)",
        color="black",
        alpha=0.8,
        linewidth=2.5,
    )

    # identify the crossover point for visualization
    # the e-core is better at low perf because it hits u_min floor later
    # the p-core is better when frequency scaling dominates because it needs lower f
    plt.title("Heterogeneous Processor: Power vs Performance", fontsize=12)
    plt.xlabel("Performance (Relative units)", fontsize=11)
    plt.ylabel("Power (Relative units)", fontsize=11)

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.xlim(0, 3.7)
    plt.ylim(0, 35)

    plt.tight_layout()
    plt.show()
    plt.savefig("task1.png")


if __name__ == "__main__":
    plot_processor_characteristics()
