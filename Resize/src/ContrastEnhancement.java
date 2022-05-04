import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;


public class ContrastEnhancement {

    // Try block to check for exceptions
    public static void ContrastEnhancement(String inputFile, String outputFile)
    {

        // Try block to check for exceptions
        try {

            // For proper execution of native libraries
            // Core.NATIVE_LIBRARY_NAME must be loaded
            // before calling any of the opencv methods
            System.loadLibrary(Core.NATIVE_LIBRARY_NAME);

            // Reading image from local directory by
            // creating object of Mat class
            Mat source = Imgcodecs.imread(inputFile, Imgcodecs.IMREAD_GRAYSCALE);

            Mat destination = new Mat(source.rows(), source.cols(), source.type());

            // Applying histogram equalization
            Imgproc.equalizeHist(source, destination);

            // Writing output image to some other directory
            // in local system
            Imgcodecs.imwrite( outputFile, destination);

            // Display message on console for successful
            // execution of program
            System.out.print("Image Successfully Contrasted");
        }

        // Catch block to handle exceptions
        catch (Exception e) {

            // Print the exception on the console
            // using getMessage() method
            System.out.println("error: " + e.getMessage());
        }
    }
}