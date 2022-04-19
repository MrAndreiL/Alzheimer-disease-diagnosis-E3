import org.junit.jupiter.api.Test;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferByte;
import java.io.File;
import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;

class ContrastEnhancementTest {
    @Test
    void isContrasted() {

        ContrastEnhancement.ContrastEnhancement("C:\\Users\\Amalia\\Desktop\\Anul 2 Sem 2\\IP\\creier.jpeg", "C:\\Users\\Amalia\\Desktop\\Anul 2 Sem 2\\IP\\enhancedTest.jpeg");

        BufferedImage bi = null;
        try {
            bi = ImageIO.read(
                    new File("C:\\Users\\Amalia\\Desktop\\Anul 2 Sem 2\\IP\\enhancedTest.jpeg"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        BufferedImage imgModified = null;
        try {
            imgModified = ImageIO.read(
                    new File("C:\\Users\\Amalia\\Desktop\\Anul 2 Sem 2\\IP\\enhancedTest2.jpeg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
//
//        byte[] byteArray = ((DataBufferByte) imgModified.getData().getDataBuffer()).getData();
//
//        byte[] byteArray2 = ((DataBufferByte) bi.getData().getDataBuffer()).getData();


        assertEquals(bi, imgModified);
//        assertArrayEquals(byteArray, byteArray2);
    }
}