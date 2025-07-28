#!/bin/bash
exp_name="${1:-no_pc_more}"

proj_name="${2:-pole}"

method="${3:-splatfacto-big}"

max_gs="${4:-1000000}"

stop_split_at="${5:-15000}"

#!/bin/bash
sbatch <<EOT
#!/bin/bash

#SBATCH --job-name=tetra_benchmark
#SBATCH --account=OPEN-29-7
#SBATCH --partition qgpu
#SBATCH --time 2-00:00:00

ml --force purge

apptainer exec --userns --writable --nv --no-home --cleanenv --home /home/user tetra.sbox \
  ns-train $method --vis wandb \
    --project-name $proj_name \
    --experiment-name $exp_name \
    \
    --max_num_iterations 300000 \
    \
    --pipeline.model.max_gs_num $max_gs \
    \
    --pipeline.model.stop_split_at $stop_split_at \
    \
    --data pole_data/policko_dataset/

EOT