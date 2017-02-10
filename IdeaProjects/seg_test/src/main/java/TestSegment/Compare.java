package TestSegment;

import Util.SysOp;

import java.io.*;
import java.nio.charset.Charset;

/**
 * Created by ethan on 17-1-20.
 */
public class Compare {

    public static void main(String args[]) throws Exception {

        Compare c = new Compare();
        SysOp s = new SysOp();
        String targetPath = s.getRoot();    // get target path

        // mark input file to output file
        String inputFile = targetPath + "/classes/files/film_combine.txt"; // path to input file
        String outputFile = targetPath + "/classes/files/film_mark_diff.txt";    // path to output file
        c.markDiffString(inputFile, outputFile);
    }


    public void markDiffString(String inputFile, String outputFile) throws Exception {

        // file to read
        InputStream fis = new FileInputStream(inputFile);
        InputStreamReader isr = new InputStreamReader(fis, Charset.forName("UTF-8"));
        BufferedReader br = new BufferedReader(isr);

        // file to write
        PrintWriter writer = new PrintWriter(outputFile, "UTF-8");

        // read, segment, then append line by line
        String line;
        while ((line = br.readLine()) != null) {
//            System.out.println(line);
            String[] splited = line.split("\t");
            String col1 = splited[0];
            String col2 = splited[1];

            if (col1.equals(col2)) writer.println(0);  // if not changed, mark 0
            else writer.println(1);   // if changed, mark 1
        }

        // close files
        br.close();
        writer.close();
    }
}
