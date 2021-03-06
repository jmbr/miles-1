"""Analysis module for the command line interface.

"""


__all__ = ['analyze']

from miles import (TransitionKernel, save_distributions)


def analyze(kernel: TransitionKernel,
            stationary_distributions: str,
            transition_matrix: str, lag_time_matrix: str,
            stationary_flux: str, local_mfpts: str,
            stationary_probability: str) -> float:
    """Analyze the result of a long-trajectory simulation.

    This function loads a database generated by the `miles long`
    command and uses the obtained first hitting points and lag times
    to estimate the stationary distribution and the global mean first
    passage time.

    Parameters
    ----------
    kernel : TransitionKernel
        The transition kernel to be analyzed.
    stationary_distributions : str
        The name of the file where to store the stationary
        distribution.
    transition_matrix : str
        File name where to save the transition matrix.
    lag_time_matrix : str
        File name where to save the matrix of local lag times.
    stationary_flux: str
        File name where the stationary flux vector will be stored.
    local_mfpts : str
        File name where the vector of local mean first passage times
        will be saved.
    stationary_probability : str
        File name containing the stationary probability vector.

    Returns
    -------
    mfpt : float
        Mean first passage time from reactant to product.

    """
    # kernel = TransitionKernel(simulation.database)
    kernel.save_distributions()

    distributions, q = kernel.compute_distributions()

    save_distributions(distributions, stationary_distributions)

    kernel.matrices.save(transition_matrix, lag_time_matrix,
                         stationary_flux, local_mfpts,
                         stationary_probability)

    return kernel.matrices.mfpt
