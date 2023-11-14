import net.sourceforge.tess4j.*
import org.apache.pdfbox.Loader
import org.apache.pdfbox.pdmodel.PDDocument
import org.apache.pdfbox.text.PDFTextStripper
import java.io.File
import java.nio.file.Paths

private val basePath: String = Paths.get("").toAbsolutePath().toString();

fun main() {
    val file = "$basePath/src/main/resources/test"
    println(imageText("$file.jpg"));
    println(pdfText("$file.pdf"))
    println(imageText("$basePath/src/main/resources/rekening.jpeg"))
}

fun imageText(path: String): String {
    val tesseracts = Tesseract();
    try {
        tesseracts.setDatapath("$basePath/src/main/resources/tessdata");
        val res: String = tesseracts.doOCR(File(path));
        return res;
    } catch (e: Exception) {
        return e.toString();
    }
}

fun pdfText(path: String): String {
    val document: PDDocument = Loader.loadPDF(File(path));
    val stripper = PDFTextStripper();
    val res: String = stripper.getText(document);
    document.close();
    return res;
}