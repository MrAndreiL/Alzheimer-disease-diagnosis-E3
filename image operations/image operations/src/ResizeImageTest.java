/**
 *Authors: Gradinariu Amalia-Laura, Hrimiuc Daniel-Marin
 */

import org.junit.jupiter.api.Test;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferByte;
import java.io.File;
import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;

class ResizeImageTest {
    @Test
    void isResized() {
        BufferedImage img = null;
        try {
            img = ImageIO.read(
                    new File("C:\\Users\\Amalia\\Desktop\\Anul 2 Sem 2\\IP\\creier.jpeg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        BufferedImage imgModified = ResizeImage.ResizeImage(img, 500, 400);
        File outputfile
                = new File("C:\\Users\\Amalia\\Desktop\\Anul 2 Sem 2\\IP\\imgModifiedResized.jpeg");
        try {
            ImageIO.write(imgModified, "jpeg", outputfile);
        } catch (IOException e) {
            e.printStackTrace();
        }

        BufferedImage bi = null;
        try {
            bi = ImageIO.read(
                    new File("C:\\Users\\Amalia\\Desktop\\Anul 2 Sem 2\\IP\\resizedTest.jpeg"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        assertEquals(bi, imgModified);
    }
}