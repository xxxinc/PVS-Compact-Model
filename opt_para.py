import numpy as np
from scipy.optimize import curve_fit
import pvs_model
def opt_para(para_init):
    vd_data = []
    vg_data = []
    id_data = []

    dir_mian = r'C:\Users\xxxin\Documents\GitHub\DataBase\TCAD_data/'
    vv = ['0.05', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7']
    dir_vd = ['vd=', 'V-IdVg.csv']
    dir_vg = ['Vg=', 'V-IdVd.csv']

    for item in vv:
        filename = dir_mian + dir_vd[0] + item + dir_vd[1]

        with open(filename, encoding='utf-8') as file:
            content = file.readlines()
        vd = round(float(item),4)
        flag1 = 1
        flag2 = 1
        rag = [0, 0]

        content.pop(len(content)-1)

        for line in content:
            if flag1 == 1:
                flag1 = 0
                continue
            var = line[:-1].split(',')

            vg = float(var[0])
            id = float(var[1])
            if vg == 0:
                rag[0] = vg
                rag[1] = id
                continue
            else:
                if flag2 == 1:
                    flag2 = 0
                    vg_data.append(rag[0])
                    vd_data.append(vd)
                    id_data.append(rag[1])
                vg_data.append(vg)
                vd_data.append(vd)
                id_data.append(id)
    
    for item in vv:
        filename = dir_mian + dir_vg[0] + item + dir_vg[1]

        with open(filename, encoding='utf-8') as file:
            content = file.readlines()
        vg = round(float(item),4)
        flag1 = 1

        content.pop(len(content)-1)

        for line in content:
            if flag1 == 1:
                flag1 = 0
                continue
            var = line[:-1].split(',')
            vd = float(var[0])
            if vd == 0:
                continue
            id = float(var[1])
            vg_data.append(vg)
            vd_data.append(vd)
            id_data.append(id)

    x_data = np.array([vg_data, vd_data])
    y_data = np.log10(np.array(id_data))
    np.savetxt('data.txt',np.array([vg_data, vd_data, id_data]).T)
    upb = [0,   0.1, 1,   50,   0.059, 0.2]
    bob = [0.5, 10,  200, 1000, 0.1,   0.6]
    para_bounds=(upb, bob)
    popt, pcov = curve_fit(pvs_model.pvs_model, x_data, y_data, p0=para_init, bounds=para_bounds, method='trf')
    np.savetxt('paras.txt', popt)

    return popt


if __name__ == '__main__':
    opt_para(0)

    
