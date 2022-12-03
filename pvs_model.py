import numpy as np
def pvs_model(vgvd, idelta, ivxo, iwrs, imu, iss, ivt0):
    import params
    # Physical para
    type0 = params.type0
    phit = params.phit

    # Device para
    # for Fin height = 20nm, Gate length = 100nm
    width = params.Width * 1e-7     # Transistor width [cm]
    lg = params.Lg * 1e-7           # Transistor gate length [cm]
    height = params.Height * 1e-7   # Transistor height [cm]
    cg = params.Cg

    # Empirical para
    beta = params.beta
    alpha = params.alpha

    # delta: DIBL 
    # vxo: VS's velocity [cm/s]
    # WRs(Rd): parastitic risistance for S and D [Ohms-cm]
    # mu: mobility [cm^2/V·s]
    # S: Subthreshold swing [V/dec]
    # VT0: threshold voltage [V]
    #fitted coefficients
    delta = idelta
    vxo = ivxo * 1e7
    wrs = iwrs * 1e-4
    mu = imu
    ss = iss
    vt0 = ivt0

    # bias values
    vgdata = vgvd[0]
    vddata = vgvd[1]

    # calculate
    logId = [] 
    for i in range(len(vgdata)):
        vg = vgdata[i]
        vd = vddata[i]

        vd = np.abs(vd)
        vg = max(type0 * vg, type0 * (vg - vd))

        dir = type0 * np.sign(vd)

        cinv = cg # generally speaking, the capaicitance of strong inversion is the Cg

        # Qixo 
        vt = vt0 - delta * vd
        Ff = 1 / (1 + np.exp((vg - (vt - alpha * phit / 2))/(alpha * phit)))
        n = ss / (phit * np.log(10))
        Qixo = cinv * n * phit * np.log(1 + np.exp((vg - (vt - alpha * phit * Ff)) / (n * phit)))

        # Vxo
        v = (Ff + (1 - Ff) / (1 + wrs * cg * (1 + 2 * delta) * vxo)) * vxo

        # Fs
        vdsats = 2 * wrs * Qixo * v + v * lg / mu
        vdsat = vdsats * (1 - Ff) + phit * Ff
        Fs = (vd / vdsat) / (pow((1 + pow((vd / vdsat), beta)),(1 / beta)))

        # Id
        Id0 = (height * 2 + width) * Qixo * v * Fs * type0 * dir
        
        logId.append(np.log10(Id0))
        
    return np.array(logId)
