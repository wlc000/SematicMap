# Data Introduction

- `porto/` is the directory for raw trajectory data, training set/validation set/test set. The `id` column is the unique id of the trajectory, the `path` column is the road segment ID list, and the `tlist` is the corresponding timestamp(UTC) list. Other columns are useless.
- `porto_roadmap_edge/` is a directory of road network data. The `.geo` file is the road segment table and the `.rel` file is the road segment link relationship table.
- `porto_roadmap_edge_porto_True_1_merge/` is the directory of processed road network data, read by the model.
- `vocab_porto_True_1_merge.pkl` is the remapping table of the road segment ID, read by the model.

