//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by FernFlower decompiler)
//

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Greyscale {
    public static void main(String[] args) throws IOException {
        BufferedImage image = null;
        File file = null;

        try {
            //AQUI COLOCA A IMAGEM QUE SERÁ CONVERTIDA
            file = new File("C:\\Users\\PICHAU\\Desktop\\imagem");
            image = ImageIO.read(file);
        } catch (IOException var14) {
            System.out.println(var14);
        }

        int width = image.getWidth();
        int height = image.getHeight();

        for(int y = 0; y < height; ++y) {
            for(int x = 0; x < width; ++x) {
                int p = image.getRGB(x, y);
                int a = p >> 24 & 255;
                int r = p >> 16 & 255;
                int g = p >> 8 & 255;
                int b = p & 255;
                int avg = (r + g + b) / 3;
                p = a << 24 | avg << 16 | avg << 8 | avg;
                image.setRGB(x, y, p);
            }
        }

        try {
            //AQUI SERÁ ONDE CRIARÁ A NOVA JUNTO DELA
            file = new File("/home/techvidvan/Desktop/imagem");
            ImageIO.write(image, "png", file);
            System.out.println("Successfully converted a colored image into a grayscale image");
        } catch (IOException var13) {
            System.out.println(var13);
        }

    }
}
