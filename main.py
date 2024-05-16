import matplotlib.pyplot as plt
import numpy as np

def plot_motor_characteristics(Voltage, I0, Is, N0, Ts):
    # np.linspace でトルクの範囲を設定（Nm）
    torque = np.linspace(0, Ts, Ts)

    current = I0 + (Is - I0) * (torque / max(torque))
    speed = N0 - (N0 / Ts) * torque

    # 出力(W)の計算
    # P [W] = N [r/min] × 2π/60  × T [gcm] × 9.80665e-5
    output = (speed * 2 * np.pi / 60) * torque * 9.80665e-5

    # 効率（Efficiency）の計算
    efficiency = (output / (Voltage * current)) * 100

    # グラフを描画
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.plot(torque, current, label=f'I0 = {I0}, Is = {Is}', color='b', linestyle='-')
    ax1.set_xlabel('Torque (gcm)')
    ax1.set_ylabel('Current (A)', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.set_xlim(0, max(torque))

    ax2 = ax1.twinx()
    ax2.plot(torque, speed, label=f'N0 = {N0}, Ts = {Ts}', color='r', linestyle='--')
    ax2.set_ylabel('Speed (r/min)', color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    ax3 = ax1.twinx()
    ax3.plot(torque, efficiency, label='Efficiency', color='g', linestyle='-.')
    ax3.spines['right'].set_position(('outward', 70))
    ax3.set_ylabel('Efficiency (%)', color='g')
    ax3.tick_params(axis='y', labelcolor='g')

    ax4 = ax1.twinx()
    ax4.plot(torque, output, label='Power (W)', color='purple', linestyle=':')
    ax4.spines['right'].set_position(('outward', 120))
    ax4.set_ylabel('Power (W)', color='purple')
    ax4.tick_params(axis='y', labelcolor='purple')

    # グリッドを表示
    ax1.grid(True)

    # figureの大きさを指定
    fig = plt.gcf()
    fig.set_size_inches(10, 6)

    fig.tight_layout()
    plt.show()

Voltage = 3.7  # 電圧値
I0 = 1.0  # 無負荷時電流
Is = 28  # ストール電流
N0 = 16000  # 無負荷時回転数
Ts = 250  # ストールトルク

plot_motor_characteristics(Voltage, I0, Is, N0, Ts)