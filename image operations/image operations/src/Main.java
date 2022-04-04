import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Basic_Image a = new Basic_Image();
        Basic_Image b = new Basic_Image();
        a.setImage("C:\\Users\\Rogue EX\\Desktop\\image operations\\resources\\brain.png");
        a.saveImage("png", "C:\\Users\\Rogue EX\\Desktop\\image operations\\resources\\brain.png");

        // try block to check for exceptions

        try {

            // Reading original image
            BufferedImage originalImg = ImageIO.read(
                    new File("C:\\Users\\Rogue EX\\Desktop\\image operations\\resources\\brain.png"));

            // Getting and Printing dimensions of original
            // image
            System.out.println("Original Image Dimension: "
                    + originalImg.getWidth() + "x"
                    + originalImg.getHeight());

            // Creating a subimage of given dimensions
            BufferedImage SubImg = RotateImage.rotateImage(originalImg, 45);
            //citire coordonate de la tastatura

            System.out.println("Dimensions for padding: ");
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter right border: ");
            int right_border = sc.nextInt();
            System.out.print("Enter bottom border: ");
            int bottom_border = sc.nextInt();
            System.out.print("Enter left border: ");
            int left_border = sc.nextInt();
            System.out.print("Enter top border: ");
            int top_border = sc.nextInt();

            BufferedImage paddedImage=PadImage.PadImage(originalImg, right_border, bottom_border, left_border, top_border);
            File outputfile2
                    = new File("C:\\Users\\Rogue EX\\Desktop\\image operations\\resources\\brain_pad.png");
            ImageIO.write(paddedImage, "jpeg", outputfile2);
            System.out.println("Padded image dimensions: " + paddedImage.getWidth() + "x" + paddedImage.getHeight());
            System.out.println();

            System.out.println("Dimensions for cropping: ");
            Scanner sc1 = new Scanner(System.in);
            System.out.print("Enter left border: ");
            int x1 = sc1.nextInt();
            System.out.print("Enter bottom border: ");
            int y1 = sc1.nextInt();
            System.out.print("Enter right border: ");
            int x2 = sc1.nextInt();
            System.out.print("Enter top border: ");
            int y2 = sc1.nextInt();
            BufferedImage croppedImage = CropImage.CropImage(originalImg, x1, y1, x2, y2, originalImg.getWidth()-x1, originalImg.getHeight()-y1);

            System.out.println("Cropped Image Dimension: "
                    + croppedImage.getWidth() + "x"
                    + croppedImage.getHeight());
            File outputfile1
                    = new File("C:\\Users\\Rogue EX\\Desktop\\image operations\\resources\\brain_cropped.png");
            ImageIO.write(croppedImage, "jpeg", outputfile1);
            System.out.println();

            System.out.println("We are rotating the image: ");
            //Printing Dimensions of new image created
            // (Rotated image)
            System.out.println("Rotated Image Dimension: "
                    + SubImg.getWidth() + "x"
                    + SubImg.getHeight());

            // Creating new file for rotated image
            File outputfile
                    = new File("C:\\Users\\Rogue EX\\Desktop\\image operations\\resources\\brain_rotated.png");

            // Writing image in new file created
            ImageIO.write(SubImg, "jpeg", outputfile);

        }

        // Catch block to handle the exception
        catch (IOException e) {

            // Print the line number where exception
            // occurred
            e.printStackTrace();
        }

        ContrastEnhancement.ContrastEnhancement("C:\\Users\\Rogue EX\\Desktop\\image operations\\resources\\brain.png","C:\\\\Users\\\\Rogue EX\\\\Desktop\\\\image operations\\\\resources\\\\brain_enhanced.png");
    }
}