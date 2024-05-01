import numpy as np

def cost_function( x, y, theta0, theta1 ):
    """Compute the squared error cost function

    Inputs:
    x        vector of length m containing x values
    y        vector of length m containing y values
    theta_0  (scalar) intercept parameter
    theta_1  (scalar) slope parameter

    Returns:
    cost     (scalar) the cost
    """

    #cost = 0.0 (i dont use for loop so i dont need this line)

    ##################################################
    # TODO: write code here to compute cost correctly

    # predicted values
    preds = theta0 + theta1 * x

    # squared errors
    squared_errors = (preds - y) ** 2

    # cost function (mse)
    cost = (1 / (2)) * np.sum(squared_errors)

    ##################################################
    
    return cost


def gradient(x, y, theta_0, theta_1):
    """Compute the partial derivative of the squared error cost function

    Inputs:
    x          vector of length m containing x values
    y          vector of length m containing y values
    theta_0    (scalar) intercept parameter
    theta_1    (scalar) slope parameter

    Returns:
    d_theta_0  (scalar) Partial derivative of cost function wrt theta_0
    d_theta_1  (scalar) Partial derivative of cost function wrt theta_1
    """
    #d_theta_0, d_theta_1 = 0, 0 (i dont use for loop so i dont need this line)

    ##################################################
    # TODO: write code here to compute partial derivatives correctly


    # predicted values
    predictions = theta_0 + theta_1 * x

    # errors
    errors = predictions - y

    # partial derivatives
    d_theta_0 = np.sum(errors)
    d_theta_1 = np.sum(errors * x)


    ##################################################

    return d_theta_0, d_theta_1 # return is a tuple

def explicit_answer(x, y):
    """Compute the explicit values of theta1 and theta2

    Inputs:
    x          vector of length m containing x values
    y          vector of length m containing y values

    Returns:
    theta_0  (scalar) intercept of line
    theta_1  (scalar) slope of line
    """
    
    
    ##################################################
    # TODO: write code here to compute explicit values of theta_0 and theta_1

    # add a column of ones for the bias term
    x_b = np.c_[np.ones((len(x), 1)), x]

    # explicit values of theta using the closed-form of cost function
    theta = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)

    # theta_0 (intercept) and theta_1 (slope)
    theta_0 = theta[0]
    theta_1 = theta[1]

    ##################################################
    return theta_0, theta_1