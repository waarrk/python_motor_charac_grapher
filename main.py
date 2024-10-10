import matplotlib.pyplot as plt
import numpy as np


def plot_motor_characteristics(Voltage, I0, Is, N0, Ts, motor_name):
    # np.linspace でトルクの範囲を設定（gcm）
    torque_gcm = np.linspace(0, Ts, Ts)
    # gcm to mNm conversion considering gravitational acceleration (9.8 m/s^2)
    torque_mNm = torque_gcm * 9.8e-2  # gcm to mNm conversion

    current = I0 + (Is - I0) * (torque_gcm / max(torque_gcm))
    speed = N0 - (N0 / Ts) * torque_gcm

    # 出力(W)の計算
    # Convert mNm to Nm for power calculation
    output = (speed * 2 * np.pi / 60) * (torque_mNm * 1e-3)
    # 最大出力をprint
    max_output = max(output)
    print(f'最大出力: {max_output} W')

    # 効率（Efficiency）の計算
    efficiency = (output / (Voltage * current)) * 100

    # 最大効率をprint
    max_efficiency = max(efficiency)
    max_eff_idx = np.argmax(efficiency)
    max_eff_torque = torque_gcm[max_eff_idx]
    max_eff_current = current[max_eff_idx]
    max_eff_speed = speed[max_eff_idx]
    max_eff_output = output[max_eff_idx]
    max_eff = efficiency[max_eff_idx]

    print(f'最大効率: {max_efficiency} %')
    print(f'最大効率時の出力: {max_eff_output} W')
    print(f'最大効率時の回転数: {max_eff_speed} r/min')
    print(f'最大効率時のトルク: {max_eff_torque} gcm')
    print(f'最大効率時の電流: {max_eff_current} A')

    # 最大出力時のインデックスを取得
    max_output_idx = np.argmax(output)
    max_output_torque = torque_gcm[max_output_idx]
    max_output_efficiency = efficiency[max_output_idx]

    # グラフを描画
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.plot(torque_gcm, current,
             label=f'I0 = {I0}, Is = {Is}', color='b', linestyle='-')
    ax1.set_xlabel('Torque (gcm)')
    ax1.set_ylabel('Current (A)', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.set_xlim(0, max(torque_gcm))

    ax2 = ax1.twinx()
    ax2.plot(torque_gcm, speed,
             label=f'N0 = {N0}, Ts = {Ts}', color='r', linestyle='--')
    ax2.set_ylabel('Speed (r/min)', color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    ax3 = ax1.twinx()
    ax3.plot(torque_gcm, efficiency, label='Efficiency',
             color='g', linestyle='-.')
    ax3.spines['right'].set_position(('outward', 70))
    ax3.set_ylabel('Efficiency (%)', color='g')
    ax3.tick_params(axis='y', labelcolor='g')

    ax4 = ax1.twinx()
    ax4.plot(torque_gcm, output, label='Power (W)',
             color='purple', linestyle=':')
    ax4.spines['right'].set_position(('outward', 120))
    ax4.set_ylabel('Power (W)', color='purple')
    ax4.tick_params(axis='y', labelcolor='purple')

    # Create a second x-axis below the first one for mNm
    ax5 = ax1.secondary_xaxis('bottom', functions=(
        lambda x: x * 9.8e-2, lambda x: x / 9.8e-2))
    ax5.set_xlabel('Torque (mNm)')
    ax5.spines['bottom'].set_position(('outward', 50))

    # 最大効率時の各値をプロット
    ax1.plot(max_eff_torque, max_eff_current, 'bo')
    ax1.annotate(f'{max_eff_current:.2f} A', (max_eff_torque, max_eff_current),
                 textcoords="offset points", xytext=(0, -15), ha='center')

    ax2.plot(max_eff_torque, max_eff_speed, 'ro')
    ax2.annotate(f'{max_eff_speed:.2f} r/min', (max_eff_torque, max_eff_speed),
                 textcoords="offset points", xytext=(0, -15), ha='center')

    ax3.plot(max_eff_torque, max_eff, 'go')
    ax3.annotate(f'{max_eff:.2f} %', (max_eff_torque, max_eff),
                 textcoords="offset points", xytext=(0, -15), ha='center')

    ax4.plot(max_eff_torque, max_eff_output, 'mo')
    ax4.annotate(f'{max_eff_output:.2f} W', (max_eff_torque, max_eff_output),
                 textcoords="offset points", xytext=(0, -15), ha='center')

    # 最大出力時の各値をプロット
    ax4.plot(max_output_torque, max_output, 'mo')
    ax4.annotate(f'{max_output:.2f} W', (max_output_torque, max_output),
                 textcoords="offset points", xytext=(0, -15), ha='center')

    ax3.plot(max_output_torque, max_output_efficiency, 'go')
    ax3.annotate(f'{max_output_efficiency:.2f} %', (max_output_torque,
                 max_output_efficiency), textcoords="offset points", xytext=(0, -15), ha='center')

    # グリッドを表示
    ax1.grid(True)

    # figureの大きさを指定
    fig = plt.gcf()
    fig.set_size_inches(10, 6)

    # グラフの外にパラメータを表示
    fig.text(0.95, 0.03, f'Motor: {motor_name}\nVoltage: {Voltage} V\nI0: {I0} A\nN0: {N0} r/min\nIs: {Is} A\nTs: {Ts} gcm',
             ha='right', va='bottom', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

    fig.tight_layout()
    plt.show()


Voltage = 18  # 電圧値
I0 = 1.5  # 無負荷時電流
Is = 112  # ストール電流
N0 = 18000   # 無負荷時回転数
Ts = 12094  # ストールトルク
motor_name = "WRS-775-200"  # モーター名

plot_motor_characteristics(Voltage, I0, Is, N0, Ts, motor_name)
