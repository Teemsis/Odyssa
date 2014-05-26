from Learner import Learner

class UKF(Learner):
    def __init__(self, alpha, beta, predict, update, smooth):
        self.alpha = alpha
        self.beta = beta
        self.predict = predict
        self.update = update
        self.smooth = smooth
    def setAlgo(self, algo):
        raise Exception("This method must be implemented")
    def smooth(self, observation, state_fct, obs_fct, precessNoise, measureNoise, meanPrior, covPrior):
        raise Exception("This method must be implemented")