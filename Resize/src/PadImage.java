
import java.awt.*;
import java.awt.image.BufferedImage;

public class PadImage {
    public static BufferedImage PadImage(BufferedImage image, int x, int y, int x1, int y1) {
        BufferedImage paddedImage = new BufferedImage(image.getWidth() + x+x1, image.getHeight()+y+y1, image.getType());

        Graphics g = paddedImage.getGraphics();

        g.setColor(Color.black);
        image=RotateImage.rotateImage(image, 180);
        g.fillRect(0, 0, image.getWidth() + x+x1, image.getHeight()+y+y1);
        g.drawImage(image, x, y, null);

        image=RotateImage.rotateImage(image, 180);
        g.fillRect(0, 0, image.getWidth() + x+x1, image.getHeight()+y+y1);
        g.drawImage(image, x1, y1, null);

        g.dispose();
        return paddedImage;
    }
}