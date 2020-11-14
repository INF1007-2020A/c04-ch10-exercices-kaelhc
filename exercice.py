#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as ply
from scipy import integrate



# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(start=-1.3,stop=2.5,num=64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:



    return np.array([(np.sqrt(c[0]**2 + c[1]**2),np.arctan(c[1],c[0])) for c in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:


    return np.abs(values-number).argmin()


def creat_plot() :
    x = np.linspace(-1, 1, num=250)
    y = x ** 2 * np.sin(1 / x ** 2) + x

    ply.scatter(x, y, label="point")
    ply.xlim(-2, 2)
    ply.plot(x, y, label="line", color="r")
    ply.title("hello , 1st function")
    ply.xlabel("x")
    ply.ylabel("y")
    ply.legend()
    ply.show()


def monte_carlo(iteration=50000)->float :
    x_inside=[]
    y_inside=[]
    x_outside = []
    y_outside = []
    p=0

    for i in range(iteration) :

        x=np.random.random()
        y=np.random.random()
        if np.sqrt(x**2+y**2) < 1 :
            x_inside.append(x)
            y_inside.append(y)
            p+=1

        else:
           x_outside.append(x)
           y_outside.append(y)

    ply.scatter(x_inside,y_inside)
    ply.scatter(x_outside,y_outside)
    ply.show()
    return 4*p/iteration


def integrale()->tuple :
    result_inf=integrate.quad(lambda x : np.exp(-x**2) , -np.inf , np.inf )

    x=np.arange(-4,4,0.1)
    y=[integrate.quad(lambda x: np.exp(-x**2) , 0 ,values )[0] for values in x ]
    ply.plot(x,y)
    ply.show()




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    creat_plot()
    print(linear_values())

    print(monte_carlo())
    integrale()


