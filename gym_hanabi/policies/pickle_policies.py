#! /usr/bin/env python

import pickle

import gym
from gym_hanabi.policies.heuristic_policy import HeuristicPolicy
from gym_hanabi.policies.heuristic_simple_policy import HeuristicSimplePolicy
from gym_hanabi.policies.keyboard_policy import KeyboardPolicy
from gym_hanabi.policies.random_policy import RandomPolicy

def main():
    env_player_name_templates = [
        (gym.make("HanabiSelf-v0").env,
         2,
         "{}Policy"),
        (gym.make("MediumHanabiSelf-v0").env,
         2,
         "Medium{}Policy"),
        (gym.make("MiniHanabiSelf-v0").env,
         2,
         "Mini{}Policy"),
        (gym.make("MiniHanabiLotsOfInfoSelf-v0").env,
         2,
         "Mini{}LotsOfInfoPolicy"),
        (gym.make("MiniHanabiLotsOfTurnsSelf-v0").env,
         2,
         "Mini{}LotsOfTurnsPolicy"),
        (gym.make("MiniHanabiLinearRewardSelf-v0").env,
         2,
         "Mini{}LinearRewardPolicy"),
        (gym.make("MiniHanabiSquaredRewardSelf-v0").env,
         2,
         "Mini{}SquaredRewardPolicy"),
        (gym.make("MiniHanabiSkewedRewardSelf-v0").env,
         2,
         "Mini{}SkewedRewardPolicy"),
        (gym.make("MiniHanabi3PSelf-v0").env,
         3,
         "Mini{}3PPolicy"),
        (gym.make("MiniHanabiFlattenedSpaceSelf-v0").env,
         2,
         "Mini{}FlattenedSpacePolicy"),
        (gym.make("MiniHanabiFlattenedSpace3PSelf-v0").env,
         3,
         "Mini{}FlattenedSpace3PPolicy"),
    ]

    for env, num_players, name_template in env_player_name_templates:
        name = name_template.format("Keyboard")
        with open("pickled_policies/{}.pickle".format(name), "wb") as f:
            pickle.dump(KeyboardPolicy(env), f)

        if num_players == 2:
            name = name_template.format("Heuristic")
            with open("pickled_policies/{}.pickle".format(name), "wb") as f:
                pickle.dump(HeuristicPolicy(env), f)

            name = name_template.format("HeuristicSimple")
            with open("pickled_policies/{}.pickle".format(name), "wb") as f:
                pickle.dump(HeuristicSimplePolicy(env), f)

        name = name_template.format("Random")
        with open("pickled_policies/{}.pickle".format(name), "wb") as f:
            pickle.dump(RandomPolicy(env), f)

if __name__ == "__main__":
    main()
