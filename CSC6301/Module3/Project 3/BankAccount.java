/**
 * Simple program that includes 3 classes that interact with each other and demonstrates
 * how a person can have a bank account, deposit and withdraw money from it, and display
 * their account information as well. I could not find a 3 class example on the internet,
 * so I am instead using this generated example.
 * 
 * BankAccount Class - Represents a bank account with an account number and balance. It will
 * have methods to deposit, withdraw, and display account info
 * @author James Zafiri
 * @version 1.0.0
 * @since Week 3 of CSC6031
 */
public class BankAccount {
    private String accountNumber;
    private double balance;
    /**
     * Sets up a bank account to use
     * @param accountNumber the number that will be associated with this account
     */
    public BankAccount(String accountNumber) {
        this.accountNumber = accountNumber;
        this.balance = 0.0;
    }
    /**
     * This method deposits money into the bank account
     * @param amount the amount of money that is passed in to deposit
     */
    public void deposit(double amount) {
        balance += amount;
    }
    /**
     * This method withdraws money from the bank account
     * @param amount the amount of money that is passed in to withdraw
     */
    public void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
        } else {
            System.out.println("Insufficient funds.");
        }
    }
    /**
     * This method displays the information of the bank account
     * There are no paramaters being passed in
     */
    public void displayInfo() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Balance: $" + balance);
    }
}
