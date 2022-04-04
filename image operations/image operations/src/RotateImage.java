import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class RotateImage {
    public static BufferedImage rotateImage(BufferedImage img, float angle) {
        int width = img.getWidth();
        int height = img.getHeight();
        double sin = Math.abs(Math.sin(Math.toRadians(angle))),
                cos = Math.abs(Math.cos(Math.toRadians(angle)));
        int neww = (int) Math.floor(width * cos + height * sin),
                newh = (int) Math.floor(height * cos + width * sin);
        BufferedImage newImage = new BufferedImage(neww, newh, img.getType());
        Graphics2D graphic = newImage.createGraphics();
        graphic.translate((neww - width) / 2, (newh - height) / 2);
        graphic.rotate(Math.toRadians(angle), width / 2, height / 2);
        graphic.drawRenderedImage(img, null);
        graphic.dispose();
        return newImage;
    }
}