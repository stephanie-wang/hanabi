from gym_hanabi.envs import hanabi_env
import pickle


class HeuristicSimplePolicy(object):
    """ Simpler Heuristic policy for mini-hanabi (probably won't do well on
    larger hanabi) """

    def __init__(self, config):
        self.config = config

    def get_move(self, observation):
        observation = hanabi_env.GameStateObservation(self.config, observation)
        numcolors = len(self.config.colors)
        SKIPONEDISCARD = False
        SKIPTWODISCARD = True
        SKIPTHREEDISCARD = True

        # 1) walk through their cards and their info. if there's a one they
        # don't know about, tell them
        for card, cardinfo in zip(observation.them.cards, observation.them.info):
            if card.number == 1:
                print(card, cardinfo)
                if cardinfo.number is None and observation.num_tokens > 0:
                    print("informing about a one")
                    return hanabi_env.InformNumberMove(card.number)

        # 1, color? skip for now because ai doesn't appear to ever to color info

        # if we can't give info about ones, see if we can place any ones
        for cardind, cardinfo in enumerate(observation.you.info):
            if cardinfo.number == 1:
                print("played cards keys:", observation.played_cards.keys())

                # a) all ones are already there, so discard any ones
                if (len(observation.played_cards.keys()) == numcolors) and not SKIPONEDISCARD:
                    # all ones have been played, discard this one
                    print("discarding a one")
                    return hanabi_env.DiscardMove(cardind)
                # b) TODO check color (but we don't give color info currently)
                else:
                    print("playing a one")
                    return hanabi_env.PlayMove(cardind)

        # 3) walk through their cards and their info. if there's a two they
        # don't know about, tell them
        for card, cardinfo in zip(observation.them.cards, observation.them.info):
            if card.number == 2:
                print(card, cardinfo)
                if cardinfo.number is None and observation.num_tokens > 0:
                    print("informing about a two")
                    return hanabi_env.InformNumberMove(card.number)

        # if we can't give info about twos, see if we can place any twos
        for cardind, cardinfo in enumerate(observation.you.info):
            if cardinfo.number == 2:
                print("played cards keys:", observation.played_cards.keys())

                # a) all ones are already there, so discard any ones
                # TODO this discard method is incorrect for cards > 1
                if (len(observation.played_cards.keys()) == numcolors) and not SKIPTWODISCARD:
                    # all ones have been played, discard this one
                    print("discarding a two")
                    return hanabi_env.DiscardMove(cardind)
                # b) TODO check color (but we don't give color info currently)
                else:
                    print("playing a two")
                    return hanabi_env.PlayMove(cardind)

        # 3) walk through their cards and their info. if there's a three they
        # don't know about, tell them
        for card, cardinfo in zip(observation.them.cards, observation.them.info):
            if card.number == 3:
                print(card, cardinfo)
                if cardinfo.number is None and observation.num_tokens > 0:
                    print("informing about a three")
                    return hanabi_env.InformNumberMove(card.number)

        # if we can't give info about twos, see if we can place any twos
        for cardind, cardinfo in enumerate(observation.you.info):
            if cardinfo.number == 3:
                print("played cards keys:", observation.played_cards.keys())

                # a) all ones are already there, so discard any ones - will never happen for 3s
                if (len(observation.played_cards.keys()) == numcolors) and not SKIPTHREEDISCARD:
                    # all ones have been played, discard this one
                    print("discarding a two")
                    return hanabi_env.DiscardMove(cardind)
                # b) TODO check color (but we don't give color info currently)
                else:
                    print("playing a three")
                    return hanabi_env.PlayMove(cardind)

        # at this point, we have no info, random play or random discard? - 
        # TODO: don't randomly guess if there's only one fuse
#        if observation.num_fuses > 0:  #change back to 1 to do what the comment says
        return hanabi_env.PlayMove(0)
#        else:
#        return hanabi_env.DiscardMove(0)

    def get_action(self, observation):
        return (hanabi_env.move_to_sample(self.config, self.get_move(observation)), )

if __name__ == "__main__":
    configs_and_names = [
        (hanabi_env.HANABI_CONFIG, "HeuristicSimplePolicy"),
        (hanabi_env.MEDIUM_HANABI_CONFIG, "MediumHeuristicSimplePolicy"),
        (hanabi_env.MINI_HANABI_CONFIG, "MiniHeuristicSimplePolicy"),
        (hanabi_env.MINI_HANABI_LOTSOFINFO_CONFIG, "MiniHeuristicSimpleLotsOfInfoPolicy"),
        (hanabi_env.MINI_HANABI_LOTSOFTURNS_CONFIG, "MiniHeuristicSimpleLotsOfTurnsPolicy"),
        (hanabi_env.MINI_HANABI_LINEAR_REWARD_CONFIG, "MiniHeuristicSimpleLinearRewardPolicy"),
        (hanabi_env.MINI_HANABI_SQUARED_REWARD_CONFIG, "MiniHeuristicSimpleSquaredRewardPolicy"),
        (hanabi_env.MINI_HANABI_SKEWED_REWARD_CONFIG, "MiniHeuristicSimpleSkewedRewardPolicy"),
    ]

    for config, name in configs_and_names:
        with open("pickled_policies/{}.pickle".format(name), "wb") as f:
            pickle.dump(HeuristicSimplePolicy(config), f)