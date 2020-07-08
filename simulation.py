import matplotlib.pyplot as plt
import numpy as np

import reeds_shepp as rs
import draw


def main():
    # choose states pairs: (x, y, yaw)
    states = [(0, 0, 0), (10, 10, -90), (20, 5, 60), (30, 10, 120),
              (35, -5, 30), (25, -10, -120), (15, -15, 100), (0, -10, -90)]

    max_c = 0.1                         # max curvature
    path_x, path_y, yaw = [], [], []

    for i in range(len(states) - 1):
        s_x = states[i][0]
        s_y = states[i][1]
        s_yaw = np.deg2rad(states[i][2])
        g_x = states[i + 1][0]
        g_y = states[i + 1][1]
        g_yaw = np.deg2rad(states[i + 1][2])

        path_i = rs.calc_optimal_path(s_x, s_y, s_yaw,
                                      g_x, g_y, g_yaw, max_c)

        path_x += path_i.x
        path_y += path_i.y
        yaw += path_i.yaw

    # animation
    plt.ion()
    plt.figure(1)

    for i in range(len(path_x)):
        plt.clf()
        plt.plot(path_x, path_y, linewidth=1, color='gray')

        for x, y, theta in states:
            draw.Arrow(x, y, np.deg2rad(theta), 2, 'blueviolet')

        draw.Car(path_x[i], path_y[i], yaw[i], 1.5, 3)

        plt.axis("equal")
        plt.title("Simulation of Reeds-Shepp Curves")
        plt.draw()
        plt.pause(0.001)

    plt.pause(1)


if __name__ == '__main__':
    main()
