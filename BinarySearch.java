import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.Scanner;
public class BinarySearch {
//    write the binary search for a random number from 1 to 100
//    take the number from user
//    put some needed validation on input
//    type the number of steps that it takes

    public static void main(String[] args) {
        int userNumber = getNumber();
        while (userNumber == -1){
            userNumber = getNumber();
        }
        System.out.println(
                "The number has been found! \nthe total steps : " + binarySearchSteps(userNumber)
        );
    }

    private static int getNumber(){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please Enter a number between 1 to 100 : ");
        try {
            int userNumber = scanner.nextInt();
            if (userNumber < 100 && userNumber > 0){
                return userNumber;
            }else {
                System.out.println("Enter a number between 1 to 100 !");
            }

        }catch (InputMismatchException e){
            System.out.println("Please enter a valid value");
        }
        return -1;
    }

    private static int binarySearchSteps(int number){
//        creating the array from 1 to 100
        int[] myArray = new int[100];
        for (int i = 0 ; i < myArray.length ; i++){
            myArray[i] = i+1;
        }

        int stepsCounter = 0;

        int firstIndex = 0;
        int lastIndex = myArray.length-1;

        while (true){
            stepsCounter++;
            int midIndex = (firstIndex+lastIndex) /2;
            if (myArray[midIndex] == number){
                break;
            }else if (myArray[midIndex] > number){
                lastIndex = midIndex;
                continue;
            }else {
                firstIndex = midIndex;
                continue;
            }
        }

        return stepsCounter;
    }

}
