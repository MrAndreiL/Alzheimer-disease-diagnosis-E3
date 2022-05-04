import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class RotateImage {
    public static BufferedImage rotateImage(BufferedImage img, float angle)
    {
        int width = img.getWidth();
        int height = img.getHeight();
        double sin = Math.abs(Math.sin(Math.toRadians(angle))),
                cos = Math.abs(Math.cos(Math.toRadians(angle)));
        int neww = (int) Math.floor(width*cos + height*sin),
                newh = (int) Math.floor(height*cos + width*sin);
        BufferedImage newImage = new BufferedImage(neww, newh, img.getType());
        Graphics2D graphic = newImage.createGraphics();
        graphic.translate((neww-width)/2, (newh-height)/2);
        graphic.rotate(Math.toRadians(angle), width/2, height/2);
        graphic.drawRenderedImage(img, null);
        graphic.dispose();
        return newImage;
    }
    /*public static void main(String[] args)
    {
        // try block to check for exceptions
        try {

            // Reading original image
            BufferedImage originalImg = ImageIO.read(
                    new File("C:\\Users\\Raluca\\Pictures\\brain2.jpg"));

            // Getting and Printing dimensions of original
            // image
            System.out.println("Original Image Dimension: "
                    + originalImg.getWidth() + "x"
                    + originalImg.getHeight());

            // Creating a subimage of given dimensions
            BufferedImage SubImg = rotate(originalImg, 45d);

            // Printing Dimensions of new image created
            // (Rotated image)
            System.out.println("Cropped Image Dimension: "
                    + SubImg.getWidth() + "x"
                    + SubImg.getHeight());

            // Creating new file for rotated image
            File outputfile
                    = new File("C:\\Users\\Raluca\\Pictures\\ImageRotated.jpg");

            // Writing image in new file created
            ImageIO.write(SubImg, "jpg", outputfile);

            // Printing executed message
            System.out.println(
                    "Image rotated successfully: "
                            + outputfile.getPath());
        }

        // Catch block to handle the exception
        catch (IOException e) {

            // Print the line number where exception
            // occurred
            e.printStackTrace();
        }
    }

     */
}