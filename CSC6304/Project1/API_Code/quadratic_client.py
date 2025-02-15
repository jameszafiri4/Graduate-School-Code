'''
Simple program (API) that uses gRPC to solve a quadratic equation based
on receiving coefficients from the user. This is the client file that
obtains the inputs as well as requesting the server to receive a solution.
This code is written in Python and was tested on Visual Studio Code.
James Zafiri
version 1.0.0
Week 2 of CSC6303
'''

from __future__ import print_function

import logging

import grpc
import quadratic_pb2
import quadratic_pb2_grpc


def get_coefficients():
    '''
    This function is where we obtain the client inputs as floats
    and also make sure they are valid real numbers.
    '''
    try:
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        c = float(input("Enter the coefficient c: "))
        return a, b, c
    except ValueError:
        print("Please enter valid numerical coefficients.")
        return get_coefficients()


def run():
    '''
    This function is where we will connect the client to the server file
    and pass through the coeffiecients we obtained. We will then receive
    the solution that the server provided to show the user. This is where
    the stub file we created is used.
    '''
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = quadratic_pb2_grpc.QuadraticSolverStub(channel)
        a, b, c = get_coefficients()
        coefficients = quadratic_pb2.Coefficients(a=a, b=b, c=c)
        response = stub.Solve(coefficients)
        print("Solution received from server:", response.result)


if __name__ == "__main__":
    logging.basicConfig()
    run()
