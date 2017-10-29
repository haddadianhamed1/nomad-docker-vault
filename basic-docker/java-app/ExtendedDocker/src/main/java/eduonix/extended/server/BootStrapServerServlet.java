package eduonix.extended.server;


import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.OutputStream;


public class BootStrapServerServlet extends HttpServlet {


    @Override
    public void doGet (HttpServletRequest hreq, HttpServletResponse hres)
            throws ServletException, IOException {
        String page = "<html><head><title>Embedded Tomcat Example</title></head>"
                + "<body>"
                + "<script type='text/javascript'>"
                + "function reallysure() { return confirm('Shut down process ?'); }"
                + "</script>"
                + "<h1>Welcome to your embedded web server!</h1>"
                + "<form method='POST' action='/shutdown'>"
                + "To stop the server, click on stop<br/>"
                + "<input type='submit' value='Stop' onclick='return reallysure()'/>"
                + "</form></body></html>";
        OutputStream out = hres.getOutputStream();
        out.write(page.getBytes());
        out.close();
    }
    
}
