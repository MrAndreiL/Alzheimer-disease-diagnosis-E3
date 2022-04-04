import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.awt.image.RenderedImage;
import java.io.File;
import java.io.IOException;
import java.io.Serializable;

public class Basic_Image implements Serializable {
    Image image;

    public Basic_Image() {
    }

    public void setImage(String path)   throws IOException {
        BufferedImage img = null;
        try {
            img = ImageIO.read(new File(path));
        } catch (IOException e) {
            System.out.println("read exception");
        }
        this.image = img;
    }
    public Image getImage(){
        return this.image;
    }

    public void saveImage(String extension,String path) throws IOException{
        try{
            File file = new File(path);
            ImageIO.write((RenderedImage) image,extension,file);
        }catch (IOException e) {
            System.out.println("write Exception");
        }
    }


}