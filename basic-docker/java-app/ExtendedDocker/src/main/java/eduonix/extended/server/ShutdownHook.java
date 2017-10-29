package eduonix.extended.server;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.OutputStream;

/**
 * Created by ubu on 01.01.15.
 */
public class ShutdownHook  extends HttpServlet {

    @Override
    public void doPost (HttpServletRequest hreq, HttpServletResponse hres) throws IOException {
        OutputStream out = hres.getOutputStream();
        out.write("Shutting down process...".getBytes());
        out.flush();
        System.exit(0);

    }
    
    
}
