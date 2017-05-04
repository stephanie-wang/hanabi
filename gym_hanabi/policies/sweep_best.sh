#! /usr/bin/env bash

set -euo pipefail

main() {
    N_ITR=8000
    N_REPEATS=16

    # Self
    python trpo_self.py \
        MiniHanabiSelf-v0 \
        pickled_policies/mini_trpo_self_best.pickle \
        logs/mini_trpo_self_best \
        --n_itr=$N_ITR

    python trpo_self.py \
        MediumHanabiSelf-v0 \
        pickled_policies/medium_trpo_self_best.pickle \
        logs/medium_trpo_self_best \
        --n_itr=$N_ITR

    python trpo_self.py \
        HanabiSelf-v0 \
        pickled_policies/trpo_self_best.pickle \
        logs/trpo_self_best \
        --n_itr=$N_ITR

    # Staggered
    python trpo_staggered.py \
        MiniHanabiAi-v0 \
        pickled_policies/mini_trpo_staggered_best.pickle \
        logs/mini_trpo_staggered_best \
        --n_itr=$(($N_ITR / $N_REPEATS)) \
        --n_repeats=20

    python trpo_staggered.py \
        MediumHanabiAi-v0 \
        pickled_policies/medium_trpo_staggered_best.pickle \
        logs/medium_trpo_staggered_best \
        --n_itr=$(($N_ITR / $N_REPEATS)) \
        --n_repeats=20

    python trpo_staggered.py \
        HanabiAi-v0 \
        pickled_policies/trpo_staggered_best.pickle \
        logs/trpo_staggered_best \
        --n_itr=$(($N_ITR / $N_REPEATS)) \
        --n_repeats=$N_REPEATS

    # AI
    python trpo_ai.py \
        MiniHanabiAi-v0 \
        pickled_policies/MiniHeuristicPolicy.pickle \
        pickled_policies/mini_trpo_ai_best.pickle \
        logs/mini_trpo_ai_best \
        --n_itr=$N_ITR

    python trpo_ai.py \
        MediumHanabiAi-v0 \
        pickled_policies/MediumHeuristicPolicy.pickle \
        pickled_policies/medium_trpo_ai_best.pickle \
        logs/medium_trpo_ai_best \
        --n_itr=$N_ITR

    python trpo_ai.py \
        HanabiAi-v0 \
        pickled_policies/HeuristicPolicy.pickle \
        pickled_policies/trpo_ai_best.pickle \
        logs/trpo_ai_best \
        --n_itr=$N_ITR
}

main