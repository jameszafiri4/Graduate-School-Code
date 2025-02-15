/*
Simple program that returns the tribonacci sequence of a number.
The program uses the number 20 as the input for this example.
This code is written in Go and was tested on Visual Studio Code.
James Zafiri
version 1.0.0
Week 3 of CSC6303
*/

package main

import "fmt"

// function that will calculate the sequence up to n
func tribonacci(n int) []int {
	// if n is negative, return empty array
	if n <= 0 {
		return []int{}
	} else if n == 1 {
		// if n is 1, return array with 0
		return []int{0}
	} else if n == 2 {
		// if n is 2, return array wiht a 0 and 1
		return []int{0, 1}
	} else {
		// initializing sequence with first 3 numbers
		fibSeq := []int{1, 1, 1}
		// caluclating the following numbers of the sequence
		for i := 3; i < n; i++ {
			// next numbers is calculated by summing up the last 3 numbers
			nextNum := fibSeq[i-1] + fibSeq[i-2] + fibSeq[i-3]
			// adding next number to the sequenece
			fibSeq = append(fibSeq, nextNum)
		}
		return fibSeq
	}
}

func main() {
	fmt.Println(tribonacci(20))
}
