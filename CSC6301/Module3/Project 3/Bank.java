/**
 * Simple program that includes 3 classes that interact with each other and demonstrates
 * how a person can have a bank account, deposit and withdraw money from it, and display
 * their account information as well. I could not find a 3 class example on the internet,
 * so I am instead using this generated example.
 * 
 * Bank Class - This contains the main method to create instances of Person and BankAccount
 * @author James Zafiri
 * @version 1.0.0
 * @since Week 3 of CSC6031
 */
public class Bank {
    /**
     * Instantiates a person and their bank account to show the info associated with it
     * @param args an array of strings that includes a person and their account number
     */
    public static void main(String[] args) {
        Person person1 = new Person("Alice", 30);
        Person person2 = new Person("Bob", 25);

        BankAccount account1 = new BankAccount("12345");
        BankAccount account2 = new BankAccount("67890");

        person1.setAccount(account1);
        person2.setAccount(account2);

        person1.deposit(1000);
        person2.deposit(500);

        person1.withdraw(200);
        person2.withdraw(100);

        System.out.println("Person 1 Info:");
        person1.displayInfo();

        System.out.println("\nPerson 2 Info:");
        person2.displayInfo();
    }
}
