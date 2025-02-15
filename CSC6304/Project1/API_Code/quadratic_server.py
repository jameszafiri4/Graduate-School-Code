'''
Simple program (API) that uses gRPC to solve a quadratic equation based
on receiving coefficients from the user. This is the server file that
contains the logic of actually providing a solution using the equation.
This code is written in Python and was tested on Visual Studio Code.
James Zafiri
version 1.0.0
Week 2 of CSC6303
'''

from concurrent import futures
import logging
import math

import grpc
import quadratic_pb2
import quadratic_pb2_grpc


class QuadraticSolverServicer(quadratic_pb2_grpc.QuadraticSolverServicer):
    '''
    This class is where we use the imported grpc stub to communicate with the
    server and client, as well as implementing the solution of the quadratic formula.
    This was based off of the gRPC example from class, but adding logic for a solution.
    '''
    def Solve(self, request, context):
        '''
        This method is where we receive 3 real values from the client and actually
        compute the solution of the quadratic equation to return as a string.
        '''
        # coefficients we are getting from the user (client)
        a, b, c = request.a, request.b, request.c
        # this is the discriminant portion of the equation in the numerator
        discriminant = b * b - 4 * a * c
        # if this is a positive number, we know we will get different real numbers for x1 and x2 (two real roots)
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return quadratic_pb2.Solution(result=f"Roots are real and distinct: x1 = {x1}, x2 = {x2}")
        # if this is zero, then we will get real numbers that are the same (one real root)
        elif discriminant == 0:
            x = -b / (2 * a)
            return quadratic_pb2.Solution(result=f"Roots are real and equal: x = {x}")
        # if negative, then this we get a complex answer (using i) so we will split our answers in x1 and x2 (two complex roots)
        else:
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
            return quadratic_pb2.Solution(result=f"Roots are complex: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")


def serve():
    '''
    This function is where we will get our server to work and initiate based on the
    stubs we created and imported.
    '''
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    quadratic_pb2_grpc.add_QuadraticSolverServicer_to_server(QuadraticSolverServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
