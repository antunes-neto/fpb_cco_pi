/**
 * File: GreenImage.java
 *
 * Description:
 * Convert color image to green image.
 *
 * @author Yusuf Shakeel
 * Date: 27-01-2014 mon
 *
 * www.github.com/yusufshakeel/Java-Image-Processing-Project
 */

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class RedImage {
    public static void main(String args[])throws IOException{
        BufferedImage img = null;
        File f = null;

        //read image
        try{
            f = new File("C:\\Users\\PICHAU\\Pictures\\imagem");
            img = ImageIO.read(f);
        }catch(IOException e){
            System.out.println(e);
        }

        //get width and height
        int width = img.getWidth();
        int height = img.getHeight();

        //convert to green image
        for(int y = 0; y < height; y++){
            for(int x = 0; x < width; x++){
                int p = img.getRGB(x,y);


                int a = (p>>24)&0xff;
                int g = (p>>16)&0xff;

                //set new RGB
                p = (a<<24) | (0<<16) | (g<<0) | 0;

                img.setRGB(x, y, p);
            }
        }

        //write image
        try{
            f = new File("C:\\Users\\PICHAU\\Pictures\\imagem");
            ImageIO.write(img, "jpg", f);
            System.out.println("Feito");
        }catch(IOException e){
            System.out.println(e);
        }
    }//main() ends here
}//class ends here