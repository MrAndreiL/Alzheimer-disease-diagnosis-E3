/**
        *
        */
        package commands;

/**
 * @author Raluca
 *
 */
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Main32 {
    public static void main(String[] args) throws IOException {
        int maxWidth = 0;
        int maxHeight = 0;
        Scanner sc1 = new Scanner(System.in);
        System.out.print("Enter directory: ");
        String directoryPath = sc1.nextLine();
        System.out.print("Enter output directory: ");
        String outputDirectoryPath = sc1.nextLine();
        sc1.close();
        File directory = new File(directoryPath);
        if (directory.isDirectory() && directory.list().length == 0) {
            System.out.println("Directory is empty");
        } else {
            for (File f : directory.listFiles()) {
                try {

                    BufferedImage originalImg = ImageIO.read(f);
                    if (originalImg.getWidth() > maxWidth)
                        maxWidth = originalImg.getWidth();
                    if (originalImg.getHeight() > maxHeight)
                        maxHeight = originalImg.getHeight();
                    System.out.println(
                            "Original Image Dimension: " + f.getName().substring(0, f.getName().lastIndexOf('.')) + " "
                                    + originalImg.getWidth() + "x" + originalImg.getHeight());

                } catch (final IOException e) {
                    e.printStackTrace();
                }
            }
            for (File f : directory.listFiles()) {
                try {
                    BufferedImage originalImg = ImageIO.read(f);
                    BufferedImage outputImage = null;
                    int height=originalImg.getHeight();
                    int width=originalImg.getWidth();
                    if (maxWidth == width && maxHeight == height) {
                        System.out.println("egale "+f.getName());
                        File outputfile = new File(outputDirectoryPath
                                + f.getName().substring(0, f.getName().lastIndexOf('.')) + "_resized.png");
                        ImageIO.write(originalImg, "png", outputfile);
                    } else if (maxWidth % width == 0 && maxHeight % height == 0) {
                        System.out.println("resize "+f.getName());
                        outputImage = ResizeImage.ResizeImage(originalImg, maxWidth, maxHeight);
                        File outputfile = new File(outputDirectoryPath
                                + f.getName().substring(0, f.getName().lastIndexOf('.')) + "_resized.png");
                        ImageIO.write(outputImage, "png", outputfile);
                    } else if (maxWidth==width && maxHeight % height != 0) {
                        System.out.println("pad height "+f.getName()+ " "+ ((maxHeight-height)/2));
                        outputImage = PadImage.PadImage(originalImg, 0, ((maxHeight-height)/2), 0,
                                ((maxHeight-height)/2));
                        File outputfile = new File(outputDirectoryPath
                                + f.getName().substring(0, f.getName().lastIndexOf('.')) + "_resized.png");
                        ImageIO.write(outputImage, "png", outputfile);
                    } else if (maxWidth % width != 0 && maxHeight==height) {
                        System.out.println("pad width "+f.getName()+ " "+ ((maxWidth-width)/2));
                        outputImage = PadImage.PadImage(originalImg, ((maxWidth-width)/2), 0,
                                ((maxWidth-width)/2), 0);
                        File outputfile = new File(outputDirectoryPath
                                + f.getName().substring(0, f.getName().lastIndexOf('.')) + "_resized.png");
                        ImageIO.write(outputImage, "png", outputfile);
                    } else {
                        System.out.println("else"+" "+f.getName());
                        outputImage = PadImage.PadImage(originalImg, ((maxWidth-width)/2), ((maxHeight-height)/2),
                                ((maxWidth-width)/2), ((maxHeight-height)/2));
                        File outputfile = new File(outputDirectoryPath
                                + f.getName().substring(0, f.getName().lastIndexOf('.')) + "_resized.png");
                        ImageIO.write(outputImage, "png", outputfile);
                    }
                }

                catch (final IOException e) {
                    e.printStackTrace();
                }
            }
        }
        System.out.println("Max Height:" + maxHeight);
        System.out.println("Max Width:" + maxWidth);
    }
}