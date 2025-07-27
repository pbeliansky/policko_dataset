#!/bin/bash
exp="${1:-testik}"

prune_start="${2:-50000}"
prune_each="${3:-5000}"
prune_qant="${4:-0.4}"

data="${5:-external://blender/lego}"

proj_name="${6:-nerfbaselines-test}"

output_name="${proj_name}/${exp}"

#!/bin/bash
sbatch <<EOT
#!/bin/bash

#SBATCH --job-name=tetra_benchmark
#SBATCH --account=OPEN-29-7
#SBATCH --partition qgpu_exp
#SBATCH --time 2-00:00:00

ml --force purge

apptainer exec --userns --writable --nv --no-home --cleanenv --home /home/user tetra.sbox \
  ns-train splatfacto --vis wandb \
    \
    --data pole_data/policko_dataset/

EOT