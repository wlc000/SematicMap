import os
import torch
from libcity.pipeline.pipeline import run_model


eta_flag = True # 需要跑网页的时候，需要设置成True



def eta(path, start_time):
    print('333',os.getcwd())
    tlist = [start_time] + [0] * (len(path)-1)
    with open("./raw_data/porto/porto_test2.csv", "w") as f:
        f.write('id;path;tlist;usr_id;traj_id;vflag;start_time\n')
        f.write('0;{};{};0;0;0;7\n'.format(str(path), str(tlist)))
    run_eta_model()
    with open("ans.txt") as f:
        prediction = float(f.readline())
        minute = int(prediction)
        second = int((prediction - minute)*60)
    return '%d分%d秒' % (minute, second)


def run_eta_model():
    other_args = {
        'gpu': False,
        'batch_size':1,
        'testonly':True,
    }

    run_model(task='trajectory_embedding', model_name='LinearETA',
              dataset_name='porto', config_file='porto', train=False,
              other_args=other_args
              )


if __name__ == '__main__':
    os.chdir('../')
    print('222',os.getcwd())
    p = [1856, 1871, 1853, 6446, 1852, 1868, 1861, 1857, 912, 5252, 9696, 743]
    print(eta(p, 1374232948))

