
import java.io.IOException;

public class Basic_Image_Commands {

    public static void main(String[] args) throws IOException {
        GetImage a = new GetImage();
        a.setImage("C:\\Users\\Rogue EX\\Desktop\\ip\\resources\\brain.png");
        a.saveImage("png", "C:\\\\Users\\\\Rogue EX\\\\Desktop\\\\ip\\\\resources\\\\brain6.png");
    }
}
