import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from scipy.ndimage import gaussian_filter1d

# Load VDOS data
# spp_1c40 = np.loadtxt('vdos_300K_1c40.dat', skiprows=1)
# spp_2c40 = np.loadtxt('vdos_300K_2c40.dat', skiprows=1)
# spp_2d40 = np.loadtxt('vdos_300K_2d40.dat', skiprows=1)
# spp_3d40 = np.loadtxt('vdos_300K_3d40.dat', skiprows=1)

# spp_1c80 = np.loadtxt('vdos_300K_1c80.dat', skiprows=1)
# spp_2c80 = np.loadtxt('vdos_300K_2c80.dat', skiprows=1)
# spp_2d80 = np.loadtxt('vdos_300K_2d80.dat', skiprows=1)
# spp_3d80 = np.loadtxt('vdos_300K_3d80.dat', skiprows=1)

#spp_1c120 = np.loadtxt('vdos_300K_1c120.dat', skiprows=1)
#spp_2c120 = np.loadtxt('vdos_300K_2c120.dat', skiprows=1)
#spp_2d120 = np.loadtxt('vdos_300K_2d120.dat', skiprows=1)
#spp_3d120 = np.loadtxt('vdos_300K_3d120.dat', skiprows=1)

# Extract frequency and VDOS

def get_vdos(filename):
    spp_sc_data = np.loadtxt(filename, skiprows=1)
    freq_sc = spp_sc_data[:, 0]
    spp_sc = spp_sc_data[:, 1]
    spp_sc[spp_sc < 0] = 0
    spp_sc /= np.trapz(spp_sc, freq_sc)
    mask_sc = freq_sc <= 20
    freq_sc = freq_sc[mask_sc]
    spp_sc = spp_sc[mask_sc]
    spp_sc_smooth = savgol_filter(spp_sc, window_length=1501, polyorder=5)
    return freq_sc, spp_sc_smooth

# Plot
plt.rcParams.update({
    'font.family': 'Nimbus Roman',
        'font.size': 20,
    'axes.labelsize': 20,
    'axes.titlesize': 20,
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'legend.fontsize': 16,

    # ---- Tick styling ----
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.size': 10,
    'ytick.major.size': 10,
    'xtick.major.width': 2.8,
    'ytick.major.width': 2.8,

    # ticks on all sides
    'xtick.top': True,
    'ytick.right': True,

    # axis line thickness
    'axes.linewidth': 1.8
})


spp_1c40freq, spp_1c40smooth  = get_vdos('vdos_300K_1c40.dat')
spp_2c40freq, spp_2c40smooth = get_vdos('vdos_300K_2c40.dat')
spp_2d40freq, spp_2d40smooth = get_vdos('vdos_300K_2d40.dat')
spp_3d40freq, spp_3d40smooth = get_vdos('vdos_300K_3d40.dat')
spp_1c80freq, spp_1c80smooth = get_vdos('vdos_300K_1c80.dat')
spp_2c80freq, spp_2c80smooth = get_vdos('vdos_300K_2c80.dat')
spp_2d80freq, spp_2d80smooth = get_vdos('vdos_300K_2d80.dat')
spp_3d80freq, spp_3d80smooth = get_vdos('vdos_300K_3d80.dat')
spp_1c120freq, spp_1c120smooth = get_vdos('vdos_300K_1c120.dat')
spp_2c120freq, spp_2c120smooth = get_vdos('vdos_300K_2c120.dat')
spp_2d120freq, spp_2d120smooth = get_vdos('vdos_300K_2d120.dat')
spp_3d120freq, spp_3d120smooth = get_vdos('vdos_300K_3d120.dat')


plt.figure()
plt.plot(spp_1c40freq, spp_1c40smooth, color='red', linewidth=2, label='DP 40')
plt.plot(spp_1c80freq, spp_1c80smooth, color='blue', linewidth=2, label='DP 80')
plt.plot(spp_1c120freq, spp_1c120smooth, color='black', linewidth=2, label='DP 120')
plt.xlabel('Frequency (THz)')
plt.ylabel('VDOS (arb. units)')
plt.xlim(0, 20)
plt.ylim(0, )
plt.yticks([])
#plt.legend(frameon=False)
plt.savefig('vdos_smooth_savgol_sPP_1chain.png', bbox_inches='tight', dpi=1000, transparent=True)
plt.close()

plt.figure()
plt.plot(spp_1c40freq, spp_1c40smooth, color='red', linewidth=2, label='1 chain')
plt.plot(spp_3d40freq, spp_3d40smooth, color='green', linewidth=2, label='Bulk')
plt.xlabel('Frequency (THz)')
plt.ylabel('VDOS (arb. units)')
plt.xlim(0, 20)
plt.ylim(0, )
plt.yticks([])
#plt.legend(frameon=False)
plt.savefig('vdos_smooth_savgol_sPP_sc_cr_dp40.png', bbox_inches='tight', dpi=1000, transparent=True)
plt.close()

plt.figure()
plt.plot(spp_1c120freq, spp_1c120smooth, color='black', linewidth=2, label='1 chain')
plt.plot(spp_3d120freq, spp_3d120smooth, color='firebrick', linewidth=2, label='Bulk')
plt.xlabel('Frequency (THz)')
plt.ylabel('VDOS (arb. units)')
plt.xlim(0, 20)
plt.ylim(0, )
plt.yticks([])
#plt.legend(frameon=False)
plt.savefig('vdos_smooth_savgol_sPP_sc_cr_dp120.png', bbox_inches='tight', dpi=1000, transparent=True)
plt.close()
