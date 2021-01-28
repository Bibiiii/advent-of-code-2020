import java.io.File;  // for reading txt file
import java.util.Scanner; // read txt file
import java.io.FileNotFoundException;  // error handling

public class Main { 
    public int getNumOfTrees(int numToTraverse, int numToSkip) {
      try {
        File trees = new File("trees.txt");
        Scanner myReader = new Scanner(trees);
        int column = 0; // column position
        int treeCounter = 0; // number of trees encountered
        int row = 0; // row position
        while (myReader.hasNextLine()) {
          String data = myReader.nextLine();
          String slope = data.repeat(100); // repeat map arbitrarily
          if ((row % numToSkip) == 0) { // if we need to skip lines, do not add to counters
            if (slope.charAt(column) == '#') {
              treeCounter++;
            }
            column+=numToTraverse;
          }
          row+=1;
        }
        myReader.close();
        System.out.println("Number of trees: " + treeCounter);
        return treeCounter;
      } catch (FileNotFoundException e) {
        System.out.println("An error has occurred.");
        e.printStackTrace();
        return 0;
      }
    }

    public long multiplyTrees(int[][] experiments) {
      long finalNum = 1;
      for (int i = 0; i < experiments.length; i++) {
        int numOfTrees = getNumOfTrees(experiments[i][0], experiments[i][1]);
        finalNum *= numOfTrees; // multiply final number by number of trees in this iteration
      }
      return finalNum;
    }

    public static void main(String[] args) {
        Main toboggan = new Main();
        /* set up experiments in format:
         {number of place to move, rows to skip}
        */
        int[][] experiments =
          {
            {1,1},
            {3,1},
            {5,1},
            {7,1},
            {1,2}
          };
        long finalNumber = toboggan.multiplyTrees(experiments);
        System.out.println("Final number is: " + finalNumber);
      }
} 