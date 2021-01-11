import java.util.Scanner;
import java.io.File;
import java.util.ArrayList;

public class d06 { 
    public static int part1(ArrayList<String> groups) {
        int sum = 0;
        for (String allAnswers : groups) {
            allAnswers.replace("\n", ""); // Remove all newlines
            sum += countUnique(allAnswers);
        }
        return sum;
    }
    
    public static int countUnique(String str) {
        int unique = 0;
        for (int i = 0; i < str.length(); i++)
            if (str.indexOf(str.charAt(i)) == i)
                unique++;
        return unique;
    }

    public static int part2(ArrayList<String> groups) {
        int sum = 0;
        for (String allAnswers : groups) {
            String[] sepAnswers = allAnswers.split("\n", 0);
            sum += countParallels(sepAnswers);
        }
        return sum;
    }

    public static int countParallels(String[] strs) {
        char[] cs = strs[0].toCharArray();
        int ubiquitous = 0;
        for (char c : cs) {
            int present = 1;
            for (String str : strs)
                present = (str.indexOf(c) < 0) ? 0 : present;
            ubiquitous += present;
        }
        return ubiquitous;
    }

    /* Separate input into strings that represent the all answers
        from each group */
    public static ArrayList<String> getGroups() {
        ArrayList<String> groups = new ArrayList<String>();
        try {
            File fd = new File("../inputs/d06");
            Scanner scn = new Scanner(fd);
            scn.useDelimiter("\n\n");
            while (scn.hasNext()) {
                String answers = scn.next();
                groups.add(answers);
            }
            scn.close();
        }
        catch (Exception e) {
            System.out.println(e);
        }
        return groups;
    }

    public static void main(String[] args) {
        ArrayList<String> groups = getGroups();
        System.out.println("Part 1: " + part1(groups));
        System.out.println("Part 2: " + part2(groups));
    }
}
