import java.awt.image.BufferedImage;

public class CropImage {
    public static BufferedImage CropImage(BufferedImage bufferedImage, int x, int y, int x1, int y1, int width, int height){
        BufferedImage croppedImage = bufferedImage.getSubimage(x, y, width-x, height-y);
        croppedImage = RotateImage.rotateImage(croppedImage, 180);
        croppedImage = croppedImage.getSubimage(x1, y1, croppedImage.getWidth()-x1, croppedImage.getHeight()-y1);
        croppedImage = RotateImage.rotateImage(croppedImage, 180);
        return croppedImage;
    }
}