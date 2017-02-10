package Util;

import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;

/**
 * Created by ethan on 17-1-20.
 */
public class SysOp {

    /**
     * get target directory as string
     * @return
     * @throws IOException
     * @throws URISyntaxException
     */
    public String getRoot() throws IOException, URISyntaxException {
        URL u = getClass().getProtectionDomain().getCodeSource().getLocation();
        File f = new File(u.toURI());
        String targetFile = f.getParent();
//        System.out.println(f.getParent());
        return targetFile;
    }
}
