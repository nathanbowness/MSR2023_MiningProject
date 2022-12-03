# HPCnet

## Installation

### Install
Install this library by running the following command:

```shell
cd pointnet2
python setup.py install
cd ../

cd HPCnet
python setup.py install
cd ../
```

## Examples

### KITTI
data:
```
 ├──data
 │  ├── KITTI
 │  │   ├── ImageSets
 │  │   ├── object
 │  │   │   ├──training
 │  │   │      ├──calib & velodyne & label_2 & image_2
```

train and test:
```
python tools/kitti_train_test.py
```

net arch in `HPCnet/hpcnet_kitti.py`

### ModelNet40
put data in `data/modelnet40_normal_resampled`

train `tools/train_cls.py`

test `tools/test_cls.py`

net in `HPCnet/hpcnet_cls_msg.py`

### S3DIS
data:
`s3dis/Stanford3dDataset_v1.2_Aligned_Version`

```
cd data_utils
python collect_indoor3d_data.py
```

```
python tools/train_semseg.py --model pointnet2_sem_seg --test_area 5
python tools/test_semseg.py --log_dir pointnet2_sem_seg --test_area 5 --visual
```
