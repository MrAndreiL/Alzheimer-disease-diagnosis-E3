import java.io.IOException;

public class Basic{
    public static void main(String[] args) throws IOException {
        Basic_Image a = new Basic_Image();
        Basic_Image b = new Basic_Image();
        a.setImage("C:\\Users\\Rogue EX\\Desktop\\ip\\resources\\brainle.jpg");
        a.rotate(90);
        b.setImage("C:\\Users\\Rogue EX\\Desktop\\ip\\resources\\brainle.jpg");
        a.saveImage("png","C:\\\\Users\\\\Rogue EX\\\\Desktop\\\\ip\\\\resources\\\\brainle3.jpg");
        b.resizeImage(2100,500);
        b.saveImage("png","C:\\\\Users\\\\Rogue EX\\\\Desktop\\\\ip\\\\resources\\\\brainle4.jpg");
    }

}
