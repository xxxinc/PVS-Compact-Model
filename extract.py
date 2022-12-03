import opt_para
import numpy as np
import params
import matplotlib.pyplot as plt
import pvs_model
def extract():
    # initial guess of fitting para
    delta = params.delta
    vxo = params.vxo
    wrs = params.WRs
    mu = params.mu
    ss = params.ss
    vt0 = params.vt0 

    para_init = [delta, vxo, wrs, mu, ss, vt0]

    para_op = opt_para.opt_para(para_init)

    ivdata = np.loadtxt('data.txt')
    
    ivlist = list(ivdata)
    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    for i in range(8):
        vg = []
        vd = []
        id = []
        for j in range(31):
            dot = ivlist.pop(0)
            vg.append(dot[0])
            vd.append(dot[1])
            id.append(dot[2])
        label_ = str(vd[0]) + '-TCAD'
        label_pre = str(vd[0]) + '-PVS'
        id_pre = pvs_model.pvs_model(np.array([vg, vd]), *para_op)

        ax1.semilogy(vg, id, label = label_)
        ax1.semilogy(vg, pow(10,id_pre), '.', label = label_pre)
    plt.xlabel('Vg(V)',fontsize = 14)
    plt.ylabel('Id(A)',fontsize = 14)
    plt.title('Transfer Id-Vg Curve', fontsize = 14)
    plt.legend(fontsize = 9)
    fig1.savefig('idvg')

    ivlist.pop(0) # 多了一个不合理数据 先弹出去

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    for i in range(8):
        vg = []
        vd = []
        id = []
        for j in range(30):
            dot = ivlist.pop(0)
            vg.append(dot[0])
            vd.append(dot[1])
            id.append(dot[2])
        print(vg)
        print(len(vg))
        label_ = str(vg[0]) + '-TCAD'
        label_pre = str(vg[0]) + '-PVS'
        id_pre = pvs_model.pvs_model(np.array([vg, vd]), *para_op)

        ax2.plot(vd, id, label = label_)
        ax2.plot(vd, pow(10,id_pre), '.', label = label_pre)
    plt.xlabel('Vd(V)',fontsize = 14)
    plt.ylabel('Id(A)',fontsize = 14)
    plt.title('Output Id-Vg Curve', fontsize = 14)
    plt.legend(fontsize = 9)
    fig2.savefig('idvd')


if __name__ == '__main__':
    extract()