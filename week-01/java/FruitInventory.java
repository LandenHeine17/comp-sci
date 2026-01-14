import java.util.HashMap;
import java.util.Scanner;

public class FruitInventory {
    public static void main(String[] args) {
        String newFood; int newAmount; char repeat;
        Scanner keyboard = new Scanner(System.in);
        HashMap<String, Integer> food = new HashMap<String, Integer>();

        System.out.println("==========Welcome to your Pantry==========");

        while (true) {
            System.out.print("Enter a food to add: ");
            newFood = keyboard.next();

            System.out.print("Enter the amount: ");
            newAmount = keyboard.nextInt();

            food.put(newFood, newAmount);

            System.out.println(showItems(food));

            System.out.print("Would you like to go again(Y/N): ");
            repeat = Character.toLowerCase(keyboard.next().charAt(0));
            if (repeat != 'y') {
                break;
            }
        }
    }

    public static String showItems(HashMap<String, Integer> hashMap) {
        String output = "\n";
        for (String entry : hashMap.keySet()) {
            output += "Key: "+entry+", Value: " + hashMap.get(entry)+"\n";
        }
        return output;
    }

}