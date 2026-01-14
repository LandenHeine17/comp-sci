import java.util.HashMap;

public class FruitHashMap01 {
    public static void main(String[] args) {
        HashMap<String, Integer> myMap = new HashMap<String, Integer>();

        myMap.put("apple", 10);
        myMap.put("orange", 20);
        myMap.put("banana", 15);
        
        for (String entry : myMap.keySet()) {
            System.out.println("Key: "+entry+", Value: " + myMap.get(entry));
        }
    }
}