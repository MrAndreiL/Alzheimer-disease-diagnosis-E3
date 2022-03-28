import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.awt.image.RenderedImage;
import java.io.File;
import java.io.IOException;
import java.io.Serializable;


public class Basic_Image implements Serializable{
    BufferedImage image;

    public Basic_Image() {
    }
    public void setImage(BufferedImage img){
        this.image = img;
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

    public void rotate(int grades)
    {
        int width = image.getWidth();
        int height = image.getHeight();

        BufferedImage newImage = new BufferedImage(
                image.getWidth(), image.getHeight(), image.getType());

        Graphics2D g2 = newImage.createGraphics();


        g2.rotate(Math.toRadians(grades), width / 2,
                height / 2);
        g2.drawImage(image, null, 0, 0);

        image = newImage;
    }
    public void resizeImage(int width, int height) {

        Image image = this.getImage();
        final BufferedImage bufferedImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        final Graphics2D graphics2D = bufferedImage.createGraphics();
        graphics2D.setComposite(AlphaComposite.Src);
        graphics2D.setRenderingHint(RenderingHints.KEY_INTERPOLATION,RenderingHints.VALUE_INTERPOLATION_BILINEAR);
        graphics2D.setRenderingHint(RenderingHints.KEY_RENDERING,RenderingHints.VALUE_RENDER_QUALITY);
        graphics2D.setRenderingHint(RenderingHints.KEY_ANTIALIASING,RenderingHints.VALUE_ANTIALIAS_ON);
        graphics2D.drawImage(image, 0, 0, width, height, null);
        graphics2D.dispose();

        this.image = bufferedImage;
    }

}
