"""  In a particular pain clinic, 10% of patients are prescribed narcotic pain killers.Overall,
    five percent of the clinic’s patients are addicted to narcotics (including pain killers and illegal substances).
    Out of all the people prescribed pain pills, 8% are addicts.
    If a patient is an addict, write a program to find the  probability that they will be prescribed pain pills """

from myprograms.WEEK_3.Utility.utilityProb_Stat import ProbabilityStatistics


class Clinic:
    # prescribed narcotic pain killers
    p_prescribed_painkillers = 0.1
    # not prescribed narcotic pain killers
    p_non_prescribed_painkillers = 0.9
    # addicted patients out of all prescribed pain pills
    p_addicts_given_prescribed_painkillers = 0.08
    # patients addicted to narcotic
    p_addicts_given_non_prescribed_painkillers = 0.05

    # getting probability of patients that will be prescribed pain pills
    result = ProbabilityStatistics.prescribed_pain_killers_given_addict(p_prescribed_painkillers,
                                                                        p_addicts_given_prescribed_painkillers,
                                                                        p_non_prescribed_painkillers,
                                                                        p_addicts_given_non_prescribed_painkillers)
    print("Probability that patients will be prescribed pain pills : ", result)


# instantiation
Clinic_object = Clinic()
