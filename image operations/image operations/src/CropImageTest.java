import org.junit.jupiter.api.Test;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferByte;
import java.io.File;
import java.io.IOException;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.*;

class CropImageTest {
    @Test
    void isCropped() {
        BufferedImage img = null;
        try {
            img = ImageIO.read(
                    new File("C:\\Users\\Amalia\\Desktop\\Anul 2 Sem 2\\IP\\creier.jpeg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        BufferedImage imgModified = CropImage.CropImage(img, 20,10, 20, 10, img.getWidth()-20, img.getHeight()-10);
        File outputfile
                = new File("C:\\Users\\Amalia\\Desktop\\Anul 2 Sem 2\\IP\\imgModifiedCropped.jpeg");
        try {
            ImageIO.write(imgModified, "jpeg", outputfile);
        } catch (IOException e) {
            e.printStackTrace();
        }

        BufferedImage bi = null;
        try {
            bi = ImageIO.read(
                    new File("C:\\Users\\Amalia\\Desktop\\Anul 2 Sem 2\\IP\\croppedTest.jpeg"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        byte[] byteArray = ((DataBufferByte) imgModified.getData().getDataBuffer()).getData();

        byte[] byteArray2 = ((DataBufferByte) bi.getData().getDataBuffer()).getData();


//        assertEquals(bi, imgModified);
        assertArrayEquals(byteArray, byteArray2);
    }
}