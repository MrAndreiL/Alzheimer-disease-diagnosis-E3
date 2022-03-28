import java.io.IOException;

public class Basic_Image_Stuff {
    public static void main(String[] args) throws IOException {
        GetImage a = new GetImage();
        a.setImage("C:\\Users\\Rogue EX\\Desktop\\ip\\resources\\brain.png");
        a.saveImage("png","C:\\\\Users\\\\Rogue EX\\\\Desktop\\\\ip\\\\resources\\\\brain2.png");
    }
}
