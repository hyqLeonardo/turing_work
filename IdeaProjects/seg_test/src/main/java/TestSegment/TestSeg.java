package TestSegment;

import Util.SysOp;
import com.turing.semantic.service.api.SemanticService;
import com.turing.utils.entity.Term;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.io.*;
import java.nio.charset.Charset;
import java.util.List;


/**
 * Created by ethan on 17-1-10.
 */


public class TestSeg {

    public static void main(String args[]) throws Exception {

        TestSeg test = new TestSeg();
        SysOp s = new SysOp();
        String targetPath = s.getRoot();    // get target path

        // segment input file to output file
//        String inputFile = targetPath + "/classes/files/film_name.txt"; // path to input file
//        String outputFile = targetPath + "/classes/files/film_term_by_nature.txt";    // path to output file
//        test.segmentFile(inputFile, outputFile, "term", "n_movie");

        // one sentence
        String sentence = "分放牛班的春天主题曲会唱吗";
        test.segmentOne(sentence, "string", null);
    }

    /**
     * segment all sentences line by line in inputFile,
     * then, output origin sentence + Tab + segmented sentence
     * @param inputFile path to input file
     * @param outputFile path to output file
     * @param method set "string" to get segmented result as string, "term" as term list
     * @throws Exception
     */
    public void segmentFile(String inputFile, String outputFile, String method, String nature) throws Exception {

        // file to read
        InputStream fis = new FileInputStream(inputFile);
        InputStreamReader isr = new InputStreamReader(fis, Charset.forName("UTF-8"));
        BufferedReader br = new BufferedReader(isr);

        // file to write
        PrintWriter writer = new PrintWriter(outputFile, "UTF-8");

        // setup segment
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("classpath*:setTest.xml");
        context.start();
        SemanticService service = context.getBean("semanticService", SemanticService.class);

        // read, segment, then append line by line
        String line;
        while ((line = br.readLine()) != null) {
//            System.out.println(line);
            String seg = new String();
            if (method == "string") {
                seg = service.segmentCustomString(line, "qa", "movie_name.txt");
            } else if (method == "term") {
                List<Term> seg_term = service.segmentCustomListTerm(line, "qa", "movie_name.txt");
                if (nature != null) { // get word nature
                    for (Term t : seg_term) {
//                        System.out.println(t.getNature().equals(nature));
                        if (t.getNature().equals(nature)) seg += '\t' + t.getWord();
//                        if (t.getNature().equals(nature)) writer.println(t.getWord());
                    }
                } else seg = '\t' + seg_term.toString();   // get term list as string
            }
//            System.out.println(line + '\t' + seg);
            writer.println(line + seg);
        }

        // close files
        br.close();
        writer.close();
    }

    /**
     * segment one sentence
     * @param sentence
     * @return
     */
    public void segmentOne(String sentence, String method, String nature) {

        // setup segment
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("classpath*:setTest.xml");
        context.start();
        SemanticService service = context.getBean("semanticService", SemanticService.class);

        System.out.println(sentence);   // input sentence
        String seg = null;
        if (method == "string") {
            seg = service.segmentCustomString(sentence, "qa", "movie_name.txt");
        } else if (method == "term") {
            List<Term> seg_term = service.segmentCustomListTerm(sentence, "qa", "movie_name.txt");
            seg = seg_term.toString();
        }
        System.out.println(sentence + '\t' + seg);
    }


}