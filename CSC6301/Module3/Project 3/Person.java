/**
 * Simple program that includes 3 classes that interact with each other and demonstrates
 * how a person can have a bank account, deposit and withdraw money from it, and display
 * their account information as well. I could not find a 3 class example on the internet,
 * so I am instead using this generated example.
 * 
 * Person Class - Represents a person and includes a name, age, and bank account. They will
 * be able to deposit and withdraw money.
 * @author James Zafiri
 * @version 1.0.0
 * @since Week 3 of CSC6031
 */
public class Person {
    private String name;
    private int age;
    private BankAccount account;
    /**
     * Creates a person that will be the owner of a bank account
     * @param name the name of the person who owns the account
     * @param age the age of the person who owns the account
     */
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
        this.account = null; // Initialize to null as the person may not have an account initially
    }
    /**
     * Sets an account for the person using the BankAccount class
     * @param account the bank account that will be passed in to work with
     */
    public void setAccount(BankAccount account) {
        this.account = account;
    }
    /**
     * This method deposits money into the persons bank account
     * @param amount the amount of money that is passed in to deposit
     */
    public void deposit(double amount) {
        if (account != null) {
            account.deposit(amount);
        } else {
            System.out.println(name + " does not have a bank account.");
        }
    }
    /**
     * This method withdraws money from the persons bank account
     * @param amount the amount of money that is passed in to withdraw
     */
    public void withdraw(double amount) {
        if (account != null) {
            account.withdraw(amount);
        } else {
            System.out.println(name + " does not have a bank account.");
        }
    }
    /**
     * This method displays the information of the persons bank account
     * There are no paramaters being passed in
     */
    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        if (account != null) {
            account.displayInfo();
        } else {
            System.out.println(name + " does not have a bank account.");
        }
    }
}
