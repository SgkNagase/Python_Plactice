# -*- coding: utf-8 -*-


class WorldHappinessReport(object):
    def __init__(self, id, country, region, happiness_rank, happiness_score):
        self.id = id
        self.country = country
        self.region = region
        self.happiness_rank = happiness_rank
        self.happiness_score = happiness_score

    def __str__(self):
        strings = []
        strings += ['id: {}'.format(self.id)]
        strings += ['country: {}'.format(self.country)]
        strings += ['region: {}'.format(self.region)]
        strings += ['happiness_rank: {}'.format(self.happiness_rank)]
        strings += ['happiness_score: {}'.format(self.happiness_score)]
        return '\n'.join(strings)
